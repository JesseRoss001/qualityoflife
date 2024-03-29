import os
import django
import pandas as pd
from io import StringIO
from my_project.models import CountryData

# Adjust this to the actual path of your Django project's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qualityoflife.settings')
django.setup()

def populate_database():
    try:
        csv_data_1 = """ 
        Overall rank,Country or region,Score,GDP per capita,Social support,Healthy life expectancy,Freedom to make life choices,Generosity,Perceptions of corruption
        1,Finland,7.769,1.340,1.587,0.986,0.596,0.153,0.393
        2,Denmark,7.600,1.383,1.573,0.996,0.592,0.252,0.410
        3,Norway,7.554,1.488,1.582,1.028,0.603,0.271,0.341
        4,Iceland,7.494,1.380,1.624,1.026,0.591,0.354,0.118
        5,Netherlands,7.488,1.396,1.522,0.999,0.557,0.322,0.298
        6,Switzerland,7.480,1.452,1.526,1.052,0.572,0.263,0.343
        7,Sweden,7.343,1.387,1.487,1.009,0.574,0.267,0.373
        8,New Zealand,7.307,1.303,1.557,1.026,0.585,0.330,0.380
        9,Canada,7.278,1.365,1.505,1.039,0.584,0.285,0.308
        10,Austria,7.246,1.376,1.475,1.016,0.532,0.244,0.226
        11,Australia,7.228,1.372,1.548,1.036,0.557,0.332,0.290
        12,Costa Rica,7.167,1.034,1.441,0.963,0.558,0.144,0.093
        13,Israel,7.139,1.276,1.455,1.029,0.371,0.261,0.082
        14,Luxembourg,7.090,1.609,1.479,1.012,0.526,0.194,0.316
        15,United Kingdom,7.054,1.333,1.538,0.996,0.450,0.348,0.278
        16,Ireland,7.021,1.499,1.553,0.999,0.516,0.298,0.310
        17,Germany,6.985,1.373,1.454,0.987,0.495,0.261,0.265
        18,Belgium,6.923,1.356,1.504,0.986,0.473,0.160,0.210
        19,United States,6.892,1.433,1.457,0.874,0.454,0.280,0.128
        20,Czech Republic,6.852,1.269,1.487,0.920,0.457,0.046,0.036
        21,United Arab Emirates,6.825,1.503,1.310,0.825,0.598,0.262,0.182
        22,Malta,6.726,1.300,1.520,0.999,0.564,0.375,0.151
        23,Mexico,6.595,1.070,1.323,0.861,0.433,0.074,0.073
        24,France,6.592,1.324,1.472,1.045,0.436,0.111,0.183
        25,Taiwan,6.446,1.368,1.430,0.914,0.351,0.242,0.097
        26,Chile,6.444,1.159,1.369,0.920,0.357,0.187,0.056
        27,Guatemala,6.436,0.800,1.269,0.746,0.535,0.175,0.078
        28,Saudi Arabia,6.375,1.403,1.357,0.795,0.439,0.080,0.132
        29,Qatar,6.374,1.684,1.313,0.871,0.555,0.220,0.167
        30,Spain,6.354,1.286,1.484,1.062,0.362,0.153,0.079
        31,Panama,6.321,1.149,1.442,0.910,0.516,0.109,0.054
        32,Brazil,6.300,1.004,1.439,0.802,0.390,0.099,0.086
        33,Uruguay,6.293,1.124,1.465,0.891,0.523,0.127,0.150
        34,Singapore,6.262,1.572,1.463,1.141,0.556,0.271,0.453
        35,El Salvador,6.253,0.794,1.242,0.789,0.430,0.093,0.074
        36,Italy,6.223,1.294,1.488,1.039,0.231,0.158,0.030
        37,Bahrain,6.199,1.362,1.368,0.871,0.536,0.255,0.110
        38,Slovakia,6.198,1.246,1.504,0.881,0.334,0.121,0.014
        39,Trinidad & Tobago,6.192,1.231,1.477,0.713,0.489,0.185,0.016
        40,Poland,6.182,1.206,1.438,0.884,0.483,0.117,0.050
        41,Uzbekistan,6.174,0.745,1.529,0.756,0.631,0.322,0.240
        42,Lithuania,6.149,1.238,1.515,0.818,0.291,0.043,0.042
        43,Colombia,6.125,0.985,1.410,0.841,0.470,0.099,0.034
        44,Slovenia,6.118,1.258,1.523,0.953,0.564,0.144,0.057
        45,Nicaragua,6.105,0.694,1.325,0.835,0.435,0.200,0.127
        46,Kosovo,6.100,0.882,1.232,0.758,0.489,0.262,0.006
        47,Argentina,6.086,1.092,1.432,0.881,0.471,0.066,0.050
        48,Romania,6.070,1.162,1.232,0.825,0.462,0.083,0.005
        49,Cyprus,6.046,1.263,1.223,1.042,0.406,0.190,0.041
        50,Ecuador,6.028,0.912,1.312,0.868,0.498,0.126,0.087
        51,Kuwait,6.021,1.500,1.319,0.808,0.493,0.142,0.097
        52,Thailand,6.008,1.050,1.409,0.828,0.557,0.359,0.028
        53,Latvia,5.940,1.187,1.465,0.812,0.264,0.075,0.064
        54,South Korea,5.895,1.301,1.219,1.036,0.159,0.175,0.056
        55,Estonia,5.893,1.237,1.528,0.874,0.495,0.103,0.161
        56,Jamaica,5.890,0.831,1.478,0.831,0.490,0.107,0.028
        57,Mauritius,5.888,1.120,1.402,0.798,0.498,0.215,0.060
        58,Japan,5.886,1.327,1.419,1.088,0.445,0.069,0.140
        59,Honduras,5.860,0.642,1.236,0.828,0.507,0.246,0.078
        60,Kazakhstan,5.809,1.173,1.508,0.729,0.410,0.146,0.096
        61,Bolivia,5.779,0.776,1.209,0.706,0.511,0.137,0.064
        62,Hungary,5.758,1.201,1.410,0.828,0.199,0.081,0.020
        63,Paraguay,5.743,0.855,1.475,0.777,0.514,0.184,0.080
        64,Northern Cyprus,5.718,1.263,1.252,1.042,0.417,0.191,0.162
        65,Peru,5.697,0.960,1.274,0.854,0.455,0.083,0.027
        66,Portugal,5.693,1.221,1.431,0.999,0.508,0.047,0.025
        67,Pakistan,5.653,0.677,0.886,0.535,0.313,0.220,0.098
        68,Russia,5.648,1.183,1.452,0.726,0.334,0.082,0.031
        69,Philippines,5.631,0.807,1.293,0.657,0.558,0.117,0.107
        70,Serbia,5.603,1.004,1.383,0.854,0.282,0.137,0.039
        71,Moldova,5.529,0.685,1.328,0.739,0.245,0.181,0.000
        72,Libya,5.525,1.044,1.303,0.673,0.416,0.133,0.152
        73,Montenegro,5.523,1.051,1.361,0.871,0.197,0.142,0.080
        74,Tajikistan,5.467,0.493,1.098,0.718,0.389,0.230,0.144
        75,Croatia,5.432,1.155,1.266,0.914,0.296,0.119,0.022
        76,Hong Kong,5.430,1.438,1.277,1.122,0.440,0.258,0.287
        77,Dominican Republic,5.425,1.015,1.401,0.779,0.497,0.113,0.101
        78,Bosnia and Herzegovina,5.386,0.945,1.212,0.845,0.212,0.263,0.006
        79,Turkey,5.373,1.183,1.360,0.808,0.195,0.083,0.106
        80,Malaysia,5.339,1.221,1.171,0.828,0.508,0.260,0.024
        81,Belarus,5.323,1.067,1.465,0.789,0.235,0.094,0.142
        82,Greece,5.287,1.181,1.156,0.999,0.067,0.000,0.034
        83,Mongolia,5.285,0.948,1.531,0.667,0.317,0.235,0.038
        84,North Macedonia,5.274,0.983,1.294,0.838,0.345,0.185,0.034
        85,Nigeria,5.265,0.696,1.111,0.245,0.426,0.215,0.041
        86,Kyrgyzstan,5.261,0.551,1.438,0.723,0.508,0.300,0.023
        87,Turkmenistan,5.247,1.052,1.538,0.657,0.394,0.244,0.028
        88,Algeria,5.211,1.002,1.160,0.785,0.086,0.073,0.114
        89,Morocco,5.208,0.801,0.782,0.782,0.418,0.036,0.076
        90,Azerbaijan,5.208,1.043,1.147,0.769,0.351,0.035,0.182
        91,Lebanon,5.197,0.987,1.224,0.815,0.216,0.166,0.027
        92,Indonesia,5.192,0.931,1.203,0.660,0.491,0.498,0.028
        93,China,5.191,1.029,1.125,0.893,0.521,0.058,0.100
        94,Vietnam,5.175,0.741,1.346,0.851,0.543,0.147,0.073
        95,Bhutan,5.082,0.813,1.321,0.604,0.457,0.370,0.167
        96,Cameroon,5.044,0.549,0.910,0.331,0.381,0.187,0.037
        97,Bulgaria,5.011,1.092,1.513,0.815,0.311,0.081,0.004
        98,Ghana,4.996,0.611,0.868,0.486,0.381,0.245,0.040
        99,Ivory Coast,4.944,0.569,0.808,0.232,0.352,0.154,0.090
        100,Nepal,4.913,0.446,1.226,0.677,0.439,0.285,0.089
        101,Jordan,4.906,0.837,1.225,0.815,0.383,0.110,0.130
        102,Benin,4.883,0.393,0.437,0.397,0.349,0.175,0.082
        103,Congo (Brazzaville),4.812,0.673,0.799,0.508,0.372,0.105,0.093
        104,Gabon,4.799,1.057,1.183,0.571,0.295,0.043,0.055
        105,Laos,4.796,0.764,1.030,0.551,0.547,0.266,0.164
        106,South Africa,4.722,0.960,1.351,0.469,0.389,0.130,0.055
        107,Albania,4.719,0.947,0.848,0.874,0.383,0.178,0.027
        108,Venezuela,4.707,0.960,1.427,0.805,0.154,0.064,0.047
        109,Cambodia,4.700,0.574,1.122,0.637,0.609,0.232,0.062
        110,Palestinian Territories,4.696,0.657,1.247,0.672,0.225,0.103,0.066
        111,Senegal,4.681,0.450,1.134,0.571,0.292,0.153,0.072
        112,Somalia,4.668,0.000,0.698,0.268,0.559,0.243,0.270
        113,Namibia,4.639,0.879,1.313,0.477,0.401,0.070,0.056
        114,Niger,4.628,0.138,0.774,0.366,0.318,0.188,0.102
        115,Burkina Faso,4.587,0.331,1.056,0.380,0.255,0.177,0.113
        116,Armenia,4.559,0.850,1.055,0.815,0.283,0.095,0.064
        117,Iran,4.548,1.100,0.842,0.785,0.305,0.270,0.125
        118,Guinea,4.534,0.380,0.829,0.375,0.332,0.207,0.086
        119,Georgia,4.519,0.886,0.666,0.752,0.346,0.043,0.164
        120,Gambia,4.516,0.308,0.939,0.428,0.382,0.269,0.167
        121,Kenya,4.509,0.512,0.983,0.581,0.431,0.372,0.053
        122,Mauritania,4.490,0.570,1.167,0.489,0.066,0.106,0.088
        123,Mozambique,4.466,0.204,0.986,0.390,0.494,0.197,0.138
        124,Tunisia,4.461,0.921,1.000,0.815,0.167,0.059,0.055
        125,Bangladesh,4.456,0.562,0.928,0.723,0.527,0.166,0.143
        126,Iraq,4.437,1.043,0.980,0.574,0.241,0.148,0.089
        127,Congo (Kinshasa),4.418,0.094,1.125,0.357,0.269,0.212,0.053
        128,Mali,4.390,0.385,1.105,0.308,0.327,0.153,0.052
        129,Sierra Leone,4.374,0.268,0.841,0.242,0.309,0.252,0.045
        130,Sri Lanka,4.366,0.949,1.265,0.831,0.470,0.244,0.047
        131,Myanmar,4.360,0.710,1.181,0.555,0.525,0.566,0.172
        132,Chad,4.350,0.350,0.766,0.192,0.174,0.198,0.078
        133,Ukraine,4.332,0.820,1.390,0.739,0.178,0.187,0.010
        134,Ethiopia,4.286,0.336,1.033,0.532,0.344,0.209,0.100
        135,Swaziland,4.212,0.811,1.149,0.000,0.313,0.074,0.135
        136,Uganda,4.189,0.332,1.069,0.443,0.356,0.252,0.060
        137,Egypt,4.166,0.913,1.039,0.644,0.241,0.076,0.067
        138,Zambia,4.107,0.578,1.058,0.426,0.431,0.247,0.087
        139,Togo,4.085,0.275,0.572,0.410,0.293,0.177,0.085
        140,India,4.015,0.755,0.765,0.588,0.498,0.200,0.085
        141,Liberia,3.975,0.073,0.922,0.443,0.370,0.233,0.033
        142,Comoros,3.973,0.274,0.757,0.505,0.142,0.275,0.078
        143,Madagascar,3.933,0.274,0.916,0.555,0.148,0.169,0.041
        144,Lesotho,3.802,0.489,1.169,0.168,0.359,0.107,0.093
        145,Burundi,3.775,0.046,0.447,0.380,0.220,0.176,0.180
        146,Zimbabwe,3.663,0.366,1.114,0.433,0.361,0.151,0.089
        147,Haiti,3.597,0.323,0.688,0.449,0.026,0.419,0.110
        148,Botswana,3.488,1.041,1.145,0.538,0.455,0.025,0.100
        149,Syria,3.462,0.619,0.378,0.440,0.013,0.331,0.141
        150,Malawi,3.410,0.191,0.560,0.495,0.443,0.218,0.089
        151,Yemen,3.380,0.287,1.163,0.463,0.143,0.108,0.077
        152,Rwanda,3.334,0.359,0.711,0.614,0.555,0.217,0.411
        153,Tanzania,3.231,0.476,0.885,0.499,0.417,0.276,0.147
        154,Afghanistan,3.203,0.350,0.517,0.361,0.000,0.158,0.025
        155,Central African Republic,3.083,0.026,0.000,0.105,0.225,0.235,0.035
        156,South Sudan,2.853,0.306,0.575,0.295,0.010,0.202,0.091 
        """
        csv_data_2 = """
        Rank,Country,Cost of Living Index,Rent Index,Cost of Living Plus Rent Index,Groceries Index,Restaurant Price Index,Local Purchasing Power Index
        1,Afghanistan,20.37,2.72,12.09,14.92,12.41,23.04
        2,Albania,35.5,8.47,22.83,29.32,25.82,30.19
        3,Algeria,26.87,4.59,16.43,28.82,14.48,24.63
        4,Argentina,34.69,7.71,22.04,28.17,33.32,30.72
        5,Armenia,33.89,11.61,23.45,27.59,30.55,28.86
        6,Australia,77.75,36.84,58.57,77.44,72.95,104.63
        7,Austria,71.04,27.13,50.46,65.88,66.03,77.25
        8,Azerbaijan,29.73,7.86,19.48,26.57,26.73,27.26
        9,Bahamas,84,35.34,61.19,70.59,89.09,45.07
        10,Bahrain,54.77,29.22,42.79,44.59,48.94,61.41
        11,Bangladesh,33.13,4.42,19.67,30.41,21.7,25.3
        12,Barbados,92.37,21.99,59.38,87.81,78.18,32.08
        13,Belarus,30.89,9.81,21.01,27.24,31.64,31.78
        14,Belgium,72.61,25.79,50.67,63.32,78.63,79.72
        15,Belize,51.3,11.64,32.71,48.76,36.6,45.73
        16,Bermuda,146.04,98.58,123.8,148.66,159.17,81.07
        17,Bolivia,34.77,10.18,23.24,31.26,24.97,36.04
        18,Bosnia And Herzegovina,36.12,6.82,22.39,31.14,25.34,44.1
        19,Botswana,40.17,10.21,26.12,35.16,42.5,62.63
        20,Brazil,33.24,8.27,21.54,28.16,25.24,27.85
        21,Bulgaria,38.38,9.07,24.64,34.02,32.44,45.96
        22,Cambodia,49.11,15.68,33.44,50.61,22.9,13.32
        23,Cameroon,39.48,6.91,24.22,40.41,26.33,15.37
        24,Canada,70.22,34.33,53.4,70.01,67.86,87.98
        25,Chile,43.9,13.51,29.66,38.87,43.26,33.27
        26,China,41.77,16.53,29.93,46.01,28.37,59.99
        27,Colombia,26.72,8.18,18.03,23.47,19.44,28.85
        28,Costa Rica,47.01,14.7,31.87,45.54,41.69,39.88
        29,Croatia,48.94,13.38,32.27,41.98,41.29,47.55
        30,Cuba,55,15.23,36.36,47.93,33.54,1.45
        31,Cyprus,59.03,22.36,41.84,49.2,61.15,57.31
        32,Czech Republic,48.24,18.4,34.25,42.76,36.72,66.47
        33,Denmark,84.12,33.23,60.26,68.6,98.75,99.45
        34,Dominican Republic,41.77,9.59,26.68,38.45,34.3,21.07
        35,Ecuador,37.34,11.28,25.12,34.49,28.55,31.76
        36,Egypt,29.52,5.82,18.41,27.42,23.42,21.54
        37,El Salvador,44.37,13.19,29.75,44.32,35.47,21.17
        38,Estonia,53.68,16.37,36.19,42.29,56.43,63.46
        39,Ethiopia,47.49,16.88,33.14,36.68,18.03,10.15
        40,Fiji,43.16,17.76,31.26,48.06,37.42,35.87
        41,Finland,73.2,25.95,51.05,65.16,77.65,91.02
        42,France,74.13,25.33,51.26,73.64,71.84,85.41
        43,Georgia,30.18,9.26,20.37,26.44,27.88,31.15
        44,Germany,65.58,27.62,47.78,52.31,60.91,103.08
        45,Ghana,36.2,19.31,28.28,37.53,30.06,16.82
        46,Greece,56.22,12.68,35.81,44.73,52.19,39.73
        47,Guatemala,43.49,15.6,30.42,41.92,32.59,26.35
        48,Guernsey,83.59,54.02,69.73,76.76,89.98,71.57
        49,Honduras,40.46,10.28,26.31,34.73,28.67,32.09
        50,Hong Kong,80.71,74.57,77.83,84.72,58.58,65.74
        51,Hungary,40.66,11.91,27.18,35.19,32.82,51.98
        52,Iceland,94.86,41.93,70.05,90.22,99.42,77.06
        53,India,24.43,5.3,15.47,26.43,17.56,49.72
        54,Indonesia,35.85,9.82,23.65,38.29,17.74,21.07
        55,Iran,37.39,17.05,27.85,29.46,25.18,17.98
        56,Iraq,34.47,10.63,23.29,30.46,28.31,40.92
        57,Ireland,76.05,42.08,60.13,62.1,80.4,82.27
        58,Israel,88.05,33.94,62.69,76.72,95.31,75.58
        59,Italy,66.47,20.55,44.95,57.95,70.58,61.74
        60,Ivory Coast,47.03,17.68,33.27,40.22,31.99,6.92
        61,Jamaica,49.67,15.1,33.46,53.41,35.04,30.25
        62,Japan,77.03,25.86,53.04,81.31,45.4,87.11
        63,Jersey,92.02,65.33,79.51,76.88,94.65,79.14
        64,Jordan,49.19,9.23,30.46,40.81,41.16,31.34
        65,Kazakhstan,28.68,9.44,19.66,25.35,27.24,32.23
        66,Kenya,33.92,8.73,22.11,31.27,28.82,32.18
        67,Kosovo (Disputed Territory),27.05,8.04,18.14,24.84,19.53,43.86
        68,Kuwait,48.68,31.31,40.54,35.63,47.48,78.57
        69,Latvia,48.45,11.77,31.26,38.37,42.1,51.65
        70,Lebanon,69.62,24.81,48.61,66.83,54.25,35.12
        71,Libya,48.35,12.89,31.73,54.03,34.1,33.25
        72,Lithuania,45.65,15.01,31.29,36.18,46.64,58.74
        73,Luxembourg,80.5,60.09,70.93,74.75,88.79,98.84
        74,Macao,66.81,43,55.65,67.9,51.32,69.27
        75,Malaysia,37.02,9.87,24.29,39.45,20.84,55.3
        76,Maldives,57.66,30.2,44.78,56.6,34.72,28.59
        77,Malta,67.84,29.72,49.97,59.59,72.42,44.18
        78,Mauritius,44.08,10.95,28.55,45.61,33.44,29.62
        79,Mexico,35.35,12.55,24.66,34.82,32.67,38.62
        80,Moldova,30.35,8.7,20.2,24.96,27.1,33.43
        81,Mongolia,34.74,11.22,23.72,36.14,22.8,24.34
        82,Montenegro,38.95,12.87,26.72,31.76,33.22,34.19
        83,Morocco,33.83,8.98,22.18,30.63,24.52,34.36
        84,Myanmar,35.67,21.18,28.87,37.63,20,13.84
        85,Nepal,28.29,3.96,16.89,26.45,20.41,22.96
        86,Netherlands,75.66,36.06,57.1,65.49,76.35,87.99
        87,New Zealand,74.52,34.44,55.73,72.04,70.05,83.63
        88,Nicaragua,39.64,8.68,25.13,38.13,27.51,17.63
        89,Nigeria,30.49,35.99,33.07,33.65,20.92,9.34
        90,North Macedonia,31.38,6.06,19.51,26.95,21.02,35.44
        91,Norway,100.9,34.68,69.86,97.31,105.49,83.11
        92,Oman,49.42,16.77,34.11,46.51,43.24,84.24
        93,Pakistan,19.92,3.91,12.42,17.81,15.54,26.63
        94,Palestine,58.11,11.01,36.03,51.23,44.58,39.84
        95,Panama,51.43,21.75,37.51,52.16,43.38,33.09
        96,Paraguay,30.2,10.04,20.75,25.45,24.19,26.08
        97,Peru,32.53,11.22,22.54,30.71,21.53,28.17
        98,Philippines,37.06,9.59,24.18,37.84,20.61,21.47
        99,Poland,38.95,14.45,27.46,32.42,33.52,59.95
        100,Portugal,47.94,20.73,35.19,39.01,40.26,46.8
        101,Puerto Rico,66.53,18.4,43.97,69.6,55.6,72.78
        102,Qatar,62.81,48.2,55.96,54.97,63.01,93.67
        103,Romania,35.24,10.17,23.49,31.38,30.02,48.12
        104,Russia,35.26,13.09,24.87,29.86,34.56,37.41
        105,Rwanda,31.62,15.9,24.25,27.71,27.99,26.82
        106,Saudi Arabia,50.41,11.67,32.25,42.57,35.5,91.85
        107,Senegal,50.25,22.97,37.46,42.17,46.22,23.45
        108,Serbia,36.21,8.73,23.33,28.18,29.24,37.83
        109,Seychelles,65.93,32.35,50.19,61.55,77.01,19.43
        110,Singapore,83.98,66.43,75.75,77.08,61.17,91.34
        111,Slovakia,44.68,16.11,31.29,39.74,36.08,54.7
        112,Slovenia,53.88,17.9,37.01,47.71,46.74,59.48
        113,Somalia,34.58,5.16,20.79,39.39,26.65,29.4
        114,South Africa,42.09,16.6,30.14,34.78,41.33,78.36
        115,South Korea,73.22,20.02,48.28,91.95,42.1,76.85
        116,Spain,53.88,21.25,38.58,45.69,53.96,70.04
        117,Sri Lanka,31.29,8.23,20.48,37.67,17.27,19.27
        118,Suriname,51.78,9.71,32.06,45.92,79.61,13.44
        119,Sweden,71.74,25.86,50.23,65.78,72.61,98.14
        120,Switzerland,123.35,53.54,90.62,128.13,122.09,118.44
        121,Syria,28.75,5.17,17.7,29.34,22.81,6.59
        122,Taiwan,62.35,17.69,41.42,76.19,29.42,58.35
        123,Tanzania,32.81,12.36,23.23,30.04,24.86,15.97
        124,Thailand,43.21,14.69,29.84,45.15,22.59,31.56
        125,Trinidad And Tobago,54.88,15.97,36.64,53.96,53.74,38.47
        126,Tunisia,27.87,5.32,17.3,27.36,15.96,27.83
        127,Turkey,28.31,6.63,18.15,22.64,18.4,32.88
        128,Uganda,33.5,9.19,22.1,31,24.85,11.41
        129,Ukraine,30.71,10.57,21.27,26.3,25.75,37.22
        130,United Arab Emirates,58.33,43.28,51.28,46.67,61.53,92.17
        131,United Kingdom,69.65,31.84,51.93,56.58,76.79,88.78
        132,United States,70.13,42.07,56.98,70.37,70.07,106.34
        133,Uruguay,52.07,13.93,34.19,44.01,49.39,30.07
        134,Uzbekistan,27.31,9.29,18.86,26.83,24.22,22.37
        135,Venezuela,43.2,9.99,27.63,37.34,46.23,15.41
        136,Vietnam,37.48,13.22,26.11,38.7,19.98,29.38
        137,Yemen,53.14,6.71,31.38,67.12,24.74,14.41
        138,Zambia,33.04,9.26,21.9,31.53,22.46,40.33
        139,Zimbabwe,45.68,8.75,28.37,39.88,38.13,19.07
        """
        # Read CSV data into pandas DataFrames
        df1 = pd.read_csv(StringIO(csv_data_1))
        df2 = pd.read_csv(StringIO(csv_data_2))

        # Rename columns to match
        df2.rename(columns={"Country": "Country or region"}, inplace=True)

        # Merge datasets
