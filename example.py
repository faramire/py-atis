# ========================================
# 
# Py-ATIS module
# github.com/faramire/py-atis/
# (c) Fabio Ramirez Stern, 2023-2024
# 
# ========================================

# CONFIG

owmAPIkey = 'YOUR-OWM-KEY' # OpenWeatherMap API key
wxapikey = 'YOUR-WX-KEY' # checkWXapi key
icaoCode = 'XXXX' # ICAO airport code

atislocation = 'YOUR-LOCATION-STRING' # Location
rwy = '25' # rwy to be said in ATIS, as string!
expect = 'expect foot approach'
lat = 12.34
lon = 56.78

# IMPORTS

from atis import createATIS()

# ========================================

# SETUP

letterc = 0 # Alpha
wxurl = f'https://api.checkwx.com/metar/{icaoCode}/' # WX API url

# ========================================

# RUNTIME

cATIS = createATIS(wxurl_=wxurl, wxapikey_=wxapikey, owmAPIkey_=owmAPIkey, atislocation_=atislocation, rwy_=rwy, lat_=lat, lon_=lon, letterc_=letterc)

print(cATIS[0])
print("\n=============================\n")
print(cATIS[1])

#END
