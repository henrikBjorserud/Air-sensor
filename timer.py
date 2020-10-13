import time


def main():


    starttime = time.time()
    while True:
        print("tick")
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))






if __name__ == "__main__":
    main()
