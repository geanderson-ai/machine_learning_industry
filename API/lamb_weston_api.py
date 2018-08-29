DOWNTIMEDOWNTIMEfrom flask import Flask, jsonify, json
import pandas as pd
import pandas_redshift as pr

pr.connect_to_redshift(dbname = 'habladb',
                        host = 'habla-ai.csvoexx0fghm.us-west-2.redshift.amazonaws.com',
                        port = 5439,
                        user = 'root',
                        password = 'MAnchi89')


# MEAN UPTIME AND DOWNTIME ACROSS MULTIPLE PLANTS
LAMB_WESTON_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.lbw_mean_uptime t')
LAMB_WESTON_DOWNTIME = pr.redshift_to_pandas('SELECT t.* FROM public.lbw_mean_downtime t')


# PASCO UPTIME BY DAY BY LINE
PASCO_L1_S6_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s6_up_groupby t')
PASCO_L1_S7_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s7_up_groupby t')
PASCO_L1_S8_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s8_up_groupby t')
PASCO_L1_S9_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s9_up_groupby t')
PASCO_L1_S10_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l1_s10_up_groupby t')
PASCO_L2_S1_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s1_up t')
PASCO_L2_S2_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s2_up t')
PASCO_L2_S3_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s3_up t')
PASCO_L2_S4_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s4_up t')
PASCO_L2_S5_UPTIME = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_l2_s5_up t')

# PASCO REASON LEVEL 1
PASCO_L1_S6_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l1s6 t')
PASCO_L1_S7_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l1s7 t')
PASCO_L1_S8_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l1s8 t')
PASCO_L1_S9_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l1s t')
PASCO_L1_S10_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l1s10 t')
PASCO_L2_S1_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l2s1 t')
PASCO_L2_S2_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l2s2 t')
PASCO_L2_S3_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l2s3 t')
PASCO_L2_S4_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l2s4 t')
PASCO_L2_S5_RLVL1 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv1_l2s5 t')

# PASCO REASON LEVEL 2
PASCO_L1_S6_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l1s6 t')
PASCO_L1_S7_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l1s7 t')
PASCO_L1_S8_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l1s8 t')
PASCO_L1_S9_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l1s t')
PASCO_L1_S10_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l1s10 t')
PASCO_L2_S1_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l2s1 t')
PASCO_L2_S2_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l2s2 t')
PASCO_L2_S3_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l2s3 t')
PASCO_L2_S4_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l2s4 t')
PASCO_L2_S5_RLVL2 = pr.redshift_to_pandas('SELECT t.* FROM public.pasco_rlv2_l2s5 t')



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pasco/uptime/")
def pasco_uptime():
    L1_S6_date = PASCO_L1_S6_UPTIME.iloc[:, 0].tolist()
    L1_S6 = PASCO_L1_S6_UPTIME.iloc[:, 1].tolist()
    L1_S7_date = PASCO_L1_S7_UPTIME.iloc[:, 0].tolist()
    L1_S7 = PASCO_L1_S7_UPTIME.iloc[:, 1].tolist()
    L1_S8_date = PASCO_L1_S8_UPTIME.iloc[:, 0].tolist()
    L1_S8 = PASCO_L1_S8_UPTIME.iloc[:, 1].tolist()
    L1_S9_date = PASCO_L1_S9_UPTIME.iloc[:, 0].tolist()
    L1_S9 = PASCO_L1_S9_UPTIME.iloc[:, 1].tolist()
    L1_S10_date = PASCO_L1_S10_UPTIME.iloc[:, 0].tolist()
    L1_S10 = PASCO_L1_S10_UPTIME.iloc[:, 1].tolist()
    L2_S1_date = PASCO_L2_S1_UPTIME.iloc[:, 0].tolist()
    L2_S1 = PASCO_L2_S1_UPTIME.iloc[:, 1].tolist()
    L2_S2_date = PASCO_L2_S1_UPTIME.iloc[:, 0].tolist()
    L2_S2 = PASCO_L2_S1_UPTIME.iloc[:, 1].tolist()
    L2_S3_date = PASCO_L2_S1_UPTIME.iloc[:, 0].tolist()
    L2_S3 = PASCO_L2_S1_UPTIME.iloc[:, 1].tolist()
    L2_S4_date = PASCO_L2_S1_UPTIME.iloc[:, 0].tolist()
    L2_S4 = PASCO_L2_S1_UPTIME.iloc[:, 1].tolist()
    L2_S5_date = PASCO_L2_S1_UPTIME.iloc[:, 0].tolist()
    L2_S5 = PASCO_L2_S1_UPTIME.iloc[:, 1].tolist()
    return jsonify({'Pasco Uptime': {'Pasco L1 S6 Date': L1_S6_date, 'Pasco L1 S6 Uptime': L1_S6, 'Pasco L1 S7 Date': L1_S7_date, 'Pasco L1 S7 Uptime': L1_S7,
    'Pasco L1 S8 Date': L1_S8_date, 'Pasco L1 S8 Uptime': L1_S8, 'Pasco L1 S9 Date': L1_S9_date, 'Pasco L1 S9 Uptime': L1_S9,
    'Pasco L1 S10 Date': L1_S10_date, 'Pasco L1 S10 Uptime': L1_S10, 'Pasco L2 S1 Date': L2_S1_date, 'Pasco L2 S1 Uptime': L2_S1,
    'Pasco L2 S2 Date': L2_S2_date, 'Pasco L2 S2 Uptime': L2_S2, 'Pasco L2 S3 Date': L2_S3_date, 'Pasco L2 S3 Uptime': L2_S3,
    'Pasco L2 S4 Date': L2_S4_date, 'Pasco L2 S4 Uptime': L2_S4, 'Pasco L2 S5 Date': L2_S5_date, 'Pasco L2 S5 Uptime': L2_S5,}})

