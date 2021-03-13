import paho.mqtt.client as mqtt

def on_connect(client, userdata,flags, rc):
    print("Connect" + str(rc))
    client.subscribe("image") 

def on_message(client, userdata, msg):
    # print "Topic : ", msg.topic
    print(msg.topic+" "+str(msg.payload))
    f = open("/tmp/output.jpg", "w")  #there is a output.jpg which is different
    f.write(msg.payload)
    # f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()