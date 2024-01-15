"""Provides a framework to generate custom ATIS strings based on the OpenWeatherAPI and the WX API."""

# ========================================
# 
# Py-ATIS module
# github.com/faramire/py-atis/
# (c) Fabio Ramirez Stern, 2023-2024
# 
# ========================================

import time
import re # regex to query for clouds from the METAR
import requests # http requests for WX API (real METAR)

from pyowm import OWM # open weather map (OWM) API

ICAOal = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo',
        'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-Ray', 'Yankee', 'Zulu']

def rp(input_) -> str:
    """Radio Pronunciation: converts numbers into single individual digits for reading out radio style"""
    return ' '.join(str(input_))

def ATISstring(location, letterc_, atistime_, rwy_, expect_, TL_, windD_, windV_, vis_, clouds_, temp_, dew_, QNH_) -> str:
    """ATIS String: embeds all information into a ready string"""

    return f"""This is {location} information {ICAOal[letterc_]}, time {atistime_} Lima.
Runway in use: {rwy_}, {expect_}.
Wind {windD_} degrees, {windV_} knots.
Visibility {vis_}.
Clouds {clouds_}.
Temperature {temp_}, Dewpoint {dew_}.
QNH {QNH_} hectopascal, transition level {TL_}.
Information {ICAOal[letterc_]} out."""

def ATIStime() -> str:
    """ATIS Time: gets the local time for the ATIS"""
    return time.strftime('%H%M')

def TL(QNH_:int):
    """Transition Level: calculates the transition level based off the QNH"""
    if QNH_ <= 977:
        return 80
    elif QNH_ <= 1013:
        return 70
    elif QNH_ <= 1050:
        return 60
    else:
        return 50

def viscalc(vis_:int):
    """WIP! Visibility Calculation: rounds visibility and converts it into a radio ready string"""
    #if vis_ < 800:
    #    rtrn = vis_ if vis_ % 50 == 0 else vis_ + 50 - vis_ % 50 # rounds to 50
    if vis_ < 5000:
        rtrn = vis_ - vis_ % 100 # rounds to 100
    else:
        rtrn = vis_ - vis_ % 1000 # rounds to 1000
    
    if rtrn == 10000:
        return "1 0 kilometers"
    elif rtrn % 1000 == 0:
        return f'{rtrn} thousand' # full thousand
    else:
        return f'{rtrn//1000} thousand {rtrn//100} hundred' # thousand + hundred

def cloudsWX(wxurl_:str, wxapikey_:str):
    """gets cloud heights from airport via WX API"""

    response = requests.request("GET", wxurl_, headers={'X-API-Key': wxapikey_}).text
    if "CAVOK" in response:
        return [0, 'CAVOK'] # indicating its CAVOK and no clouds height there
    else:
        out_ = re.findall('(FEW...|SCT...|BKN...|OVC...)', response) # finds all cloud heights
        out_.insert(0, len(out_)) # undoes one layer of "array within array" (I think)
        return(out_)
    
def CLDS(api_:str) -> list[str]:
    """decodes the cloud heights from the CheckWX API"""

    if api_[0] == 0: # code indicating CAVOK
        return ['CAV OK', 'CAVOK']
    else:
        len_= len(api_) # how many cloud layers are in the array?
        ttsstr_ = '' # text to speech string
        normstr_ = ' '.join(api_[1:len_]) # readable string
        for i in range(1, len_): # do for as many cloud layers there are
            cov_ = str(api_[i])[:3] # the first three letters are the coverage amount
            alt_ = rp(str(api_[i][4:])) # from char 4 on are the heights
            match cov_:
                case 'SCT':
                    add = 'Scattered'
                case 'FEW':
                    add = 'Few'
                case 'BKN':
                    add = 'Broken'
                case 'OVC':
                    add = 'Overcast'
                case _:
                    add = 'error'
            ttsstr_ = ' '.join([ttsstr_, add, alt_])
        return [ttsstr_, normstr_]


def createATIS(wxurl_: str, wxapikey_: str, owmAPIkey_: str, atislocation_: str, rwy_: str, expect_: str, lat_: int, lon_: int, letterc_: int=0) -> list[str]:
    """Create ATIS: gets all information needed and generates two ATIS strings: TTS ready [0] and readible [1]"""

    owmATIS     = OWM(owmAPIkey_) # initiate OWM API
    mgrATIS     = owmATIS.weather_manager()

    atistime    = ATIStime()
    ol          = mgrATIS.one_call(lat=lat_, lon=lon_, exclude='minutely,hourly')
    QNH         = ol.current.pressure['press']
    tl          = TL(QNH)
    windD       = ol.current.wnd['deg']
    windV       = round(ol.current.wnd['speed'] * 1.94384)
    vis         = ol.current.visibility_distance
    clouds      = CLDS(cloudsWX(wxurl_, wxapikey_))
    temp        = round(ol.current.temp['temp'] - 273.15)
    dew         = round(ol.current.dewpoint - 273.15)

    atisTTS     = ATISstring(atislocation_, letterc_, rp(atistime), rp(rwy_), expect_, rp(tl), rp(windD), rp(windV), viscalc(vis), clouds[0], rp(temp), rp(dew), rp(QNH))
    atisNORM    = ATISstring(atislocation_, letterc_, atistime, rwy_, expect_, tl, windD, windV, vis, clouds[1], temp, dew, QNH)

    return [atisTTS, atisNORM]
