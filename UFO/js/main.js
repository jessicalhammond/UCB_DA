// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredAddresses to addressData initially
var filterdata = dataSet;

// renderTable renders the filter data to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filterdata.length; i++) {
    // Get get the current address object and its fields
    var alien = filterdata[i];
    var fields = Object.keys(alien);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = alien[field];
    }
  }
}

function handleSearchButtonClick() {
    // Set filteredAddresses to an array of all addresses whose "state" matches the filter
  filterdata = dataSet.filter(function(alien) {
    return ($datetimeInput.value.trim()===alien.datetime || $datetimeInput.value.trim()==='') &&
    ($cityInput.value.trim()===alien.city|| $cityInput.value.trim()==='') &&
    ($stateInput.value.trim()===alien.state || $stateInput.value.trim()==='') &&
    ($countryInput.value.trim()===alien.country || $countryInput.value.trim()==='') &&
    ($shapeInput.value.trim()===alien.shape|| $shapeInput.value.trim()==='');

    // If true, add the address to the filteredAddresses, otherwise don't add it to filteredAddresses
    return datetime=== filter;
  });
  // console.log(filteredAddresses)
  renderTable();
}

// Render the table for the first time on page load
renderTable();
