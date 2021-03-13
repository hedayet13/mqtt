import paho.mqtt.client as mqtt
import ftplib

def on_connect(client,userdata,flags,rc):
    print("Connected with result code"+str(rc))
    client.subscribe("Hedayet/test")
    # client.subscribe("Hedayet/topic")

def on_message(client,userdata,msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload == "Hello":
        # print("Receive messaage #1")
        session =ftplib.FTP('ftpupload.net','epiz_28058617','Wd99Jczzl4')
        file = open('img/res3.jpg','rb')
        session.storbinary('STOR /htdocs/image.jpg',file)
        print("Image send")


    if msg.payload =="World":
        print("Received message #2")
    # else:
    #     print("Good Bye")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message= on_message

client.connect("test.mosquitto.org",1883,60)

client.loop_forever()