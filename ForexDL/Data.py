import pandas as pd
import tensorflow as tf
import oandapy as od
from talib.abstract import *
import numpy as np
import time as tm
import logging as log




#1420070400


def getDataBatch(startTime="0", instrument="EUR_USD"):
    account = od.API(environment="practice", access_token="", headers={'X-Accept-Datetime-Format': 'UNIX'})
    hist = account.get_history(instrument="EUR_USD", granularity="M1", start=startTime, count="5000", candleFormat="midpoint")
    data = hist['candles']
    close = np.ndarray([0])
    high = np.ndarray([0])
    low = np.ndarray([0])
    volume = np.ndarray([0])
    openMid = np.ndarray([0])
    time = np.ndarray([0])
    for x in data:
        cur = x
        close = np.append(close, float(cur.get('closeMid')))
        high = np.append(high, float(cur.get('highMid')))
        low = np.append(low, float(cur.get('lowMid')))
        volume = np.append(volume, float(cur.get('volume')))
        openMid = np.append(openMid, float(cur.get('openMid')))
        time = np.append(time, float(cur.get('time')))
       
    return close, high, low, volume, openMid, time
        
def getData(startTime="0", instrument="EUR_USD", endTime="0"):
    close, high, low, volume, openMid, time = getDataBatch(startTime=startTime, instrument=instrument)
    
    while int(time[len(time)-1]) < int(endTime):
        #60000000
        close2, high2, low2, volume2, open2, time2 = getDataBatch(startTime=str(int(time[len(time)])+60000000), instrument=instrument)
        close = np.append(close, close2)
        high = np.append(high, high2)
        low = np.append(low, low2)
        volume = np.append(volume, volume2)
        openMid = np.append(openMid, open2)
        time = np.append(time, time2)
        tm.sleep(0.1)
        
    return close, high, low, volume, openMid, time
        
