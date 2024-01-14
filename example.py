# ========================================
# 
# Py-ATIS
# (c) Fabio Ramirez Stern, 2023-2024
# 
# ========================================

# CONFIG

owmAPIkey = 'YOUR-OWM-KEY' # OpenWeatherMap API key
wxapikey = 'YOUR-WX-KEY' # checkWXapi key
wxurl = 'https://api.checkwx.com/metar/XXXX/' # WX API url

atislocation = 'YOUR-LOCATION-STRING' # Location
rwy = '25' # rwy to be said in ATIS, as string!
expect = 'expect foot approach'
lat =  '12.34'
long = '56.78'

# IMPORTS

from atis import createATIS()

# ========================================

# SETUP

letterc = 0 # Alpha

# ========================================

# RUNTIME

cATIS = createATIS(wxurl, wxapikey, owmAPIkey, atislocation, rwy, lat, long, letterc)

print(cATIS[0])
print("\n=============================\n")
print(cATIS[1])

#END
