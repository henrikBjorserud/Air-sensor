Measuring the air quality where I live

This repo contains an attempt to build and
use my air sensor-device (airrohr), send data from said sensor 
to "http://api.luftdaten.info", retrieve that data and 
maybe store it and present it or just present it in a 
self-updating live-plot. Or both.

I built and installed the sensor-device on my balcony yesterday
(2020-10-13) and connected it to the luftdaten api.
It seems to be working as it should.
I followed these instructions: https://luftdata.se/assets/bygginstruktioner_lov-iot.pdf

The .dat will be created when user stops the program

I have now added a class called "Reading" av restructured everything

I added a photo of the air sensor to the repository. It was partly
soldered and partly glued with sparkly glue. 