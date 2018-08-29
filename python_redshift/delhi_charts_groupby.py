from flask import Flask, jsonify, json
import pandas as pd

delhi_bagger1_up_groupby = pd.read_csv('delhi_bagger1_up_groupby.csv')
delhi_bagger1_down_groupby = pd.read_csv('delhi_bagger1_down_groupby.csv')

delhi_bagger2_up_groupby = pd.read_csv('delhi_bagger2_up_groupby.csv')
delhi_bagger2_down_groupby = pd.read_csv('delhi_bagger2_down_groupby.csv')

delhi_bagger3_up_groupby = pd.read_csv('delhi_bagger3_up_groupby.csv')
delhi_bagger3_down_groupby = pd.read_csv('delhi_bagger3_down_groupby.csv')

delhi_bagger4_up_groupby = pd.read_csv('delhi_bagger4_up_groupby.csv')
delhi_bagger4_down_groupby = pd.read_csv('delhi_bagger4_down_groupby.csv')

delhi_bagger5_up_groupby = pd.read_csv('delhi_bagger5_up_groupby.csv')
delhi_bagger5_down_groupby = pd.read_csv('delhi_bagger5_down_groupby.csv')



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/delhi/downtime/groupby")
def hello():
    bagger1 = delhi_bagger1_down_groupby.to_list()
    bagger2 = delhi_bagger2_down_groupby.to_list()
    bagger3 = delhi_bagger3_down_groupby.to_list()
    bagger4 = delhi_bagger4_down_groupby.to_list()
    bagger5 = delhi_bagger5_down_groupby.to_list()
    
    return jsonify ({'bagger1': bagger1, 'bagger2': bagger2, 'bagger3': bagger3, 'bagger4': bagger4, 'bagger5': bagger5})

@app.route("/delhi/uptime/groupby")
def hello():
    bagger1 = delhi_bagger1_up_groupby.to_list()
    bagger2 = delhi_bagger2_up_groupby.to_list()
    bagger3 = delhi_bagger3_up_groupby.to_list()
    bagger4 = delhi_bagger4_up_groupby.to_list()
    bagger5 = delhi_bagger5_up_groupby.to_list()

    return jsonify ({'bagger1': bagger1, 'bagger2': bagger2, 'bagger3': bagger3, 'bagger4': bagger4, 'bagger5': bagger5})




if __name__ == '__main__':
    app.run(debug=True)
