
from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf

# Used to reconstruct the colormap in pycam02ucs.cm.viscm
parameters = {'xp': [2.1581435310413326, 54.01370687724014, 55.938716989168853, 41.882492089570462, -11.846508176523287, -42.13044634856628, -11.80261541678101, -48.3048415098566, -21.235560651796106, 2.1581435310413326],
              'yp': [29.17744717550667, 37.432795698924735, -13.312340270171546, -33.11883899233294, -64.00369623655911, -60.18145161290319, 2.0105648986632048, 49.48756720430109, 26.53622250970244, 28.800129366106063],
              'min_Jp': 50.233463035,
              'max_Jp': 50.233463035}

cm_data = [[ 0.54045421,  0.4196555 ,  0.06347418],
       [ 0.54730313,  0.41608002,  0.05787023],
       [ 0.55396526,  0.41250526,  0.05237599],
       [ 0.56062932,  0.4088305 ,  0.04685219],
       [ 0.56715049,  0.40513519,  0.04143911],
       [ 0.57364244,  0.40135514,  0.03613659],
       [ 0.58001563,  0.39754217,  0.03136507],
       [ 0.58634481,  0.39365153,  0.02709322],
       [ 0.59256228,  0.38972462,  0.02336793],
       [ 0.59873495,  0.38571891,  0.0201508 ],
       [ 0.60478844,  0.38168256,  0.01748195],
       [ 0.61080797,  0.37755829,  0.01532752],
       [ 0.61668887,  0.37341786,  0.01372726],
       [ 0.6225559 ,  0.36917277,  0.01265375],
       [ 0.62827631,  0.36491863,  0.0121382 ],
       [ 0.63396781,  0.3605678 ,  0.01217716],
       [ 0.63953961,  0.35618867,  0.01278313],
       [ 0.64503004,  0.35175169,  0.01396815],
       [ 0.65044656,  0.34724976,  0.01575193],
       [ 0.65573427,  0.34272904,  0.01812953],
       [ 0.6609785 ,  0.33811585,  0.02116196],
       [ 0.6661021 ,  0.33347694,  0.02483291],
       [ 0.67111451,  0.32880509,  0.02916811],
       [ 0.67606094,  0.3240572 ,  0.03424283],
       [ 0.68088115,  0.31929062,  0.04003363],
       [ 0.68558598,  0.31449617,  0.04623462],
       [ 0.69020947,  0.30963852,  0.05265706],
       [ 0.69470384,  0.3047677 ,  0.05922633],
       [ 0.69906999,  0.29988476,  0.06593281],
       [ 0.70333262,  0.29496265,  0.07281271],
       [ 0.70746894,  0.29002796,  0.07983309],
       [ 0.71146798,  0.28509578,  0.08697936],
       [ 0.71532817,  0.28017074,  0.0942545 ],
       [ 0.71906087,  0.27524025,  0.10169038],
       [ 0.72265121,  0.27032586,  0.1092704 ],
       [ 0.72608999,  0.26544365,  0.11698672],
       [ 0.72937418,  0.26060213,  0.12484421],
       [ 0.73250048,  0.25581087,  0.1328474 ],
       [ 0.73546988,  0.25107298,  0.14101328],
       [ 0.73827564,  0.24640421,  0.14933877],
       [ 0.74091029,  0.24182316,  0.15781535],
       [ 0.74337062,  0.23734254,  0.16644482],
       [ 0.74565353,  0.23297571,  0.17522793],
       [ 0.7477561 ,  0.22873656,  0.18416437],
       [ 0.74967564,  0.22463932,  0.19325268],
       [ 0.75140982,  0.2206984 ,  0.20249029],
       [ 0.75295764,  0.2169257 ,  0.21187998],
       [ 0.75431609,  0.21333869,  0.22140932],
       [ 0.75548405,  0.20995135,  0.23107166],
       [ 0.75646099,  0.20677664,  0.24086035],
       [ 0.75724683,  0.20382667,  0.25076779],
       [ 0.75784195,  0.20111256,  0.26078551],
       [ 0.75824718,  0.19864419,  0.27090427],
       [ 0.75846377,  0.19643006,  0.28111414],
       [ 0.75849339,  0.1944771 ,  0.29140462],
       [ 0.7583381 ,  0.19279058,  0.30176475],
       [ 0.75800032,  0.19137402,  0.31218316],
       [ 0.7574828 ,  0.19022913,  0.32264827],
       [ 0.7567886 ,  0.18935581,  0.33314829],
       [ 0.75592101,  0.18875218,  0.34367136],
       [ 0.75488364,  0.18841468,  0.354205  ],
       [ 0.75368023,  0.18833811,  0.36473761],
       [ 0.75231467,  0.18851579,  0.37525771],
       [ 0.75079098,  0.18893981,  0.385754  ],
       [ 0.74911327,  0.18960111,  0.39621548],
       [ 0.74728572,  0.19048976,  0.40663149],
       [ 0.74531256,  0.19159505,  0.41699173],
       [ 0.74319801,  0.19290577,  0.42728632],
       [ 0.74094633,  0.19441035,  0.43750582],
       [ 0.73856174,  0.19609699,  0.44764127],
       [ 0.73604842,  0.19795387,  0.45768419],
       [ 0.73341053,  0.19996922,  0.4676266 ],
       [ 0.73065214,  0.2021315 ,  0.47746104],
       [ 0.72777734,  0.20442937,  0.48718034],
       [ 0.72479062,  0.20685144,  0.49677635],
       [ 0.72169522,  0.2093877 ,  0.50624531],
       [ 0.71849484,  0.21202814,  0.51558191],
       [ 0.7151931 ,  0.21476323,  0.52478134],
       [ 0.71179352,  0.21758393,  0.53383932],
       [ 0.70829947,  0.22048173,  0.54275203],
       [ 0.70471423,  0.22344864,  0.55151616],
       [ 0.70104094,  0.22647717,  0.56012886],
       [ 0.6972826 ,  0.22956034,  0.56858773],
       [ 0.6934421 ,  0.23269164,  0.5768908 ],
       [ 0.68952238,  0.23586485,  0.58503606],
       [ 0.68552579,  0.2390746 ,  0.59302289],
       [ 0.68145452,  0.24231594,  0.60085097],
       [ 0.67731081,  0.24558418,  0.60851989],
       [ 0.6730967 ,  0.24887502,  0.61602957],
       [ 0.6688141 ,  0.25218455,  0.62338025],
       [ 0.6644647 ,  0.25550923,  0.63057242],
       [ 0.66005003,  0.25884588,  0.63760682],
       [ 0.65557141,  0.26219164,  0.64448442],
       [ 0.65102995,  0.265544  ,  0.65120636],
       [ 0.64642577,  0.26890131,  0.65777503],
       [ 0.64175993,  0.27226136,  0.66419122],
       [ 0.63703294,  0.27562251,  0.6704563 ],
       [ 0.63224501,  0.2789834 ,  0.67657178],
       [ 0.62739609,  0.28234296,  0.68253917],
       [ 0.62248591,  0.28570038,  0.68835996],
       [ 0.61751393,  0.2890551 ,  0.69403555],
       [ 0.61247932,  0.2924068 ,  0.69956725],
       [ 0.60738102,  0.2957554 ,  0.7049562 ],
       [ 0.60221766,  0.29910104,  0.71020335],
       [ 0.5969876 ,  0.30244407,  0.71530942],
       [ 0.59168733,  0.30578605,  0.72027628],
       [ 0.58631564,  0.30912708,  0.72510296],
       [ 0.58087046,  0.3124678 ,  0.72978876],
       [ 0.57534902,  0.31580932,  0.73433295],
       [ 0.56974829,  0.31915287,  0.73873432],
       [ 0.56406494,  0.32249984,  0.74299118],
       [ 0.55829538,  0.32585174,  0.74710128],
       [ 0.55243573,  0.3292102 ,  0.75106178],
       [ 0.5464819 ,  0.33257692,  0.75486919],
       [ 0.54042954,  0.33595368,  0.75851938],
       [ 0.5342741 ,  0.3393423 ,  0.76200748],
       [ 0.52801085,  0.3427446 ,  0.76532792],
       [ 0.5216349 ,  0.34616241,  0.76847432],
       [ 0.51514125,  0.34959748,  0.77143955],
       [ 0.50852487,  0.35305148,  0.77421565],
       [ 0.50178069,  0.35652596,  0.77679388],
       [ 0.49490371,  0.3600223 ,  0.7791647 ],
       [ 0.48788908,  0.36354163,  0.78131778],
       [ 0.48073219,  0.36708484,  0.78324209],
       [ 0.47342875,  0.37065248,  0.7849259 ],
       [ 0.46597491,  0.3742447 ,  0.78635688],
       [ 0.45836741,  0.37786124,  0.78752222],
       [ 0.45060369,  0.38150131,  0.78840876],
       [ 0.4426788 ,  0.3851651 ,  0.7890033 ],
       [ 0.4345922 ,  0.38885054,  0.78929205],
       [ 0.42634733,  0.3925537 ,  0.78926152],
       [ 0.41794634,  0.3962712 ,  0.78889895],
       [ 0.40939297,  0.39999892,  0.78819234],
       [ 0.40069277,  0.403732  ,  0.78713074],
       [ 0.39185321,  0.40746486,  0.78570458],
       [ 0.38288269,  0.41119167,  0.78390574],
       [ 0.37378872,  0.41490719,  0.78172713],
       [ 0.36459208,  0.41860108,  0.77916657],
       [ 0.35530947,  0.42226522,  0.77622332],
       [ 0.34595986,  0.42589114,  0.77289948],
       [ 0.33656446,  0.42947018,  0.76920011],
       [ 0.32714523,  0.43299409,  0.76513273],
       [ 0.3177301 ,  0.43645322,  0.76070967],
       [ 0.30834647,  0.43983906,  0.75594549],
       [ 0.29902227,  0.44314383,  0.75085718],
       [ 0.28978625,  0.4463604 ,  0.74546412],
       [ 0.28067074,  0.44948133,  0.73978979],
       [ 0.2717046 ,  0.4525013 ,  0.73385746],
       [ 0.26291512,  0.4554163 ,  0.72769078],
       [ 0.25432988,  0.45822294,  0.72131482],
       [ 0.24597514,  0.46091886,  0.71475498],
       [ 0.23787563,  0.46350265,  0.70803664],
       [ 0.23006058,  0.46597182,  0.70119065],
       [ 0.22254306,  0.46832914,  0.6942353 ],
       [ 0.21534017,  0.47057609,  0.68719319],
       [ 0.20846605,  0.47271487,  0.68008553],
       [ 0.20193167,  0.47474834,  0.67293205],
       [ 0.19574461,  0.47667993,  0.66575084],
       [ 0.18990893,  0.47851354,  0.65855825],
       [ 0.18442508,  0.48025345,  0.65136892],
       [ 0.17929028,  0.48190411,  0.64419631],
       [ 0.1744992 ,  0.48346984,  0.63705394],
       [ 0.17003898,  0.48495643,  0.62994766],
       [ 0.16589608,  0.4863689 ,  0.62288527],
       [ 0.16205388,  0.48771233,  0.61587301],
       [ 0.15849303,  0.48899179,  0.60891568],
       [ 0.15519176,  0.49021229,  0.60201668],
       [ 0.15212633,  0.49137876,  0.59517809],
       [ 0.14927145,  0.49249602,  0.58840077],
       [ 0.14660071,  0.49356872,  0.58168443],
       [ 0.14408705,  0.49460139,  0.57502766],
       [ 0.1417032 ,  0.49559832,  0.56842806],
       [ 0.13942206,  0.49656365,  0.56188228],
       [ 0.13721712,  0.49750125,  0.55538607],
       [ 0.13506277,  0.49841479,  0.54893436],
       [ 0.13293463,  0.49930766,  0.54252132],
       [ 0.13080983,  0.50018301,  0.53614044],
       [ 0.12866733,  0.50104366,  0.52978482],
       [ 0.12648813,  0.5018921 ,  0.52344731],
       [ 0.12425485,  0.50273076,  0.51711853],
       [ 0.12195275,  0.50356163,  0.51078974],
       [ 0.11956963,  0.50438634,  0.50445185],
       [ 0.11709598,  0.50520624,  0.49809544],
       [ 0.11452519,  0.50602233,  0.49171087],
       [ 0.11185378,  0.50683531,  0.48528834],
       [ 0.10908166,  0.50764554,  0.47881794],
       [ 0.10621244,  0.50845304,  0.47228974],
       [ 0.10325381,  0.50925753,  0.46569384],
       [ 0.10021799,  0.51005844,  0.45902043],
       [ 0.09712225,  0.51085486,  0.45225985],
       [ 0.09398947,  0.51164562,  0.44540264],
       [ 0.09084891,  0.51242926,  0.43843956],
       [ 0.08773687,  0.51320406,  0.43136164],
       [ 0.08469747,  0.51396806,  0.42416021],
       [ 0.08178332,  0.51471907,  0.41682689],
       [ 0.07905545,  0.51545479,  0.40935232],
       [ 0.07658465,  0.51617253,  0.40172939],
       [ 0.07444984,  0.5168694 ,  0.39395127],
       [ 0.07273623,  0.51754239,  0.38601095],
       [ 0.07153262,  0.51818831,  0.37790169],
       [ 0.0709271 ,  0.51880377,  0.36961699],
       [ 0.07100176,  0.51938525,  0.36115061],
       [ 0.07182695,  0.51992901,  0.35249647],
       [ 0.073456  ,  0.52043114,  0.34364866],
       [ 0.07592174,  0.52088756,  0.33460119],
       [ 0.07923802,  0.52129421,  0.32534117],
       [ 0.08339496,  0.52164624,  0.31586731],
       [ 0.08836684,  0.52193874,  0.30617348],
       [ 0.09411567,  0.5221665 ,  0.29625365],
       [ 0.10059616,  0.52232393,  0.2861019 ],
       [ 0.10776013,  0.52240501,  0.27571252],
       [ 0.11556005,  0.52240323,  0.26508018],
       [ 0.12395866,  0.52231147,  0.25419096],
       [ 0.13294031,  0.52212122,  0.2430122 ],
       [ 0.14244824,  0.52182404,  0.23157051],
       [ 0.15245267,  0.52141059,  0.21986525],
       [ 0.16297526,  0.52086811,  0.20784568],
       [ 0.1739769 ,  0.52018534,  0.19554069],
       [ 0.18544027,  0.51934938,  0.18296221],
       [ 0.19739616,  0.51834225,  0.17008039],
       [ 0.20978897,  0.51715174,  0.15697115],
       [ 0.22262369,  0.51575981,  0.14365972],
       [ 0.23586189,  0.51415215,  0.13023659],
       [ 0.24941456,  0.51232211,  0.116867  ],
       [ 0.26319051,  0.51026698,  0.10374734],
       [ 0.27705948,  0.50799493,  0.09114748],
       [ 0.29083647,  0.50553138,  0.07942162],
       [ 0.30435112,  0.50290976,  0.06893298],
       [ 0.31745963,  0.50016816,  0.06002268],
       [ 0.33006308,  0.49734312,  0.05295971],
       [ 0.34206206,  0.49447733,  0.04791143],
       [ 0.3534908 ,  0.49158438,  0.04484622],
       [ 0.36434933,  0.48868512,  0.04360858],
       [ 0.37466183,  0.48579324,  0.04391633],
       [ 0.38448698,  0.4829105 ,  0.04543195],
       [ 0.393878  ,  0.4800371 ,  0.0478252 ],
       [ 0.40284454,  0.47718453,  0.05079215],
       [ 0.41147352,  0.47433763,  0.05410874],
       [ 0.41979829,  0.47149565,  0.05759074],
       [ 0.42783083,  0.46866386,  0.06108966],
       [ 0.43561815,  0.46583396,  0.06450874],
       [ 0.4431985 ,  0.46299887,  0.06777526],
       [ 0.4505975 ,  0.46015476,  0.07083054],
       [ 0.45783901,  0.45729737,  0.07362892],
       [ 0.46494526,  0.4544221 ,  0.07613348],
       [ 0.47193687,  0.45152409,  0.07831271],
       [ 0.47883301,  0.44859824,  0.08013796],
       [ 0.48565144,  0.44563926,  0.08158131],
       [ 0.49240857,  0.44264175,  0.08261382],
       [ 0.49911959,  0.43960016,  0.08320374],
       [ 0.50579844,  0.43650888,  0.08331478],
       [ 0.51245787,  0.43336231,  0.08290405],
       [ 0.51910945,  0.43015484,  0.08191953],
       [ 0.52576349,  0.42688097,  0.08029676],
       [ 0.53242898,  0.42353543,  0.07795417],
       [ 0.53911344,  0.42011326,  0.07478632]]

test_cm = LinearSegmentedColormap.from_list(__file__, cm_data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from pycam02ucs.cm.viscm import viscm
        viscm(test_cm)
    except ImportError:
        print("pycam02ucs not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=test_cm)
    plt.show()