from flask import Flask, jsonify, json
import pandas as pd

park_S6_down = pd.read_csv('park_string6_down.csv')
park_S6_up = pd.read_csv('park_string6_up.csv')
park_S7_down = pd.read_csv('park_string7_down.csv')
park_S7_up = pd.read_csv('park_string7_up.csv')
park_S8_down = pd.read_csv('park_string8_down.csv')
park_S8_up = pd.read_csv('park_string8_up.csv')
park_S9_down = pd.read_csv('park_string9_down.csv')
park_S9_up = pd.read_csv('park_string9_up.csv')
park_S45_down = pd.read_csv('park_string45_down.csv')
park_S45_up = pd.read_csv('park_string45_up.csv')
park_S1_down = pd.read_csv('park_string1_down.csv')
park_S1_up = pd.read_csv('park_string1_up.csv')
park_S2_down = pd.read_csv('park_string2_down.csv')
park_S2_up = pd.read_csv('park_string2_up.csv')
park_S3_down = pd.read_csv('park_string3_down.csv')
park_S3_up = pd.read_csv('park_string3_up.csv')
park_S4_down = pd.read_csv('park_string4_down.csv')
park_S4_up = pd.read_csv('park_string4_up.csv')
park_S5_down = pd.read_csv('park_string5_down.csv')
park_S5_up = pd.read_csv('park_string5_up.csv')




app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/park/downtime/")
def downtime():
    S6 = park_S6_down.to_list()
    S7 = park_S7_down.to_list()
    S8 = park_S8_down.to_list()
    S9 = park_S9_down.to_list()
    S45 = park_S45_down.to_list()
    S1 = park_S1_down.to_list()
    S2 = park_S2_down.to_list()
    S3 = park_S3_down.to_list()
    S4 = park_S4_down.to_list()
    S5 = park_S5_down.to_list()
    return jsonify ({'S6': S6, 'S7': S7, 'S8': S8, 'S9': S9, 'S45': S45, 'S1': S1, 'S2': S2, 'S3': S3, 'S4': S4, 'S5': S5})

@app.route("/park/uptime/")
def uptime():
    S6 = park_S6_up.to_list()
    S7 = park_S7_up.to_list()
    S8 = park_S8_up.to_list()
    S9 = park_S9_up.to_list()
    S45 = park_S45_up.to_list()
    S1 = park_S1_up.to_list()
    S2 = park_S2_up.to_list()
    S3 = park_S3_up.to_list()
    S4 = park_S4_up.to_list()
    S5 = park_S5_up.to_list()
    return jsonify ({'L1 S6': S6, 'L1 S7': S7, 'L1 S8': S8, 'L1 S9': S9, 'L1 S10': S10, 'L2 S1': S1, 'L2 S2': S2, 'L2 S3': S3, 'LS S4': LS_S4, 'L2 S5': S5})




if __name__ == '__main__':
    app.run(debug=True)
