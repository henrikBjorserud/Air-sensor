Measuring the air quality where I live

This repo contains an attempt in progress to build an an 
air sensor-device (airrohr), send data from said sensor 
to "http://api.luftdaten.info", retrieve that data and 
maybe store it and present it or just present it in a 
self-updating live-plot. Or both.

I built and installed the sensor-device on my balcony yesterday
(2020-10-13) and connected it to the luftdaten api.
It seems to be working as it should.

The .dat files contains data collected from 22.30 20-10-13 until
an unexpected connection error halted everything about six hours later.

Work to be done:

Error handling when connection is lost

Re-structuring the code (again)

Add unittest

Try to code the live-plot

Maybe adding a timestamp to the requests

Maybe adding a menu choice for writing, reading, live-plotting 
