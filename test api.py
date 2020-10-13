import requests
import json


#def jprint(obj):
    #create a formatted string of the Python JSON object
    #text = json.dumps(obj, sort_keys=True, indent=4)
    #print(text)



def main():



    response = requests.get("http://api.luftdaten.info/v1/sensor/15551/")





    #jprint(response.json())
    #print(response.json())
    #resp = response.json()
    #data = []

    #for i in resp:
    #    print(i["sensordatavalues"])
    #    for h, j in enumerate(i["sensordatavalues"]):
    #        print(j["value"], h+1)
    #        data.append(j["value"])

    #print(data)
    #print(data[0])
    #print(data[1])




if __name__ == "__main__":
    main()