@app.route("/lambweston/uptime/")
def lbw_uptime():
    month = LAMB_WESTON_UPTIME.iloc[:, 0].tolist()
    american_falls = LAMB_WESTON_UPTIME.iloc[:, 1].tolist()
    boardman = LAMB_WESTON_UPTIME.iloc[:, 2].tolist()
    connell = LAMB_WESTON_UPTIME.iloc[:, 3].tolist()
    delhi = LAMB_WESTON_UPTIME.iloc[:, 4].tolist()
    park_rapids = LAMB_WESTON_UPTIME.iloc[:, 5].tolist()
    pasco = LAMB_WESTON_UPTIME.iloc[:, 6].tolist()
    richland = LAMB_WESTON_UPTIME.iloc[:, 7].tolist()
    return jsonify({'Lamb Weston Uptime': {'Month': month, 'American Falls': american_falls, 'Boardman': boardman, 'Connell': connell, 'Delhi': delhi,
    'Park Rapids': park_rapids, 'Pasco': pasco, 'Richland': richland}})

@app.route("/lambweston/downtime/")
def lbw_downtime():
    month = LAMB_WESTON_DOWNTIME.iloc[:, 0].tolist()
    american_falls = LAMB_WESTON_DOWNTIME.iloc[:, 1].tolist()
    boardman = LAMB_WESTON_DOWNTIME.iloc[:, 2].tolist()
    connell = LAMB_WESTON_DOWNTIME.iloc[:, 3].tolist()
    delhi = LAMB_WESTON_DOWNTIME.iloc[:, 4].tolist()
    park_rapids = LAMB_WESTON_DOWNTIME.iloc[:, 5].tolist()
    pasco = LAMB_WESTON_DOWNTIME.iloc[:, 6].tolist()
    richland = LAMB_WESTON_DOWNTIME.iloc[:, 7].tolist()
    return jsonify({'Lamb Weston Uptime': {'Month': month, 'American Falls': american_falls, 'Boardman': boardman, 'Connell': connell, 'Delhi': delhi,
    'Park Rapids': park_rapids, 'Pasco': pasco, 'Richland': richland}})

