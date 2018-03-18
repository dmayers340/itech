 var map, marker;
 var geoLocatorMarker, geoLocatorInfoWindow;
 var directionsService, directionsDisplay, currentLat, currentLng, currentPosition;
 var campus, lat, lng;

function initMap() {

	map = new google.maps.Map(document.getElementById('map'), {
 	mapTypeId: google.maps.MapTypeId.ROADMAP,
  	});

	campus  = new google.maps.LatLng(55.872084,-4.288222);
	map.setCenter(campus);

	directionsDisplay = new google.maps.DirectionsRenderer();
	directionsService = new google.maps.DirectionsService();
}

function loadLocation(fLat, fLng){

	var baseurl = window.location.origin; 

	lat = fLat; 
	lng = fLng;

	marker = new google.maps.Marker({
		position: new google.maps.LatLng(lat, lng),
		map: map,
		icon: {
			url: baseurl + "/static/img/icon.svg",
			scaledSize: new google.maps.Size(60, 50)
		},
		visible: true
	  });

	var locationWindow = new google.maps.InfoWindow;
		locationWindow.setContent('Your destination');
		locationWindow.open(map, marker);

	locateUser(); 
}

function calcRoute(directionsService, directionsDisplay) { 
		
	directionsDisplay.setMap(map);

	var request = {
		origin: new google.maps.LatLng(currentPosition),
		destination: new google.maps.LatLng(lat, lng),
		travelMode: 'WALKING'
	};
	
	directionsService.route(request, function(result, status) { 
			if (status == 'OK') {
			directionsDisplay.setOptions({ preserveViewport: true });
			directionsDisplay.setDirections(result);
		}  
	});

	map.setZoom(17);
	map.setCenter(new google.maps.LatLng(lat, lng));

}

function locateUser(){ 

	if (navigator.geolocation) {

	  navigator.geolocation.getCurrentPosition(function(position) {
		currentPosition = {
		  lat: position.coords.latitude,
		  lng: position.coords.longitude
		};

		currentLat = position.coords.latitude;
		currentLng = position.coords.longitude;

		var pos = new google.maps.LatLng(currentPosition);
		geoLocatorInfoWindow = new google.maps.InfoWindow;
		geoLocatorMarker = new google.maps.Marker({map: map});

		geoLocatorMarker.setPosition(pos);
		geoLocatorInfoWindow.setContent('Your location');
		geoLocatorInfoWindow.open(map, geoLocatorMarker);

		calcRoute(directionsService, directionsDisplay); 

	}, function() {
	handleLocationError(true, geoLocatorInfoWindow);
	});
	} else {
	  // Browser doesn't support Geolocation
	  handleLocationError(false, geoLocatorInfoWindow);
	}
}

function handleLocationError(browserHasGeolocation, geoLocatorInfoWindow) {	
	var errorposition = new google.maps.LatLng(lat, lng);
	geoLocatorInfoWindow = new google.maps.InfoWindow;
	geoLocatorInfoWindow.setPosition(errorposition);
	geoLocatorInfoWindow.setContent( 'Error: The Geolocation service failed.Your browser doesn\'t support geolocation.'); 
	geoLocatorInfoWindow.open(map);
}

function removeForm1(){
	console.log("remove");
}

function printRating(r) {
   			var x ="", i;
   			for (i=1; i<=r; i++) {
       			 x = x + "<i class='fas fa-star'></i> ";  
   			 }		
    		document.getElementById("rating").innerHTML = x;
}