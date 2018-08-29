from flask import Flask, jsonify, json
import pandas as pd

connell_L1_SE_down = pd.read_csv('connell_L1_SE_down.csv')
connell_L1_SF_down = pd.read_csv('connell_L1_SF_down.csv')
connell_L1_SG_down = pd.read_csv('connell_L1_SG_down.csv')
connell_L1_SH_down = pd.read_csv('connell_L1_SH_down.csv')
connell_L2_SA_down = pd.read_csv('connell_L2_SA_down.csv')
connell_L2_SB_down = pd.read_csv('connell_L2_SB_down.csv')
connell_L2_SC_down = pd.read_csv('connell_L2_SC_down.csv')
connell_L2_SD_down = pd.read_csv('connell_L2_SD_down.csv')

connell_L1_SE_up = pd.read_csv('connell_L1_SE_up.csv')
connell_L1_SF_up = pd.read_csv('connell_L1_SF_up.csv')
connell_L1_SG_up = pd.read_csv('connell_L1_SG_up.csv')
connell_L1_SH_up = pd.read_csv('connell_L1_SH_up.csv')
connell_L2_SA_up = pd.read_csv('connell_L2_SA_up.csv')
connell_L2_SB_up = pd.read_csv('connell_L2_SB_up.csv')
connell_L2_SC_up = pd.read_csv('connell_L2_SC_up.csv')
connell_L2_SD_up = pd.read_csv('connell_L2_SD_up.csv')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/connell/downtime/")
def hello():

    L1_SE = connell_L1_SE_down.to_list()
    L1_SF = connell_L1_SF_down.to_list()
    L1_SG = connell_L1_SG_down.to_list()
    L1_SH = connell_L1_SH_down.to_list()
    L2_SA = connell_L2_SA_down.to_list()
    L2_SB = connell_L2_SB_down.to_list()
    L2_SC = connell_L2_SC_down.to_list()
    L2_SD = connell_L2_SD_down.to_list()

    return jsonify ({'L1 SE': L1_SE, 'L1 SF': L1_SF, 'L1 SG': L1_SG, 'L1 SH': L1_SH, 'L2 SA': L2_SA, 'L2 SB': L2_SB, 'L2 SC': L2_SC, 'L2 SD': L2_SD})

@app.route("/connell/uptime/")
def hello():
    L1_SE = connell_L1_SE_up.to_list()
    L1_SF = connell_L1_SF_up.to_list()
    L1_SG = connell_L1_SG_up.to_list()
    L1_SH = connell_L1_SH_up.to_list()
    L2_SA = connell_L2_SA_up.to_list()
    L2_SB = connell_L2_SB_up.to_list()
    L2_SC = connell_L2_SC_up.to_list()
    L2_SD = connell_L2_SD_up.to_list()

    return jsonify ({'L1 SE': L1_SE, 'L1 SF': L1_SF, 'L1 SG': L1_SG, 'L1 SH': L1_SH, 'L2 SA': L2_SA, 'L2 SB': L2_SB, 'L2 SC': L2_SC, 'L2 SD': L2_SD})




if __name__ == '__main__':
    app.run(debug=True)
