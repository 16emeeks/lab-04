"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""
#Elliott Meeks

import paho.mqtt.client as mqtt
import time
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    
    client.publish("emeeks/ping", f"{num}")
    
    #client.subscribe("emeeks/ping")
    client.subscribe("emeeks/pong")
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("emeeks/pong", on_message_from_pong)
   
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))


def on_message_from_pong(client, userdata, msg):
    num = str(msg.payload, "utf-8")
    print("Custom callback - topic: " + msg.topic + "   msg: " + num)
    num2 = int(num)+1
    client.publish("emeeks/ping", f"{num2}")
    time.sleep(1)

num = 1;
if __name__ == '__main__':
    """your code here"""
    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    client.connect(host="172.20.10.2", port=1883, keepalive=60)
    
    client.loop_forever()
        
        
        
        
        
        