def expandData(startTime="0", instrument="EUR_USD", endTime="0"):
    close, high, low, volume, openMid, time = getData(startTime=startTime, instrument=instrument, endTime=endTime)
    inputs = {
    'open': openMid,
    'high': high,
    'low': low,
    'close': close,
    'volume': volume
    }
    #print (type(inputs.get('open')))
    #Overlap Studies
    sma = SMA(inputs)
    bbuper, bbmiddle, bblower = BBANDS(inputs)
    dema = DEMA(inputs)
    ema = EMA(inputs)
    htTrend = HT_TRENDLINE(inputs)
    kama = KAMA(inputs)
    ma = MA(inputs)
    mama, fama = MAMA(inputs)
    midpoint = MIDPOINT(inputs)
    midprice = MIDPRICE(inputs)
    sar = SAR(inputs)
    sarext = SAREXT(inputs)
    t3 = T3(inputs)
    trima = TRIMA(inputs)
    wma = WMA(inputs)
    
    #Momentum Indicators
    adx = ADX(inputs)
    adxr = ADXR(inputs)
    apo =APO(inputs)
    aroonDown, aroonUp = AROON(inputs)
    aroon = AROONOSC(inputs)
    bop = BOP(inputs)
    cci = CCI(inputs)
    cmo = CMO(inputs)
    dx = DX(inputs)
    macd, macds, macdh = MACD(inputs)
    macdext, macdexts, macdexth = MACDEXT(inputs)
    macdfix, macdfixs, macdfixh = MACDFIX(inputs)
    mfi = MFI(inputs)
    minusdi = MINUS_DI(inputs)
    minusdm = MINUS_DM(inputs)
    mom = MOM(inputs)
    plusdi = PLUS_DI(inputs)
    plusdm = PLUS_DM(inputs)
    ppo = PPO(inputs)
    roc = ROC(inputs)
    rocp = ROCP(inputs)
    rocr = ROCR(inputs)
    rocr100 = ROCR100(inputs)
    rsi = RSI(inputs)
    slowk, slowd = STOCH(inputs)
    fastk, fastd = STOCHF(inputs)
    rsifastk, rsifastd = STOCHRSI(inputs)
    trix = TRIX(inputs)
    ultosc = ULTOSC(inputs)
    willr = WILLR(inputs)
    
    
    #volume indicators
    ad = AD(inputs)
    adosc = ADOSC(inputs)
    obv = OBV(inputs)
    
    #cycle indicators
    ht_dcperiod = HT_DCPERIOD(inputs)
    ht_dcphase = HT_DCPHASE(inputs)
    ht_phasor_inphase, ht_phasor_quadrature = HT_PHASOR(inputs)
    ht_sine, ht_leadsine = HT_SINE(inputs)
    ht_trendmode = HT_TRENDMODE(inputs)
    
    #price transform
    avgprice = AVGPRICE(inputs)
    medprice = MEDPRICE(inputs)
    typrice = TYPPRICE(inputs)
    wclprice = WCLPRICE(inputs)
    
    #volatility ind
    atr = ATR(inputs)
    natr = NATR(inputs)
    trange = TRANGE(inputs)
    
    
    #pattern rec
    twocrows = CDL2CROWS(inputs)
    threeblackcrows = CDL3BLACKCROWS(inputs)
    threeinside = CDL3INSIDE(inputs)
    threelinestrike = CDL3LINESTRIKE(inputs)
    threeoutside = CDL3OUTSIDE(inputs)
    threestarsinsouth = CDL3STARSINSOUTH(inputs)
    threeWhiteSoldiers = CDL3WHITESOLDIERS(inputs)
    abandonBaby = CDLABANDONEDBABY(inputs)
    advanceBlock = CDLADVANCEBLOCK(inputs)
    beltHold = CDLBELTHOLD(inputs)
    breakAway = CDLBREAKAWAY(inputs)
    closingM = CDLCLOSINGMARUBOZU(inputs)
    consealBabySwall = CDLCONCEALBABYSWALL(inputs)
    counterAttack = CDLCOUNTERATTACK(inputs)
    darkCloudCover = CDLDARKCLOUDCOVER(inputs)
    doji = CDLDOJI(inputs)
    dojiStar = CDLDOJISTAR(inputs)
    dragonFlyDoji = CDLDRAGONFLYDOJI(inputs)
    engulfing = CDLENGULFING(inputs)
    eveningDojiStar = CDLEVENINGDOJISTAR(inputs)
    eveningStar = CDLEVENINGSTAR(inputs)
    gapSideSideWhite = CDLGAPSIDESIDEWHITE(inputs)
    graveStoneDoji = CDLGRAVESTONEDOJI(inputs)
    hammer = CDLHAMMER(inputs)
    hangingMan = CDLHANGINGMAN(inputs)
    harami = CDLHARAMI(inputs)
    haramiCross = CDLHARAMICROSS(inputs)
    highWave = CDLHIGHWAVE(inputs)
    hikkake = CDLHIKKAKE(inputs)
    hikkakeMod = CDLHIKKAKEMOD(inputs)
    homingPigeon = CDLHOMINGPIGEON(inputs)
    identical3Crows = CDLIDENTICAL3CROWS(inputs)
    inNeck = CDLINNECK(inputs)
    invertedHammer = CDLINVERTEDHAMMER(inputs)
    kicking = CDLKICKING(inputs)
    kickingByLength = CDLKICKINGBYLENGTH(inputs)
    ladderBottom = CDLLADDERBOTTOM(inputs)
    longLeggedDoji = CDLLONGLEGGEDDOJI(inputs)
    longLine = CDLLONGLINE(inputs)
    maruBozu = CDLMARUBOZU(inputs)
    matchingLow = CDLMATCHINGLOW(inputs)
    matHold = CDLMATHOLD(inputs)
    morningDojiStar = CDLMORNINGDOJISTAR(inputs)
    morningStar = CDLMORNINGSTAR(inputs)
    onNeck = CDLONNECK(inputs)
    piercing = CDLPIERCING(inputs)
    rickShawman = CDLRICKSHAWMAN(inputs)
    riseFall3Methods = CDLRISEFALL3METHODS(inputs)
    seperatingLines = CDLSEPARATINGLINES(inputs)
    shootingStar = CDLSHOOTINGSTAR(inputs)
    shortline = CDLSHORTLINE(inputs)
    spinningTop = CDLSPINNINGTOP(inputs)
    stalledPattern = CDLSTALLEDPATTERN(inputs)
    stickSandwhich = CDLSTICKSANDWICH(inputs)
    takuri = CDLTAKURI(inputs)
    tasukiGap = CDLTASUKIGAP(inputs)
    thrusting = CDLTHRUSTING(inputs)
    triStar = CDLTRISTAR(inputs)
    unique3River = CDLUNIQUE3RIVER(inputs)
    upsideGap2Crows = CDLUPSIDEGAP2CROWS(inputs)
    xSdieGap3Methods = CDLXSIDEGAP3METHODS(inputs)
    
    data = np.array([close, high, low, volume, openMid, time, sma, bbuper, bbmiddle, bblower, dema, ema, htTrend, kama, ma, mama, fama, midpoint, midprice, sar, sarext, t3, trima, wma, adx, adxr, ppo, apo, aroonDown, aroonUp, aroon, bop, cci, cmo, dx, macd, macds, macdh, macdext, macdexts, macdexth, macdfix, macdfixs, macdfixh, mfi, minusdi, minusdm, mom, plusdi, plusdm, roc, rocr, rocp, rocr100, rsi, slowk, slowd, fastk, fastd, rsifastk, rsifastd, trix, ultosc, willr, ad, adosc, obv, ht_dcperiod, ht_dcphase, ht_phasor_inphase, ht_phasor_quadrature, ht_sine, ht_leadsine, ht_trendmode, avgprice, medprice, typrice, wclprice, atr, natr, trange, twocrows, threeblackcrows, threeinside, threelinestrike, threeoutside, threestarsinsouth, threeWhiteSoldiers, abandonBaby, advanceBlock, beltHold, breakAway, closingM, consealBabySwall, counterAttack, darkCloudCover, doji, dojiStar, dragonFlyDoji, engulfing, eveningDojiStar, eveningStar, gapSideSideWhite, graveStoneDoji, hammer, hangingMan, harami, haramiCross, highWave, hikkake,  hikkakeMod, homingPigeon, identical3Crows, inNeck, invertedHammer, kicking, kickingByLength, ladderBottom, longLeggedDoji, longLine, maruBozu, matchingLow, matHold, morningDojiStar, morningStar, onNeck, piercing, rickShawman, riseFall3Methods, seperatingLines, shootingStar, shortline, spinningTop, stalledPattern, stickSandwhich, takuri, tasukiGap, thrusting, triStar, unique3River, upsideGap2Crows, xSdieGap3Methods])
    
    return data

