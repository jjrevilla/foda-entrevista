var FRDLocation = function () {
};

// Uso variables globales, pues asi solo las creo una vez y no en cada
// llamada a las funciones
var map; // variable global del mapa
var geocoder; // variable global para obtener direcciones
var marker; //variable global del marcador

var latitude;
var longitude;

// Funcion para dibujar un marker en el mapa
function placeMarker(location) {
  if ( marker ) {
    marker.setPosition(location);
  } else {
    marker = new google.maps.Marker({
      position: location,
      map: map
    });
  }
}

// Funcion para recuperar el nombre de la calle, distrito, etc
// basado en la coordenada actual del marker
function codeLatLng(location) {
    var latlng = new google.maps.LatLng(latitude, longitude);
    geocoder.geocode({'latLng': location}, function(results, status) {
	if (status == google.maps.GeocoderStatus.OK) {
            if (results[0]) {		
		var address = results[0].formatted_address.split(',')[0];
		var district = results[1].formatted_address.split(',')[0];
		var city = results[3].formatted_address.split(',')[0];	
		$('#inputAddress').val(address);
		$('#inputDistrict').val(district);
		$('#inputCity').val(city);
            }
	} else {
            alert("Geocoder failed due to: " + status);
	}
    });
}

// Inicializacion del Mapa
FRDLocation.set_location = function (position) {
    
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
    
    var coords = new google.maps.LatLng(latitude, longitude);    

    var options = {
        zoom                    : 16,
        center                  : coords,
        mapTypeControl          : false,
        navigationControlOptions: {
            style: google.maps.NavigationControlStyle.SMALL
        },
        disableDefaultUI        : true,
        //zoomControl: true,
        mapTypeId               : google.maps.MapTypeId.ROADMAP
    };
    
    geocoder = new google.maps.Geocoder();
    map = new google.maps.Map(document.getElementById("location-map"), options);
    // Añaden dos eventos, uno al crear el marker, y el otro
    // para recuperar las direcciones
    google.maps.event.addListener(map, 'click', function(event) {	
	placeMarker(event.latLng);
	codeLatLng(event.latLng);
    });    
};

jQuery(document).ready(function () {
    Utils.geo_location(FRDLocation.set_location);    
});
