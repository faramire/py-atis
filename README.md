# Py-ATIS
A Python module to generate ATIS strings with Open Weather Map (OWM) and CheckWX (WX).

The current version generates a European/German style ATIS, following ICAO and local standards, as well as trying to mimic the ATIS of Frankfurt (EDDF).
Further it uses metric wherever possible, ie. kilometers for visibility, hectopascals for QNH and degrees celsius for OAT/dewpoint.
Metric rules, but if I'm really bored, I might add an US style string.

## Dependencies:
- You need an [OWM API](https://openweathermap.org/) key (free) and a [CheckWX API](https://www.checkwxapi.com/) key (also free).
- pyowm: (for OWM) ``pip install pyowm``
- requests: (for CheckWX) ``pip install requests``
