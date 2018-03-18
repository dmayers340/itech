
var map, infowindow, markers, infoWindows, campus; 
var geoLocatorMarker, geoLocatorInfoWindow;
var directionsService, directionsDisplay, currentLat, currentLng, currentPosition, pos; 
var locations;
var baseurl;

function initMap() {

	baseurl = window.location.origin;

	map = new google.maps.Map(document.getElementById('map'), {
 	mapTypeId: google.maps.MapTypeId.ROADMAP,
  	});

	campus  = new google.maps.LatLng(55.872084,-4.288222);
	map.setCenter(campus);

	 directionsDisplay = new google.maps.DirectionsRenderer();
	 directionsService = new google.maps.DirectionsService();
	
	 geoLocatorInfoWindow = new google.maps.InfoWindow;
	 geoLocatorMarker = new google.maps.Marker({map: map}); 
} 

function loadAll()
{	
	
	var marker, i;

	markers = [];
	infoWindows = [];

	infowindow = new google.maps.InfoWindow({
			maxWidth: 200
	});

	infoWindows.push(infowindow);
	infoWindows.push(geoLocatorInfoWindow);

	for (i = 0; i < locations.length; i++) {  
			   	marker = new google.maps.Marker({
				position: new google.maps.LatLng(locations[i][1], locations[i][2]),
				map: map,
				building: locations[i][12],
				floor: locations[i][5],
				icon: {
				url: baseurl + "/static/img/icon.svg",
				scaledSize: new google.maps.Size(60, 50)
				},
				visible: true
			  }); 
			 
			  google.maps.event.addListener(marker, 'click', (function(marker, i) {
				return function() {

				clearInfoWindows(); 

				infowindow.setContent(
				  	"<h4>" + locations[i][0] + "</h4><br/>" + // name   
				  	"<img width='150' src= '" + baseurl + "/media/" + locations[i][3] + " '/><hr>" + 
				  	locations[i][4] + "<br/></br>" + // description
				  	"<b>Building: </b>" + locations[i][12] + "</br>" +
				  	"<b>Floor: </b>" + locations[i][5] + "</br> "+
				  	"<b>Broken? </b>" + locations[i][11] + "</br></br>" +
				  	"<b>Visit the " + "<a href ='/fountain/"+locations[i][13]+"'> fountain page</a> to see the reviews or rate this fountain!</b>"
				  	);
				 infowindow.open(map, marker);

				 var endPosition = locations[i]; 

					// current location to a fountain 
				  
				  calcRoute(directionsService, directionsDisplay, endPosition);
				}
			  })(marker, i));

			  markers.push(marker);
			}

	setBounds();	
}

function clearMarkers() {
	for (var i = 0; i < markers.length; i++) {
		 markers[i].setVisible(false);
		 }
}

function clearInfoWindows() {
	for (var i = 0; i < infoWindows.length; i++) {
		 infoWindows[i].close();
		 }

}

function showAllMarkers(){		
	clearInfoWindows(); 

	for (var i = 0; i < markers.length; i++) {
		 markers[i].setVisible(true);
		 }
		setBounds();
}

function sortMarkers() {
	showBuilding = document.getElementById("Building").value;
	showFloor = document.getElementById("Floor").value; 

	clearMarkers();
	clearInfoWindows(); 

	if (showBuilding == "all"){
		showAllMarkers(); 
	}

	else if (showFloor == "all") {
		var i;
		for (i = 0; i < markers.length; i++) {
			if (markers[i].building == showBuilding) {
				markers[i].setVisible(true);
				map.setCenter(markers[i].getPosition());
				map.setZoom(17); 
			} 
		}
	}
	
	else {
		var i;
		var f = false; 
		for (i = 0; i < markers.length; i++) {
			if (markers[i].building == showBuilding){
				if (markers[i].floor == showFloor){
					markers[i].setVisible(true);
					map.setCenter(markers[i].getPosition());
					map.setZoom(17);
					f = true;
				}
			} 	
		}
		
		if (f == false) {
			setBounds(); 
			geoLocatorInfoWindow.setPosition(campus);
			geoLocatorInfoWindow.setContent("Sorry, couldn't locate any fountains! </br></br> Try selecting a different floor or a building."); 
			geoLocatorInfoWindow.open(map);
		}
	}

}

