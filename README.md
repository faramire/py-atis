# Py-ATIS
A Python module to generate ATIS strings with Open Weather Map (OWM) and CheckWX (WX).

**THIS IS NOT TO BE USED IN REAL AVIATION!**  
ALWAYS USE OFFICIAL SOURCES FOR ACCURATE, UP TO DATE INFORMATION. CHECK YOUR LOCAL, UP TO DATE AIP FOR MORE INFORMATION.

I created this for a custom alarm that wakes me up in the morning with up to date weather information, but in the form of an ATIS. Hence it currently says "expect foot approach".

The current version generates a European/German style ATIS, following ICAO and local standards, as well as trying to mimic the ATIS of Frankfurt Main Airport (EDDF).
Further it uses metric wherever possible, ie. kilometers for visibility, hectopascals for QNH and degrees celsius for OAT/dewpoint.
Metric rules, but if I'm really bored, I might add an US style string.

## Dependencies
- You need an [OWM API](https://openweathermap.org/) key (free) and a [CheckWX API](https://www.checkwxapi.com/) key (also free).
- pyowm: (for OWM) ``pip install pyowm``
- requests: (for CheckWX) ``pip install requests``

## Example
You can use the provided example.py. You need the two API keys as well as the ICAO code of a nearby airport that is in CheckWX in order to get cloud heights (eg. OVC120), as OWM does not provide such information.

It will print out two ATIS, one that is designed to be read out by text-to-speech (TTL) and hence has digits written individually (eg. 1013 => 1 0 1 3), and another one that is meant to be read by a human.

Here is an example output:
```
This is Frankfurt information Alpha, time 2 2 5 0 Lima.
Runway in use: 2 5, expect foot approach.
Wind 2 0 0 degrees, 1 1 knots.
Visibility 1 0 kilometers.
Clouds  Overcast 1 3.
Temperature - 2, Dewpoint - 4.
QNH 1 0 0 6 hectopascal, transition level 7 0.
Information Alpha out.

=============================

This is Frankfurt information Alpha, time 2250 Lima.
Runway in use: 25, expect foot approach.
Wind 200 degrees, 11 knots.
Visibility 9999.
Clouds OVC013.
Temperature -2, Dewpoint -4.
QNH 1006 hectopascal, transition level 70.
Information Alpha out.
```
