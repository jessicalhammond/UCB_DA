# Pandas
import pandas as pd

#flash and jasonify
from flask import Flask, jsonify, make_response, render_template, redirect

#################################################
# Flask Setup
#################################################
app = Flask(__name__, static_url_path='/static')

#################################################
# Flask Routes
#################################################

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/names")
def names():
    names_1 = pd.read_excel("bbnames.xlsx", sheet_name=0, header=0, skiprows = None)
    trans = names_1.transpose()
    df = trans[0][2:]
    otu_id = list(df.index[:-1])
    otu_id
    # otu_id_list = ["BB_" + str(s) for s in otu_id]
    return jsonify(otu_id)

@app.route("/otu")
def otu():
    names_1 = pd.read_excel("bbnames.xlsx", sheet_name=0, header=0, skiprows = None)
    otu_descrip = names_1['Lowest Taxonomic Level of Bacteria/Archaea Found']
    otu_descrip = list(otu_descrip)
    return jsonify(otu_descrip)

@app.route("/metadata/<sample_id>")
def metadata(sample_id):
    sample_data = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')
    sample_return = sample_data.loc[sample_data['SAMPLEID'] == int(sample_id)]
    json_return = sample_return.to_json(orient='index')
    return json_return

@app.route("/wfreq/<sample_id>")
def wfreq(sample_id):
    sample_data = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')
    sample_return = sample_data.loc[sample_data['SAMPLEID'] == int(sample_id)]
    sample_return = sample_return['WFREQ'].to_json()
    return jsonify(sample_return)

@app.route("/sample/<sample_id>")
def email(sample_id):
    sample_data = pd.read_csv('belly_button_biodiversity_samples.csv')
    sample_data.head()
    value =  sample_data.loc[:, sample_data.columns.str.contains(sample_id)]
    new = value["BB_" + sample_id]
    new = new.sort_values(ascending =False)
    # new = pd.DataFrame(filter(lambda a: a != 0, new))
    newj = new.to_json(orient='split')
    return newj

@app.route("/team")
def team():
    return render_template('team.html')
if __name__ == '__main__':
    app.run(debug=True)