function findNearest()
{	
	var pi = Math.PI;
    var R = 6371; //equatorial radius
    var distances = [];
    var closest = -1;

    for( i=0;i<markers.length; i++ ) {  
        var lat2 = markers[i].position.lat();
        var lon2 = markers[i].position.lng();

        var chLat = lat2-currentLat;
        var chLon = lon2-currentLng;

        var dLat = chLat*(pi/180);
        var dLon = chLon*(pi/180);

        var rLat1 = currentLat*(pi/180);
        var rLat2 = lat2*(pi/180);

        var a = Math.sin(dLat/2) * Math.sin(dLat/2) + 
                    Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(rLat1) * Math.cos(rLat2); 
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
        var d = R * c;

        distances[i] = d;
        if ( closest == -1 || d < distances[closest] ) {
            closest = i;
        }

	    clearMarkers();
	    markers[closest].visible = true;
	    var endPosition = locations[closest]; 

	    google.maps.event.trigger(markers[closest], 'click');
	}
}

function locateUser() 
{		
		// Try HTML5 geolocation.
			if (navigator.geolocation) {

				  navigator.geolocation.getCurrentPosition(function(position) {
					currentPosition = {
					  lat: position.coords.latitude,
					  lng: position.coords.longitude
					};

					currentLat = position.coords.latitude;
					currentLng = position.coords.longitude;
					pos = new google.maps.LatLng(currentPosition);
					
					geoLocatorMarker.setPosition(pos);
					geoLocatorInfoWindow.setContent('Your location');
					geoLocatorInfoWindow.open(map, geoLocatorMarker);

					setBounds();

				}, function() {
				handleLocationError(true, infoWindow);
				});
			} else {
			  // Browser doesn't support Geolocation
			  handleLocationError(false, infoWindow);
		}
}

function calcRoute(directionsService, directionsDisplay, endPoint) {
	
	directionsDisplay.setMap(map);

	var lat1 = endPoint[1];
	var lng1 = endPoint[2];

	var request = {
		origin: new google.maps.LatLng(currentPosition),
		destination: new google.maps.LatLng(lat1,lng1),
		travelMode: 'WALKING'
	};
	
	directionsService.route(request, function (result, status) {
	if (status == 'OK') {
	directionsDisplay.setOptions({ preserveViewport: true });
	directionsDisplay.setDirections(result);
	} else {
	directionsDisplay.setOptions({ preserveViewport: true });
	}
		});

	map.setZoom(17);
	map.setCenter(new google.maps.LatLng(lat1,lng1));

}

function setBounds() {
	var bounds = new google.maps.LatLngBounds();
	for (var i =0; i<markers.length; i++) {
		bounds.extend(markers[i].getPosition());
	}
	map.fitBounds(bounds);
}

function enableFloor(){
	if (document.getElementById("Building").value == "all") {
		document.getElementById("Floor").disabled=true;
	}else{
		document.getElementById("Floor").disabled=false;
	}
}

function showGreeting(){
	var infowindow2 = new google.maps.InfoWindow({
			maxWidth: 200});
	infowindow2.setPosition(campus);
	infowindow2.setContent("<h5>Welcome to<h5>Find A Fountain!</h5><hr><font size='3'>Select one of the options above or click on any of the fountains to get directions, rate a fountain, leave a review, and more. <hr> Just keep in mind that location services are needed to fully enjoy this site.</font>");
	infowindow2.open(map);
}

// if geolocation disabled 
function handleLocationError(browserHasGeolocation, geoLocatorInfoWindow) {
	
	geoLocatorInfoWindow.setPosition(campus);
	geoLocatorInfoWindow.setContent(browserHasGeolocation ?
				  'Error: The Geolocation service failed.' :
				  'Error: Your browser doesn\'t support geolocation.'); 
	geoLocatorInfoWindow.open(map);
}
