import pickle
import matplotlib.pyplot as plt

def plot(pm10, pm25):

    pm10 = [float(value) for value in pm10]
    pm25 = [float(value) for value in pm25]
    plt.plot(pm10, "b-,", label="PM10 (10µm)")
    plt.plot(pm25, "r-,", label="PM2,5 (2,5µm")
    plt.legend(loc="best")
    plt.title("Particle matter per cubic metre air, Olskroken:")
    plt.show()
 
def plot_pm10(pm10):

    pm10 = [float(value) for value in pm10]
    plt.plot(pm10)
    plt.title("pm10 in air, Olskroken:")
    plt.show()

def plot_pm25(pm25):

    pm25 = [float(value) for value in pm25]
    plt.plot(pm25)
    plt.title("pm2.5 in air, Olskroken:")
    plt.show()

def main():

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

    #plot_pm10(pm10)

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

    #plot_pm25(pm25)

    plot(pm10, pm25)

if __name__ == "__main__":
    main()
