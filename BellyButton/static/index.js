
function getOptions(){
    var select = document.getElementById('BB_DropDown');
    Plotly.d3.json('/names', function(error, names){
    if (error) return console.warn(error);

    for(var i = 0; i < names.length; i++) {
        var opt = names[i];
        var el = document.createElement("option");
        el.text = opt;
        el.value = opt;
        select.appendChild(el);
    }

    getData(names[0], buildCharts);


})};

function getData(sample, callback) {
    Plotly.d3.json(`/sample/${sample}`, function(error, sampleData){
        if (error) return console.warn(error);

        Plotly.d3.json('/otu', function(error, otuData){
            if (error) return console.warn(error);

            callback(sampleData, otuData)
        })

        Plotly.d3.json(`/metadata/${sample}`, function(error, metaData){
            if (error) return console.warn(error);

            makeMetaData(metaData);

        })
    }) 
};

// updateMetaData = populaion of data to the panel for metadata
function makeMetaData(metadata) {
    console.log(metadata['0']["GENDER"])
    document.getElementById("age").innerHTML += metadata['0']["AGE"];
    document.getElementById("bbtype").innerHTML += metadata['0']["BBTYPE"];
    document.getElementById("ethnicity").innerHTML += metadata['0']["ETHNICITY"];
    document.getElementById("gender").innerHTML += metadata['0']["GENDER"];
    document.getElementById("location").innerHTML += metadata['0']["LOCATION"];
    document.getElementById("sampleid").innerHTML += metadata['0']["SAMPLEID"];
};

function optionChanged(newSample){
    getData(newSample, makeMetaData)
};

//  updateCharts look into Plotly.restyle(chartTag, "x", [otuids])

function buildCharts(){};


function init(){
    getOptions();
};

init();