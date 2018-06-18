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
    
    // var dateValue = datetime.value.trim().toLowerCase();
    // var cityValue = city.value.trim().toLowerCase();
    // var stateValue = state.value.trim().toLowerCase();
    // var countryValue = country.value.trim().toLowerCase();
    // var shapeValue = shape.value.trim().toLowerCase();
    console.log(date.value, city.value);

    var tableReturn = dataSetTest.filter(function(sighting) {
        return (datetime.value.trim()===sighting.datetime || datetime.value.trim()==='') &&
        (city.value.trim()===sighting.city|| city.value.trim()==='') &&
        (state.value.trim()===sighting.state || state.value.trim()==='') &&
        (country.value.trim()===sighting.country || country.value.trim()==='') &&
        (shape.value.trim()===sighting.shape|| shape.value.trim()==='');
    });
    makeTable(tableReturn);
}
makeTable();



