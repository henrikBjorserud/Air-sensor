import pickle
import requests
#import os
import time




def save_data(data):

    pm10 = data[0]
    pm25 = data[1]

    with open("pm10.dat", "ab") as pm10_file:
        pickle.dump(pm10, pm10_file)

    with open("pm25.dat", "ab") as pm25_file:
        pickle.dump(pm25, pm25_file)

    #print(os.stat("pm10.dat"))
    #print(os.stat("pm25.dat"))

def api_request():

    response = requests.get("http://api.luftdaten.info/v1/sensor/50643/")

    resp = response.json()
    data = []

    for i in resp:
        print(i["sensordatavalues"])
        for h, j in enumerate(i["sensordatavalues"]):
            print(j["value"], h + 1)
            data.append(j["value"])

    save_data(data)

def main():



    starttime = time.time()
    while True:
        print("tick")
        api_request()
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))


if __name__ == "__main__":
    main()
