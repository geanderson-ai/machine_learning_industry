from flask import Flask, jsonify, json
import pandas as pd
import pandas_redshift as pr

pr.connect_to_redshift(dbname = 'habladb',
                        host = 'habla-ai.csvoexx0fghm.us-west-2.redshift.amazonaws.com',
                        port = 5439,
                        user = 'root',
                        password = 'MAnchi89')

pasco_L1_S6_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s6_down_groupby t')
pasco_L1_S6_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s6_up_groupby t')
pasco_L1_S7_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s7_down_groupby t')
pasco_L1_S7_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s7_up_groupby t')
pasco_L1_S8_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s8_down_groupby t')
pasco_L1_S8_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s8_up_groupby t')
pasco_L1_S9_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s9_down_groupby t')
pasco_L1_S9_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s9_up_groupby t')
pasco_L1_S10_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s10_down_groupby t')
pasco_L1_S10_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s10_up_groupby t')
pasco_L2_S1_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s1_down_groupby t')
pasco_L2_S1_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s1_up_groupby t')
pasco_L2_S2_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s2_down_groupby t')
pasco_L2_S2_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s2_up_groupby t')
pasco_L2_S3_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s3_down_groupby t')
pasco_L2_S3_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s3_up_groupby t')
pasco_L2_S4_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s4_down_groupby t')
pasco_L2_S4_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s4_up_groupby t')
pasco_L2_S5_down = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s5_down_groupby t')
pasco_L2_S5_up = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s5_up_groupby t')





app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pasco/downtime_groupby/")
def downtime():
    L1_S6 = pasco_L1_S6_down_groupby.to_list()
    L1_S7 = pasco_L1_S7_down_groupby.to_list()
    L1_S8 = pasco_L1_S8_down_groupby.to_list()
    L1_S9 = pasco_L1_S9_down_groupby.to_list()
    L1_S10 = pasco_L1_S10_down_groupby.to_list()
    L2_S1 = pasco_L2_S1_down_groupby.to_list()
    L2_S2 = pasco_L2_S2_down_groupby.to_list()
    L2_S3 = pasco_L2_S3_down_groupby.to_list()
    L2_S4 = pasco_L2_S4_down_groupby.to_list()
    L2_S5 = pasco_L2_S5_down_groupby.to_list()
    return jsonify ({'L1 S6': L1_S6, 'L1 S7': L1_S7, 'L1 S8': L1_S8, 'L1 S9': L1_S9, 'L1 S10': L1_S10, 'L2 S1': L2_S1, 'L2 S2': L2_S2, 'L2 S3': L2_S3, 'LS S4': LS_S4, 'L2 S5': L2_S5})

@app.route("/pasco/uptime_groupby/")
def uptime():
    L1_S6 = pasco_L1_S6_up_groupby.to_list()
    L1_S7 = pasco_L1_S7_up_groupby.to_list()
    L1_S8 = pasco_L1_S8_up_groupby.to_list()
    L1_S9 = pasco_L1_S9_up_groupby.to_list()
    L1_S10 = pasco_L1_S10_up_groupby.to_list()
    L2_S1 = pasco_L2_S1_up_groupby.to_list()
    L2_S2 = pasco_L2_S2_up_groupby.to_list()
    L2_S3 = pasco_L2_S3_up_groupby.to_list()
    L2_S4 = pasco_L2_S4_up_groupby.to_list()
    L2_S5 = pasco_L2_S5_up_groupby.to_list()
return jsonify ({'L1 S6': L1_S6, 'L1 S7': L1_S7, 'L1 S8': L1_S8, 'L1 S9': L1_S9, 'L1 S10': L1_S10, 'L2 S1': L2_S1, 'L2 S2': L2_S2, 'L2 S3': L2_S3, 'LS S4': LS_S4, 'L2 S5': L2_S5})
