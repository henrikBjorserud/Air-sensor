import pickle
import time
import matplotlib.pyplot as plt
import requests
import Sensors


def plot(data, place):

    pm10 = [float(value[0]) for value in data]
    pm25 = [float(value[1]) for value in data]
    plt.plot(pm10, "b-,", label="PM10 (10µm)")
    plt.plot(pm25, "r-,", label="PM2,5 (2,5µm)")
    plt.ylabel("PM per m3")
    plt.xlabel("Minutes")
    plt.legend(loc="best")
    plt.title("Particles in the air, " + place)
    plt.show()


def read_data_from_dat(place):

    dat_data = []
    str(place)

    with open("particle_matter.dat", "rb") as pm_file:
        while True:
            try:
                i = pickle.load(pm_file)
                dat_data.append(i)
            except EOFError:
                break

    temp = (dat_data[-1])

    print("Outside temperature in " + place + " right now: " + temp[-1] + " degrees celsius")
    plot(dat_data, place)


def save_data(data):

    with open("particle_matter.dat", "ab") as particle_matter_file:
        pickle.dump(data, particle_matter_file)


def parse_json(pm_sensor, temp_sensor):

    data_parse = []
    temp_parse = []

    for i in pm_sensor:
        # print(i["sensordatavalues"])
        for h, j in enumerate(i["sensordatavalues"]):
            # print(j["value"], h + 1)
            data_parse.append(j["value"])

    for i in temp_sensor:
        # print(i["sensordatavalues"])
        for j in (i["sensordatavalues"]):
            # print(j["value"])
            temp_parse.append(j["value"])

    data = [data_parse[0], data_parse[1], temp_parse[0]]

    save_data(data)


def api_request(pm, temp):

    response = requests.get(pm)

    pm_sensor = response.json()

    response_2 = requests.get(temp)

    temp_sensor = response_2.json()

    parse_json(pm_sensor, temp_sensor)


def main():

    print("Which sensor would you like to take readings from? \n"
          "[1] Henrik´s sensor in Lunden \n"
          "[2] The other sensor in Lunden \n"
          "[3] The sensor in Strömmensberg \n"
          )

    choice = int(input("Enter your choice, [1]-[4]:"))

    if choice == 1:
        while True:

            start_time = time.time()

            api_request(Sensors.sensor_1.concatenate(), Sensors.sensor_2.concatenate())

            read_data_from_dat(Sensors.sensor_1.place)

            time.sleep(150.0 - ((time.time() - start_time) % 150.0))

    elif choice == 2:
        while True:
            start_time = time.time()

            api_request(Sensors.sensor_3.concatenate(), Sensors.sensor_4.concatenate())

            read_data_from_dat(Sensors.sensor_3.place)

            time.sleep(150.0 - ((time.time() - start_time) % 150.0))

    elif choice == 3:
        while True:
            start_time = time.time()

            api_request(Sensors.sensor_5.concatenate(), Sensors.sensor_6.concatenate())

            read_data_from_dat(Sensors.sensor_6.place)

            time.sleep(150.0 - ((time.time() - start_time) % 150.0))


if __name__ == "__main__":
    main()
