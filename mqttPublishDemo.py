import paho.mqtt.publish as publish

publish.single("Hedayet/test","Hello",hostname="test.mosquitto.org")
publish.single("Hedayet/topic","World",hostname="test.mosquitto.org")

print('done')