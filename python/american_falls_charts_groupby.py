from flask import Flask, jsonify, json
import pandas as pd

american_falls_L10_S1_down_groupby = pd.read_csv('american_falls_L10_S1_down_groupby.csv')
american_falls_L10_S2_down_groupby = pd.read_csv('american_falls_L10_S2_down_groupby.csv')
american_falls_L10_S3_down_groupby = pd.read_csv('american_falls_L10_S3_down_groupby.csv')
american_falls_L10_S4_down_groupby = pd.read_csv('american_falls_L10_S4_down_groupby.csv')
american_falls_L10_S5_down_groupby = pd.read_csv('american_falls_L10_S5_down_groupby.csv')
american_falls_L20_S2_down_groupby = pd.read_csv('american_falls_L20_S2_down_groupby.csv')
american_falls_L20_S3_down_groupby = pd.read_csv('american_falls_L20_S3_down_groupby.csv')
american_falls_L20_S4_down_groupby = pd.read_csv('american_falls_L20_S4_down_groupby.csv')

american_falls_L10_S1_up_groupby = pd.read_csv('american_falls_L10_S1_up_groupby.csv')
american_falls_L10_S2_up_groupby = pd.read_csv('american_falls_L10_S2_up_groupby.csv')
american_falls_L10_S3_up_groupby = pd.read_csv('american_falls_L10_S3_up_groupby.csv')
american_falls_L10_S4_up_groupby = pd.read_csv('american_falls_L10_S4_up_groupby.csv')
american_falls_L10_S5_up_groupby = pd.read_csv('american_falls_L10_S5_up_groupby.csv')
american_falls_L20_S2_up_groupby = pd.read_csv('american_falls_L20_S2_up_groupby.csv')
american_falls_L20_S3_up_groupby = pd.read_csv('american_falls_L20_S3_up_groupby.csv')
american_falls_L20_S4_up_groupby = pd.read_csv('american_falls_L20_S4_up_groupby.csv')


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/american_falls/downtime/groupby")
def hello():

    L10_S1 = american_falls_L10_S1_down_groupby.to_list()
    L10_S2 = american_falls_L10_S2_down_groupby.to_list()
    L10_S3 = american_falls_L10_S3_down_groupby.to_list()
    L10_S4 = american_falls_L10_S4_down_groupby.to_list()
    L10_S5 = american_falls_L10_S5_down_groupby.to_list()
    L20_S2 = american_falls_L20_S2_down_groupby.to_list()
    L20_S3 = american_falls_L20_S3_down_groupby.to_list()
    L20_S4 = american_falls_L20_S4_down_groupby.to_list()


    return jsonify ({'L10 S1': L10_S1, 'L10 S2': L10_S2, 'L10 S3': L10_S3, 'L10 S4': L10_S4, 'L10 S5': L10_S5, 'L20 S2': L20_S2, 'L20 S3': L20_S3, 'L20 S4': L20_S4})

@app.route("/american_falls/uptime/groupby")
def hello():

    L10_S1 = american_falls_L10_S1_up_groupby.to_list()
    L10_S2 = american_falls_L10_S2_up_groupby.to_list()
    L10_S3 = american_falls_L10_S3_up_groupby.to_list()
    L10_S4 = american_falls_L10_S4_up_groupby.to_list()
    L10_S5 = american_falls_L10_S5_up_groupby.to_list()
    L20_S2 = american_falls_L20_S2_up_groupby.to_list()
    L20_S3 = american_falls_L20_S3_up_groupby.to_list()
    L20_S4 = american_falls_L20_S4_up_groupby.to_list()

    
    return jsonify ({'L10 S1': L10_S1, 'L10 S2': L10_S2, 'L10 S3': L10_S3, 'L10 S4': L10_S4, 'L10 S5': L10_S5, 'L20 S2': L20_S2, 'L20 S3': L20_S3, 'L20 S4': L20_S4})




if __name__ == '__main__':
    app.run(debug=True)
