from flask import Flask, jsonify, json
import pandas as pd

connell_L1_SE_down_groupby = pd.read_csv('connell_L1_SE_down_groupby.csv')
connell_L1_SF_down_groupby = pd.read_csv('connell_L1_SF_down_groupby.csv')
connell_L1_SG_down_groupby = pd.read_csv('connell_L1_SG_down_groupby.csv')
connell_L1_SH_down_groupby = pd.read_csv('connell_L1_SH_down_groupby.csv')
connell_L2_SA_down_groupby = pd.read_csv('connell_L2_SA_down_groupby.csv')
connell_L2_SB_down_groupby = pd.read_csv('connell_L2_SB_down_groupby.csv')
connell_L2_SC_down_groupby = pd.read_csv('connell_L2_SC_down_groupby.csv')
connell_L2_SD_down_groupby = pd.read_csv('connell_L2_SD_down_groupby.csv')

connell_L1_SE_up_groupby = pd.read_csv('connell_L1_SE_up_groupby.csv')
connell_L1_SF_up_groupby = pd.read_csv('connell_L1_SF_up_groupby.csv')
connell_L1_SG_up_groupby = pd.read_csv('connell_L1_SG_up_groupby.csv')
connell_L1_SH_up_groupby = pd.read_csv('connell_L1_SH_up_groupby.csv')
connell_L2_SA_up_groupby = pd.read_csv('connell_L2_SA_up_groupby.csv')
connell_L2_SB_up_groupby = pd.read_csv('connell_L2_SB_up_groupby.csv')
connell_L2_SC_up_groupby = pd.read_csv('connell_L2_SC_up_groupby.csv')
connell_L2_SD_up_groupby = pd.read_csv('connell_L2_SD_up_groupby.csv')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/connell/downtime/groupby")
def hello():

    L1_SE = connell_L1_SE_down_groupby.to_list()
    L1_SF = connell_L1_SF_down_groupby.to_list()
    L1_SG = connell_L1_SG_down_groupby.to_list()
    L1_SH = connell_L1_SH_down_groupby.to_list()
    L2_SA = connell_L2_SA_down_groupby.to_list()
    L2_SB = connell_L2_SB_down_groupby.to_list()
    L2_SC = connell_L2_SC_down_groupby.to_list()
    L2_SD = connell_L2_SD_down_groupby.to_list()

    return jsonify ({'L1 SE': L1_SE, 'L1 SF': L1_SF, 'L1 SG': L1_SG, 'L1 SH': L1_SH, 'L2 SA': L2_SA, 'L2 SB': L2_SB, 'L2 SC': L2_SC, 'L2 SD': L2_SD})

@app.route("/connell/uptime/groupby")
def hello():
    L1_SE = connell_L1_SE_up_groupby.to_list()
    L1_SF = connell_L1_SF_up_groupby.to_list()
    L1_SG = connell_L1_SG_up_groupby.to_list()
    L1_SH = connell_L1_SH_up_groupby.to_list()
    L2_SA = connell_L2_SA_up_groupby.to_list()
    L2_SB = connell_L2_SB_up_groupby.to_list()
    L2_SC = connell_L2_SC_up_groupby.to_list()
    L2_SD = connell_L2_SD_up_groupby.to_list()

    return jsonify ({'L1 SE': L1_SE, 'L1 SF': L1_SF, 'L1 SG': L1_SG, 'L1 SH': L1_SH, 'L2 SA': L2_SA, 'L2 SB': L2_SB, 'L2 SC': L2_SC, 'L2 SD': L2_SD})




if __name__ == '__main__':
    app.run(debug=True)
