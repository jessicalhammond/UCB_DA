var tbody = document.querySelector("tbody");
var global = document.querySelector('#global');
var datetime = document.querySelector("#date");
var city = document.querySelector("#city");
var state = document.querySelector("#state");
var country = document.querySelector("#country");
var shape = document.querySelector("#shape");
var searchBtn = document.querySelector("#searchbtn");

searchBtn.addEventListener('click', executeSearch);

var ufodata = dataSetTest;

function makeTable(){
    tbody.innerHTML = "";
    for (var i = 0; i < ufodata.length; i++) {
        var sighting = ufodata[i];
        var fields = Object.keys(sighting);
        var row = tbody.insertRow(i);
        for (j = 0; j < fields.length; j++) {
            var field = fields[j];
            var cell = row.insertCell(j);
            cell.innerText = sighting[field];
        }
    }
}

function executeSearch() {
    var dateValue = datetime.value.trim().toLowerCase();
    var cityValue = city.value.trim().toLowerCase();
    // var stateValue = state.value.trim().toLowerCase();
    // var countryValue = country.value.trim().toLowerCase();
    var shapeValue = shape.value.trim().toLowerCase();
    console.log(dateValue, cityValue);

    var tableReturn = dataSetTest.filter(function(sighting) {
        var dateData = sighting.datetime.trim().toLowerCase();
        var cityData = sighting.city.trim().toLowerCase();
        var stateData = sighting.state.trim().toLowerCase();
        var countryData = sighting.country.trim().toLowerCase();
        var shapeData = sighting.shape.trim().toLowerCase();
        if (dateValue && (dateData != dateValue)){
            return false;
        }
        if (cityValue && (cityData != cityValue)) {        
            return false;
        }
        // if (stateValue && (stateData != stateValue)) {
        //     return false;
        // }
        // if (countryValue && (countryData != countryValue)) {
        //     return false;
        // }
        if (shapeValue && (shapeData != shapeValue)) {
            return false;
        }
        return true;
        // console.log(tablereturn)
        // console.log(cityValue == sighting.city.trim().toLowerCase()|| cityValue==='')
        return (dateValue == sighting.datetime.trim().toLowerCase() || dateValue==='') &&
        (cityValue == sighting.city.trim().toLowerCase()|| cityValue==='') &&
        (stateValue == sighting.state.trim().toLowerCase() || stateValue==='') &&
        (countryValue == sighting.country.trim().toLowerCase() || countryValue==='') &&
        (shapeData==shapeValue|| shapeValue==='');
        return datetime=== filter
    });
    makeTable();
}
makeTable();



