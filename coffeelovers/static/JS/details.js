function initMap() {
      var macc =  {lat: -37.964577, lng: -57.547188};
      var map = new google.maps.Map(
           document.getElementById('map'), {zoom: 15, center: macc});
      var marker = new google.maps.Marker({position: macc, map: map});
    }


function myFunction() {
      document.getElementById("myText").autofocus = true;  
}