@app.route("/lambweston/pasco/level1/")
def pasco_lvl1():
    L1_S6_A = PASCO_L1_S6_RLVL1.iloc[:, 0].tolist()
    L1_S6_B = PASCO_L1_S6_RLVL1.iloc[:, 1].tolist()
    L1_S6_C = PASCO_L1_S6_RLVL1.iloc[:, 2].tolist()

    L1_S7_A = PASCO_L1_S7_RLVL1.iloc[:, 0].tolist()
    L1_S7_B = PASCO_L1_S7_RLVL1.iloc[:, 1].tolist()
    L1_S7_C = PASCO_L1_S7_RLVL1.iloc[:, 2].tolist()

    L1_S8_A = PASCO_L1_S8_RLVL1.iloc[:, 0].tolist()
    L1_S8_B = PASCO_L1_S8_RLVL1.iloc[:, 1].tolist()
    L1_S8_C = PASCO_L1_S8_RLVL1.iloc[:, 2].tolist()

    L1_S9_A = PASCO_L1_S9_RLVL1.iloc[:, 0].tolist()
    L1_S9_B = PASCO_L1_S9_RLVL1.iloc[:, 1].tolist()
    L1_S9_C = PASCO_L1_S9_RLVL1.iloc[:, 2].tolist()

    L1_S10_A = PASCO_L1_S10_RLVL1.iloc[:, 0].tolist()
    L1_S10_B = PASCO_L1_S10_RLVL1.iloc[:, 1].tolist()
    L1_S10_C = PASCO_L1_S10_RLVL1.iloc[:, 2].tolist()

    L2_S1_A = PASCO_L2_S1_RLVL1.iloc[:, 0].tolist()
    L2_S1_B = PASCO_L2_S1_RLVL1.iloc[:, 1].tolist()
    L2_S1_C = PASCO_L2_S1_RLVL1.iloc[:, 2].tolist()

    L2_S2_A = PASCO_L2_S2_RLVL1.iloc[:, 0].tolist()
    L2_S2_B = PASCO_L2_S2_RLVL1.iloc[:, 1].tolist()
    L2_S2_C = PASCO_L2_S2_RLVL1.iloc[:, 1].tolist()

    L2_S3_A = PASCO_L2_S3_RLVL1.iloc[:, 0].tolist()
    L2_S3_B = PASCO_L2_S3_RLVL1.iloc[:, 1].tolist()
    L2_S3_C = PASCO_L2_S3_RLVL1.iloc[:, 2].tolist()

    L2_S4_A = PASCO_L2_S4_RLVL1.iloc[:, 0].tolist()
    L2_S4_B = PASCO_L2_S4_RLVL1.iloc[:, 1].tolist()
    L2_S4_C = PASCO_L2_S4_RLVL1.iloc[:, 2].tolist()

    L2_S5_A = PASCO_L2_S5_RLVL1.iloc[:, 0].tolist()
    L2_S5_B = PASCO_L2_S5_RLVL1.iloc[:, 2].tolist()
    L2_S5_C = PASCO_L2_S5_RLVL1.iloc[:, 2].tolist()
    return jsonify({'Lamb Weston Reason Level 1': {'L1_S6': {'Date': L1_S6_A, 'Reason Lvl1': L1_S6_B, 'Quantity': L1_S6_C}},
    {'L1_S7': {'Date': L1_S7_A, 'Reason Lvl1': L1_S7_B, 'Quantity': L1_S7_C}}, {'L1_S8': {'Date': L1_S8_A, 'Reason Lvl1': L1_S8_B, 'Quantity': L1_S8_C}},
    {'L1_S9': {'Date': L1_S9_A, 'Reason Lvl1': L1_S9_B, 'Quantity': L1_S9_C}}, {'L1_S10': {'Date': L1_S10_A, 'Reason Lvl1': L1_S10_B, 'Quantity': L1_S10_C}},
    {'L2_S1': {'Date': L2_S1_A, 'Reason Lvl1': L2_S1_B, 'Quantity': L2_S1_C}}, {'L2_S2': {'Date': L2_S2_A, 'Reason Lvl1': L1_S2_B, 'Quantity': L1_S2_C}},
    {'L2_S3': {'Date': L2_S3_A, 'Reason Lvl1': L2_S3_B, 'Quantity': L2_S3_C}}, {'L2_S4': {'Date': L2_S4_A, 'Reason Lvl1': L1_S4_B, 'Quantity': L1_S4_C}},
    {'L2_S5': {'Date': L2_S5_A, 'Reason Lvl1': L1_S5_B, 'Quantity': L1_S5_C}}})

