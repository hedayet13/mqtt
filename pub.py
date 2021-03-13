import paho.mqtt.publish as publish
MQTT_SERVER = "test.mosquitto.org"  #Write Server IP Address
MQTT_PATH = "Image1"

# while True:
#     f=open("img/res0.jpg", "rb") #3.7kiB in same folder
#     fileContent = f.read()
#     byteArr = bytearray(fileContent)
#     publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)

f=open("img/res0.jpg", "rb") #3.7kiB in same folder
fileContent = f.read()
byteArr = bytearray(fileContent)
publish.single(MQTT_PATH, byteArr, hostname=MQTT_SERVER)