def int64(value):
    value = float(value)
    val = tf.train.Feature(float_list=tf.train.FloatList(value=[value]))
    
    return val

def findLabel(current, next):
    dif = next - current
    dif = dif*10000
    print('dif = '+str(dif))
    if dif < -100:
        return 0
    elif dif < -50:
        return 1
    elif dif < -25:
        return 2
    elif dif < -20:
        return 3
    elif dif < -15:
        return 4
    elif dif < -10:
        return 5
    elif dif < -5:
        return 6
    elif dif < 0:
        return 7
    elif dif < 5:
        return 8
    elif dif < 10:
        return 9
    elif dif < 15:
        return 10
    elif dif < 20:
        return 11
    elif dif < 25:
        return 12
    elif dif < 50:
        return 13
    elif dif < 100:
        return 14
    elif dif > 100:
        return 15
  
def packData(input, filename="EURUSD"):
    write = tf.python_io.TFRecordWriter(filename+".tfrecords")
    a = 0
    while a < (len(input[1])-1440):
        label = findLabel(float(input[0][a]), float(input[0][a+1440]))
        print(label)
        example = tf.train.Example(features=tf.train.Features(feature={'label':int64(label), 
                                                                       'close': int64(input[0][a]), 
                                                                       'high': int64(input[1][a]), 
                                                                       'low': int64(input[2][a]), 
                                                                       'volume': int64(input[3][a]), 
                                                                       'openMid': int64(input[4][a]), 
                                                                       'time': int64(input[5][a]), 
                                                                       'sma': int64(input[6][a]), 
                                                                       'bbuper': int64(input[7][a]), 
                                                                       'bbmiddle': int64(input[8][a]), 
                                                                       'bblower': int64(input[9][a]), 
                                                                       'dema': int64(input[10][a]), 
                                                                       'ema': int64(input[11][a]), 
                                                                       'htTrend': int64(input[12][a]), 
                                                                       'kama': int64(input[13][a]), 
                                                                       'ma': int64(input[14][a]), 
                                                                       'mama': int64(input[15][a]), 
                                                                       'fama': int64(input[16][a]), 
                                                                       'midpoint': int64(input[17][a]), 
                                                                       'midprice': int64(input[18][a]), 
                                                                       'sar': int64(input[19][a]), 
                                                                       'sarext': int64(input[20][a]), 
                                                                       't3': int64(input[21][a]), 
                                                                       'trima': int64(input[22][a]), 
                                                                       'wma': int64(input[23][a]), 
                                                                       'adx': int64(input[24][a]), 
                                                                       'adxr': int64(input[25][a]), 
                                                                       'ppo': int64(input[26][a]), 
                                                                       'apo': int64(input[27][a]), 
                                                                       'aroonDown': int64(input[28][a]), 
                                                                       'aroonUp': int64(input[29][a]), 
                                                                       'aroon': int64(input[30][a]), 
                                                                       'bop': int64(input[31][a]), 
                                                                       'cci': int64(input[32][a]), 
                                                                       'cmo': int64(input[33][a]), 
                                                                       'dx': int64(input[34][a]), 
                                                                       'macd': int64(input[35][a]), 
                                                                       'macds': int64(input[36][a]), 
                                                                       'macdh': int64(input[37][a]), 
                                                                       'macdext': int64(input[38][a]), 
                                                                       'macdexts': int64(input[39][a]), 
                                                                       'macdexth': int64(input[40][a]), 
                                                                       'macdfix': int64(input[41][a]), 
                                                                       'macdfixs': int64(input[42][a]), 
                                                                       'macdfixh': int64(input[43][a]), 
                                                                       'mfi': int64(input[44][a]), 
                                                                       'minusdi': int64(input[45][a]), 
                                                                       'minusdm': int64(input[46][a]), 
                                                                       'mom': int64(input[47][a]), 
                                                                       'plusdi': int64(input[48][a]), 
                                                                       'plusdm': int64(input[49][a]), 
                                                                       'roc': int64(input[50][a]), 
                                                                       'rocr': int64(input[51][a]), 
                                                                       'rocp': int64(input[52][a]), 
                                                                       'rocr100': int64(input[53][a]), 
                                                                       'rsi': int64(input[54][a]), 
                                                                       'slowk': int64(input[55][a]), 
                                                                       'slowd': int64(input[56][a]), 
                                                                       'fastk': int64(input[57][a]), 
                                                                       'fastd': int64(input[58][a]), 
                                                                       'rsifastk': int64(input[59][a]), 
                                                                       'rsifastd': int64(input[60][a]), 
                                                                       'trix': int64(input[61][a]), 
                                                                       'ultosc': int64(input[62][a]), 
                                                                       'willr': int64(input[63][a]), 
                                                                       'ad': int64(input[64][a]), 
                                                                       'adosc': int64(input[65][a]), 
                                                                       'obv': int64(input[66][a]), 
                                                                       'ht_dcperiod': int64(input[67][a]), 
                                                                       'ht_dcphase': int64(input[68][a]), 
                                                                       'ht_phasor_inphase': int64(input[69][a]), 
                                                                       'ht_phasor_quadrature': int64(input[70][a]), 
                                                                       'ht_sine': int64(input[71][a]), 
                                                                       'ht_leadsine': int64(input[72][a]), 
                                                                       'ht_trendmode': int64(input[73][a]), 
                                                                       'avgprice': int64(input[74][a]), 
                                                                       'medprice': int64(input[75][a]), 
                                                                       'typrice': int64(input[76][a]), 
                                                                       'wclprice': int64(input[77][a]), 
                                                                       'atr': int64(input[78][a]), 
                                                                       'natr': int64(input[79][a]), 
                                                                       'trange': int64(input[80][a]), 
                                                                       'twocrows': int64(input[81][a]), 
                                                                       'threeblackcrows': int64(input[82][a]), 
                                                                       'threeinside': int64(input[83][a]), 
                                                                       'threelinestrike': int64(input[84][a]), 
                                                                       'threeoutside': int64(input[85][a]), 
                                                                       'threestarsinsouth': int64(input[86][a]), 
                                                                       'threeWhiteSoldiers': int64(input[87][a]), 
                                                                       'abandonBaby': int64(input[88][a]), 
                                                                       'advanceBlock': int64(input[89][a]), 
                                                                       'beltHold': int64(input[90][a]), 
                                                                       'breakAway': int64(input[91][a]), 
                                                                       'closingM': int64(input[92][a]), 
                                                                       'consealBabySwall': int64(input[93][a]), 
                                                                       'counterAttack': int64(input[94][a]), 
                                                                       'darkCloudCover': int64(input[95][a]), 
                                                                       'doji': int64(input[96][a]), 
                                                                       'dojiStar': int64(input[97][a]), 
                                                                       'dragonFlyDoji': int64(input[98][a]), 
                                                                       'engulfing': int64(input[99][a]), 
                                                                       'eveningDojiStar': int64(input[100][a]), 
                                                                       'eveningStar': int64(input[101][a]), 
                                                                       'gapSideSideWhite': int64(input[102][a]), 
                                                                       'graveStoneDoji': int64(input[103][a]), 
                                                                       'hammer': int64(input[104][a]), 
                                                                       'hangingMan': int64(input[105][a]), 
                                                                       'harami': int64(input[106][a]), 
                                                                       'haramiCross': int64(input[107][a]), 
                                                                       'highWave': int64(input[108][a]), 
                                                                       'hikkake': int64(input[109][a]),  
                                                                       'hikkakeMod': int64(input[110][a]), 
                                                                       'homingPigeon': int64(input[111][a]), 
                                                                       'identical3Crows': int64(input[112][a]), 
                                                                       'inNeck': int64(input[113][a]), 
                                                                       'invertedHammer': int64(input[114][a]), 
                                                                       'kicking': int64(input[115][a]), 
                                                                       'kickingByLength': int64(input[116][a]), 
                                                                       'ladderBottom': int64(input[117][a]), 
                                                                       'longLeggedDoji': int64(input[118][a]), 
                                                                       'longLine': int64(input[119][a]), 
                                                                       'maruBozu': int64(input[120][a]), 
                                                                       'matchingLow': int64(input[121][a]), 
                                                                       'matHold': int64(input[122][a]), 
                                                                       'morningDojiStar': int64(input[123][a]), 
                                                                       'morningStar': int64(input[124][a]), 
                                                                       'onNeck': int64(input[125][a]), 
                                                                       'piercing': int64(input[126][a]), 
                                                                       'rickShawman': int64(input[127][a]), 
                                                                       'riseFall3Methods': int64(input[128][a]), 
                                                                       'seperatingLines': int64(input[129][a]), 
                                                                       'shootingStar': int64(input[130][a]), 
                                                                       'shortline': int64(input[131][a]), 
                                                                       'spinningTop': int64(input[132][a]), 
                                                                       'stalledPattern': int64(input[133][a]), 
                                                                       'stickSandwhich': int64(input[134][a]), 
                                                                       'takuri': int64(input[135][a]), 
                                                                       'tasukiGap': int64(input[136][a]), 
                                                                       'thrusting': int64(input[137][a]), 
                                                                       'triStar': int64(input[138][a]), 
                                                                       'unique3River': int64(input[139][a]), 
                                                                       'upsideGap2Crows': int64(input[140][a]), 
                                                                       'xSdieGap3Methods': int64(input[141][a])}))        
        write.write(example.SerializeToString())
        a = a+1
    
data = expandData(startTime="142007040000000", instrument= "EUR_USD", endTime="1420149840000000") 

packData(data)   
    
