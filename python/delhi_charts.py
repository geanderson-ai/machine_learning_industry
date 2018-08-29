from flask import Flask, jsonify, json
import pandas as pd

delhi_bagger1_up = pd.read_csv('delhi_bagger1_up.csv')
delhi_bagger1_down = pd.read_csv('delhi_bagger1_down.csv')

delhi_bagger2_up = pd.read_csv('delhi_bagger2_up.csv')
delhi_bagger2_down = pd.read_csv('delhi_bagger2_down.csv')

delhi_bagger3_up = pd.read_csv('delhi_bagger3_up.csv')
delhi_bagger3_down = pd.read_csv('delhi_bagger3_down.csv')

delhi_bagger4_up = pd.read_csv('delhi_bagger4_up.csv')
delhi_bagger4_down = pd.read_csv('delhi_bagger4_down.csv')

delhi_bagger5_up =  pd.read_csv('delhi_bagger5_up.csv')
delhi_bagger5_down =  pd.read_csv('delhi_bagger5_down.csv')




app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/delhi/downtime/")
def hello():
    bagger1 = delhi_bagger1_down.to_list()
    bagger2 = delhi_bagger2_down.to_list()
    bagger3 = delhi_bagger3_down.to_list()
    bagger4 = delhi_bagger4_down.to_list()
    bagger5 = delhi_bagger5_down.to_list()
    
    return jsonify ({'bagger1': bagger1, 'bagger2': bagger2, 'bagger3': bagger3, 'bagger4': bagger4, 'bagger5': bagger5})

@app.route("/delhi/uptime/")
def hello():
    bagger1 = delhi_bagger1_up.to_list()
    bagger2 = delhi_bagger2_up.to_list()
    bagger3 = delhi_bagger3_up.to_list()
    bagger4 = delhi_bagger4_up.to_list()
    bagger5 = delhi_bagger5_up.to_list()

    return jsonify ({'bagger1': bagger1, 'bagger2': bagger2, 'bagger3': bagger3, 'bagger4': bagger4, 'bagger5': bagger5})




if __name__ == '__main__':
    app.run(debug=True)