# Merge datasets
        combined_df = pd.merge(df1, df2, on="Country or region", how="inner")

        # Drop 'Overall rank' from df1 and 'Rank' from df2 if they exist
        if 'Overall rank' in combined_df.columns:
            combined_df.drop(columns=['Overall rank'], inplace=True)
        if 'Rank' in combined_df.columns:
            combined_df.drop(columns=['Rank'], inplace=True)

        # Clear existing data in the database
        CountryData.objects.all().delete()

        # Populate new data
        for _, row in combined_df.iterrows():
            CountryData.objects.create(
                country_or_region=row['Country or region'],
                score=row['Score'],
                gdp_per_capita=row['GDP per capita'],
                social_support=row['Social support'],
                healthy_life_expectancy=row['Healthy life expectancy'],
                freedom_to_make_life_choices=row['Freedom to make life choices'],
                generosity=row['Generosity'],
                perceptions_of_corruption=row['Perceptions of corruption'],
                cost_of_living_index=row['Cost of Living Index'],
                rent_index=row['Rent Index'],
                cost_of_living_plus_rent_index=row['Cost of Living Plus Rent Index'],
                groceries_index=row['Groceries Index'],
                restaurant_price_index=row['Restaurant Price Index'],
                local_purchasing_power_index=row['Local Purchasing Power Index']
            )
        print("Database populated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
populate_database()