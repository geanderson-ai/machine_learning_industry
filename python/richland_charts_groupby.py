from flask import Flask, jsonify, json
import pandas as pd


richland_L1_S1_down_groupby = pd.read_csv('richland_L1_S1_down_groupby.csv')
richland_L1_S2_down_groupby = pd.read_csv('richland_L1_S2_down_groupby.csv')
richland_L1_S3_down_groupby = pd.read_csv('richland_L1_S3_down_groupby.csv')
richland_L1_S4_down_groupby = pd.read_csv('richland_L1_S4_down_groupby.csv')
richland_L1_S5_down_groupby = pd.read_csv('richland_L1_S5_down_groupby.csv')

richland_L1_S1_up_groupby = pd.read_csv('richland_L1_S1_up_groupby.csv')
richland_L1_S2_up_groupby = pd.read_csv('richland_L1_S2_up_groupby.csv')
richland_L1_S3_up_groupby = pd.read_csv('richland_L1_S3_up_groupby.csv')
richland_L1_S4_up_groupby = pd.read_csv('richland_L1_S4_up_groupby.csv')
richland_L1_S5_up_groupby = pd.read_csv('richland_L1_S5_up_groupby.csv')


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/richland/downtime/groupby")
def hello():
    L1_S1 = richland_L1_S1_down_groupby.to_list()
    L1_S2 = richland_L1_S2_down_groupby.to_list()
    L1_S3 = richland_L1_S3_down_groupby.to_list()
    L1_S4 = richland_L1_S4_down_groupby.to_list()
    L1_S5 = richland_L1_S5_down_groupby.to_list()

    return jsonify ({'L1 S1': L1_S1, 'L1 S2': L1_S2, 'L1 S3': L1_S3, 'L1 S4': L1_S4, 'L1 S5': L1_S5})

@app.route("/richland/uptime/groupby")
def hello():
    L1_S1 = richland_L1_S1_down_groupby.to_list()
    L1_S2 = richland_L1_S2_down_groupby.to_list()
    L1_S3 = richland_L1_S3_down_groupby.to_list()
    L1_S4 = richland_L1_S4_down_groupby.to_list()
    L1_S5 = richland_L1_S5_down_groupby.to_list()

    return jsonify ({'L1 S1': L1_S1, 'L1 S2': L1_S2, 'L1 S3': L1_S3, 'L1 S4': L1_S4, 'L1 S5': L1_S5})



if __name__ == '__main__':
    app.run(debug=True)
