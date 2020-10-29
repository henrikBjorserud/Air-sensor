
class Sensors:
    def __init__(self, place, sensor_type, number):

        self.place = place
        self.sensor_type = sensor_type
        self.number = number

    def concatenate(self):
        return "http://api.luftdaten.info/v1/sensor/" + self.number + "/"

sensor_1 = Sensors("Henrik´s balcony", "pm", "50643")
sensor_2 = Sensors("Henrik´s balcony", "temp", "50644")
sensor_3 = Sensors("Lunden", "pm", "48076")
sensor_4 = Sensors("Lunden", "temp", "48077")
sensor_5 = Sensors("Strömmenberg", "pm", "19599")
sensor_6 = Sensors("Strömmensberg", "temp", "19600")
