// var tbody = document.querySelector("tbody");
// var filterInput = document.querySelector("#filter");
// var searchBtn = document.querySelector("#searchbtn");
// var td = document.querySelector('td');
// var tr = document.querySelector('tr');

// searchBtn.addEventListener('click', executeSearch);

//  create an array for the list of cities, then use d3 
// to append the list to option elements in drop down.
var cities = for city in results; 


function executeSearch() {
    // global
    var filtertable = filterInput.value.trim().toLowerCase(); 
    // categories
    var state = stateInput.value.trim().toLowerCase();
    var country = countryInput.value.trim().toLowerCase();
    
    ufodata = dataSet.filter(function(sighting) {
        var sightingstate = sighting.state.toLowerCase();
        var sightingcountry = sighting.country.toLowerCase();
        var sightingcity = sighting.city.toLowerCase();
        var sightingdate = sighting.datetime.toLowerCase();
        var sightingshape = sighting.shape.toLowerCase();	
        if sightingstate = 
        return (sightingstate == filtertable||sightingcity == filtertable
            ||sightingcountry == filtertable
            || sightingcity == filtertable
            ||sightingdate == filtertable
            || ) {
            
        } 
    

    //     if (sightingdate == filtertable) {
    //         return sightingdate == filtertable
    //     }
    //     if (sightingshape == filtertable) {
    //         return sightingshape == filtertable
    //     }
    // });
    console.log(filtertable)
    makeTable(newtable);
}


// function executeSearch() {
//     setFilteredGrid()
// }

// function executeSearch() {
//     var filterValue = filterInput.value.trim().toLowerCase();
//     console.log(filterValue);

//     tableReturn = dataSetTest.filter(function(sighting) {
//         var date = sighting.datetime.trim().toLowerCase();
//         var city = sighting.city.trim().toLowerCase();
//         var state = sighting.state.trim().toLowerCase();
//         var country = sighting.country.trim().toLowerCase();
//         var shape = sighting.shape.trim().toLowerCase();
//         // var duration = sighting.durationMinutes.trim().toLowerCase();
//         return ( (date == filterValue) &&  (city == filterValue) &&
//         (state == filterValue) && (country == filterValue) && 
//         (shape == filterValue));
//     });
//     // console.log(tableReturn);
//     makeTable();
// }