@app.route("/lambweston/pasco/level2/")
def pasco_lvl2():
    L1_S6_A = PASCO_L1_S6_RLVL2.iloc[:, 0].tolist()
    L1_S6_B = PASCO_L1_S6_RLVL2.iloc[:, 1].tolist()
    L1_S6_C = PASCO_L1_S6_RLVL2.iloc[:, 2].tolist()

    L1_S7_A = PASCO_L1_S7_RLVL2.iloc[:, 0].tolist()
    L1_S7_B = PASCO_L1_S7_RLVL2.iloc[:, 1].tolist()
    L1_S7_C = PASCO_L1_S7_RLVL2.iloc[:, 2].tolist()

    L1_S8_A = PASCO_L1_S8_RLVL2.iloc[:, 0].tolist()
    L1_S8_B = PASCO_L1_S8_RLVL2.iloc[:, 1].tolist()
    L1_S8_C = PASCO_L1_S8_RLVL2.iloc[:, 2].tolist()

    L1_S9_A = PASCO_L1_S9_RLVL2.iloc[:, 0].tolist()
    L1_S9_B = PASCO_L1_S9_RLVL2.iloc[:, 1].tolist()
    L1_S9_C = PASCO_L1_S9_RLVL2.iloc[:, 2].tolist()

    L1_S10_A = PASCO_L1_S10_RLVL2.iloc[:, 0].tolist()
    L1_S10_B = PASCO_L1_S10_RLVL2.iloc[:, 1].tolist()
    L1_S10_C = PASCO_L1_S10_RLVL2.iloc[:, 2].tolist()

    L2_S1_A = PASCO_L2_S1_RLVL2.iloc[:, 0].tolist()
    L2_S1_B = PASCO_L2_S1_RLVL2.iloc[:, 1].tolist()
    L2_S1_C = PASCO_L2_S1_RLVL2.iloc[:, 2].tolist()

    L2_S2_A = PASCO_L2_S2_RLVL2.iloc[:, 0].tolist()
    L2_S2_B = PASCO_L2_S2_RLVL2.iloc[:, 1].tolist()
    L2_S2_C = PASCO_L2_S2_RLVL2.iloc[:, 1].tolist()

    L2_S3_A = PASCO_L2_S3_RLVL2.iloc[:, 0].tolist()
    L2_S3_B = PASCO_L2_S3_RLVL2.iloc[:, 1].tolist()
    L2_S3_C = PASCO_L2_S3_RLVL2.iloc[:, 2].tolist()

    L2_S4_A = PASCO_L2_S4_RLVL2.iloc[:, 0].tolist()
    L2_S4_B = PASCO_L2_S4_RLVL2.iloc[:, 1].tolist()
    L2_S4_C = PASCO_L2_S4_RLVL2.iloc[:, 2].tolist()

    L2_S5_A = PASCO_L2_S5_RLVL2.iloc[:, 0].tolist()
    L2_S5_B = PASCO_L2_S5_RLVL2.iloc[:, 2].tolist()
    L2_S5_C = PASCO_L2_S5_RLVL2.iloc[:, 2].tolist()
    return jsonify({'Lamb Weston Reason Level 1': {'L1_S6': {'Date': L1_S6_A, 'Reason Lvl2': L1_S6_B, 'Quantity': L1_S6_C}},
    {'L1_S7': {'Date': L1_S7_A, 'Reason Lvl2': L1_S7_B, 'Quantity': L1_S7_C}}, {'L1_S8': {'Date': L1_S8_A, 'Reason Lvl2': L1_S8_B, 'Quantity': L1_S8_C}},
    {'L1_S9': {'Date': L1_S9_A, 'Reason Lvl2': L1_S9_B, 'Quantity': L1_S9_C}}, {'L1_S10': {'Date': L1_S10_A, 'Reason Lvl2': L1_S10_B, 'Quantity': L1_S10_C}},
    {'L2_S1': {'Date': L2_S1_A, 'Reason Lvl2': L2_S1_B, 'Quantity': L2_S1_C}}, {'L2_S2': {'Date': L2_S2_A, 'Reason Lvl2': L1_S2_B, 'Quantity': L1_S2_C}},
    {'L2_S3': {'Date': L2_S3_A, 'Reason Lvl2': L2_S3_B, 'Quantity': L2_S3_C}}, {'L2_S4': {'Date': L2_S4_A, 'Reason Lvl2': L1_S4_B, 'Quantity': L1_S4_C}},
    {'L2_S5': {'Date': L2_S5_A, 'Reason Lvl2': L1_S5_B, 'Quantity': L1_S5_C}}})


app.run(debug=True)
