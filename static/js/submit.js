var map, marker; 
				var position, currentLatitude, currentLongitude;
				var campus;

				// initialises a new map 
				function initMap() {
					map = new google.maps.Map(document.getElementById('map'), {
					  zoom: 17,
					  mapTypeId: google.maps.MapTypeId.ROADMAP,
					});

					campus  = new google.maps.LatLng(55.872084,-4.288222);
					map.setCenter(campus);

					marker = new google.maps.Marker({
						map: map, 
						position: campus,
						visible: true, 
						draggable: true
					}); 

					google.maps.event.addListener(marker, 'dragend', function(marker){
						position = marker.latLng; 
						currentLatitude = position.lat();
						currentLongitude = position.lng();
						console.log(currentLatitude, currentLongitude);
						document.getElementById("latitude").value=currentLatitude;
						document.getElementById("longitude").value=currentLongitude;
					 });
				}