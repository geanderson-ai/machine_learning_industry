from flask import Flask, jsonify, json
import pandas as pd

boardman_east_B1_down = pd.read_csv('boardman_east_B1_down.csv')
boardman_east_B2_down = pd.read_csv('boardman_east_B2_down.csv')
boardman_east_B3_down = pd.read_csv('boardman_east_B3_down.csv')
boardman_east_B4_down = pd.read_csv('boardman_east_B4_down.csv')
boardman_east_B5_down = pd.read_csv('boardman_east_B5_down.csv')
boardman_east_B6_down = pd.read_csv('boardman_east_B6_down.csv')

boardman_east_B1_up = pd.read_csv('boardman_east_B1_up.csv')
boardman_east_B2_up = pd.read_csv('boardman_east_B2_up.csv')
boardman_east_B3_up = pd.read_csv('boardman_east_B3_up.csv')
boardman_east_B4_up = pd.read_csv('boardman_east_B4_up.csv')
boardman_east_B5_up = pd.read_csv('boardman_east_B5_up.csv')
boardman_east_B6_up = pd.read_csv('boardman_east_B6_up.csv')



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/boardman/downtime/")
def hello():
    B1 = boardman_east_B1_down.to_list()
    B2 = boardman_east_B2_down.to_list()
    B3 = boardman_east_B3_down.to_list()
    B4 = boardman_east_B4_down.to_list()
    B5 = boardman_east_B5_down.to_list()
    B6 = boardman_east_B6_down.to_list()

    return jsonify ({'B1': B1, 'B2': B2, 'B3': B3, 'B4': B4, 'B5': B5, 'B6': B6})

@app.route("/boardman/uptime/")
def hello():
    B1 = boardman_east_B1_up.to_list()
    B2 = boardman_east_B2_up.to_list()
    B3 = boardman_east_B3_up.to_list()
    B4 = boardman_east_B4_up.to_list()
    B5 = boardman_east_B5_up.to_list()
    B6 = boardman_east_B6_up.to_list()

    return jsonify ({'B1': B1, 'B2': B2, 'B3': B3, 'B4': B4, 'B5': B5, 'B6': B6})



if __name__ == '__main__':
    app.run(debug=True)
