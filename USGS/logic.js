var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1Ijoia3JhenlraWVrYSIsImEiOiJjamlkdmxkY2EwZnI0M3FxdjBzZXBkem1lIn0.8WybYg6XgM_dZQhcP0r_Hw");
  
var geoMap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1Ijoia3JhenlraWVrYSIsImEiOiJjamlkdmxkY2EwZnI0M3FxdjBzZXBkem1lIn0.8WybYg6XgM_dZQhcP0r_Hw");
    
// Define a baseMaps object to hold our base layers
var baseMaps = {
  "Street Map": streetmap,
  "Geo Map": geoMap
};

var techPlates = new L.LayerGroup();

var earthquakes = new L.LayerGroup();

var overlayMaps = {
  Earthquakes: earthquakes,
  TechPlates: techPlates
};

var myMap = L.map("map", {
  center: [
    37.09, -95.71
  ],
  zoom: 5,
  layers: [streetmap, geoMap]
});

// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  console.log(data);
  
  function styleInfo(feature){
    return {
      opacity: 1,
      fillOpacity: .5,
      fillColor: getColor(feature.properties.mag),
      color: '#009cf6',
      radius: getRadius(feature.properties.mag),
      weight: .5,
      stroke: true
    };
  }

  function getColor(mag){
      switch (true) {
      case mag > 5:
        return "red";
      case mag > 4:
        return "orange";
      case mag > 3:
        return "yellow";
      case mag > 2:
        return "#7FFF00";
      case mag > 1:
        return "green";
      default:
        return "blue";
      };
    }

  function getRadius(mag){
    if (mag === 0) {
      return 1;
    }  
    return mag*4; 
  }

  L.geoJSON(data, {
    onEachFeature: function (feature, layer){
      layer.bindPopup("<h3>" + feature.properties.place + 
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
    }, 
    pointToLayer: function(feature, latlng){
      return L.circleMarker(latlng)
    },
    style: styleInfo
  }).addTo(earthquakes);

  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

  var link = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";

  d3.json(link, function(plateData) {
    L.geoJSON(plateData, {
      color: "orange",
      weight: 1
    }).addTo(techPlates);
  });

  var legend = L.control({ position: "bottomright" });
  
  legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");
    var limits = [0,1,2,3,4,5]
    var colors = ["blue" , "green", "#7FFF00", "yellow", "orange", "red"]
  
    // Loop through our intervals and generate a label with a colored square for each interval.
    for (var i = 0; i < limits.length; i++) {
      div.innerHTML += "Mag Scale<br><i style='color: " + colors[i] + "'>" +
        limits[i] + (limits[i + 1] ? "&ndash;" + limits[i + 1] + "<br>" : "+") + "</i>";
    }
    return div;
  };

  // Adding legend to the map
  legend.addTo(myMap);

});


