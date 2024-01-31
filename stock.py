from include import *

def stock_orange():
    orange = yf.Ticker("ORAN")
    return (orange.info.get('currentPrice'))

def stock_airbus():
    airbus = yf.Ticker("AIR.PA")
    return (airbus.info.get('currentPrice'))

def stock_peugeot():
    peugeot = yf.Ticker("UG.PA")
    return (peugeot.info.get('currentPrice'))

def stock_renault():
    renault = yf.Ticker("RNO.PA")
    return (renault.info.get('currentPrice'))

def stock_societe_generale():
    societe_generale = yf.Ticker("GLE.PA")
    return (societe_generale.info.get('currentPrice'))

def stock_bnp_paribas():
    bnp_paribas = yf.Ticker("BNP.PA")
    return (bnp_paribas.info.get('currentPrice'))

def stock_credit_agricole():
    credit_agricole = yf.Ticker("ACA.PA")
    return (credit_agricole.info.get('currentPrice'))

def stock_saint_gobain():
    saint_gobain = yf.Ticker("SGO.PA")
    return (saint_gobain.info.get('currentPrice'))

def stock_schneider_electric():
    schneider_electric = yf.Ticker("SU.PA")
    return (schneider_electric.info.get('currentPrice'))

def stock_engie():
    engie = yf.Ticker("ENGI.PA")
    return (engie.info.get('currentPrice'))

def stock_total():
    total = yf.Ticker("FP.PA")
    return (total.info.get('currentPrice'))

def stock_sanofi():
    sanofi = yf.Ticker("SAN.PA")
    return (sanofi.info.get('currentPrice'))

def stock_vinci():
    vinci = yf.Ticker("DG.PA")
    return (vinci.info.get('currentPrice'))

def stock_bouygues():
    bouygues = yf.Ticker("EN.PA")
    return (bouygues.info.get('currentPrice'))

def stock_atos():
    atos = yf.Ticker("ATO.PA")
    return (atos.info.get('currentPrice'))

def stock_publicis():
    publicis = yf.Ticker("PUB.PA")
    return (publicis.info.get('currentPrice'))

def stock_accor():
    accor = yf.Ticker("AC.PA")
    return (accor.info.get('currentPrice'))

def stock_alstom():
    alstom = yf.Ticker("ALO.PA")
    return (alstom.info.get('currentPrice'))

def stock_arcelor_mittal():
    arcelor_mittal = yf.Ticker("MT.AS")
    return (arcelor_mittal.info.get('currentPrice'))

def stock_lvma():
    lvma = yf.Ticker("MC.PA")
    return (lvma.info.get('currentPrice'))

def stock_lvmh():
    lvmh = yf.Ticker("RI.PA")
    return (lvmh.info.get('currentPrice'))