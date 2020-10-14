import pickle
import requests
import time
import matplotlib.pyplot as plt

def plot(pm10, pm25):

    pm10 = [float(value) for value in pm10]
    pm25 = [float(value) for value in pm25]
    plt.plot(pm10, "b-,", label="PM10 (10µm)")
    plt.plot(pm25, "r-,", label="PM2,5 (2,5µm)")
    plt.ylabel("PM per m3")
    plt.xlabel("Minutes")
    plt.legend(loc="best")
    plt.title("Particle in the air, Olskroken:")
    plt.show()


def read_data_from_dat():
    pm10 = []
    pm25 = []

    with open("pm10.dat", "rb") as pm10_file:
        while True:
            try:
                i = pickle.load(pm10_file)
                pm10.append(i)
            except EOFError:
                break

    for i in pm10:
        print(i)

    print("--------------------------")

    with open("pm25.dat", "rb") as pm25_file:
        while True:
            try:
                i = pickle.load(pm25_file)
                pm25.append(i)
            except EOFError:
                break

    for i in pm25:
        print(i)

    plot(pm10, pm25)


def save_data(data):

    pm10_save = data[0]
    pm25_save = data[1]

    with open("pm10.dat", "ab") as pm10_file:
        pickle.dump(pm10_save, pm10_file)

    with open("pm25.dat", "ab") as pm25_file:
        pickle.dump(pm25_save, pm25_file)

    read_data_from_dat()


def api_request():

    response = requests.get("http://api.luftdaten.info/v1/sensor/50643/")   # 50643 is the id of my sensor

    resp = response.json()
    data = []

    for i in resp:
        print(i["sensordatavalues"])
        for h, j in enumerate(i["sensordatavalues"]):
            print(j["value"], h + 1)
            data.append(j["value"])

    save_data(data)

def main():

    start_time = time.time()

    while True:
        print("tick")
        api_request()

        time.sleep(150.0 - ((time.time() - start_time) % 150.0))


if __name__ == "__main__":
    main()
