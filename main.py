# ========================================
# 
# Py-ATIS
# (c) Fabio Ramirez Stern, 2023-2024
# 
# ========================================

# CONFIG

version = '0.1' # version number
owmAPIkey = 'YOUR-OWM-KEY' # OpenWeatherMap API key
wxapikey = 'YOUR-WX-KEY' # checkWXapi key
lgfilename = f'YOUR-LOG-NAME_LOG_{version}_' # Logfile name
atislocation = 'YOUR-LOCATION-STRING' # Location

# IMPORTS

#import RPi.GPIO as GPIO

from atis import *

import datetime
import time
import logging


# LOGGING
"""lgfilename = lgfilename + f'{datetime.datetime.now()}'
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG, filename=lgfilename)
logging.info(f'FRS-AGORA LOG {version}')"""


# ========================================

# SETUP

owm = OWM(owmAPIkey) # initiate OWM API
mgr = owm.weather_manager()

wxurl = "https://api.checkwx.com/metar/EDDF/" # WX API url

ICAOal = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo',
        'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-Ray', 'Yankee', 'Zulu']
letterc = 0


cATIS = createATIS()

print(cATIS[0])
print("\n=============================\n")
print(cATIS[1])

# ========================================
      
# RUNTIME

#while 1:
    #main()

#END
