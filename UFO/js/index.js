var tbody = document.querySelector("tbody");
var filterInput = document.querySelector("#filter");
var searchBtn = document.querySelector("#searchbtn");
var td = document.querySelector('td');
var tr = document.querySelector('tr');


searchBtn.addEventListener('click', executeSearch);

var ufodata = dataSetTest;


console.log(ufodata)

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
    var filterValue = filterInput.value.trim().toLowerCase();
    console.log(filterValue);

    tableReturn = dataSetTest.filter(function(sighting) {
        var date = sighting.datetime.trim().toLowerCase();
        var city = sighting.city.trim().toLowerCase();
        var state = sighting.state.trim().toLowerCase();
        var country = sighting.country.trim().toLowerCase();
        var shape = sighting.shape.trim().toLowerCase();
        // var duration = sighting.durationMinutes.trim().toLowerCase();
        return ( (date == filterValue) &&  (city == filterValue) &&
        (state == filterValue) && (country == filterValue) && 
        (shape == filterValue));
    });
    // console.log(tableReturn);
    makeTable();
}

makeTable();

