Measuring the air quality where I live

This repo contains an attempt in progress to build an an 
air sensor-device (airrohr), send data from said sensor 
to "http://api.luftdaten.info", retrieve that data and 
maybe store it and present it or just present it in a 
self-updating live-plot. Or both.

I built and installed the sensor-device on my balcony yesterday
(2020-10-13) and connected it to the luftdaten api.
It seems to be working as it should.
I followed these instructions: https://luftdata.se/assets/bygginstruktioner_lov-iot.pdf

The .dat files contains data collected from 22.30 20-10-13 until
an unexpected connection error halted everything about six hours later.

Since last update everything is happening at once, the dat files are 
plotted and new values are added as soon as you run the "air quality.py".
Unfortunatly there will be many plots since I have not figured out
how to update the plots correctly.


Work to be done:

Error handling when connection is lost (saved the error messege in a txt for future reference)

Re-structuring the code (again)

Add unittest

Try to code the live-plot, or rather get the SciView-window to update rather than open ininite windows

Maybe adding a timestamp to the requests

Maybe adding a menu choice for writing, reading, live-plotting

Maybe adding a meter of sorts, so that one can se how dangererous the pm levels are to ones health right now
