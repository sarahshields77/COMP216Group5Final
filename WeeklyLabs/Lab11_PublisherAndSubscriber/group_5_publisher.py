import paho.mqtt.client as mqtt
import json
import time
import group_5_util

PORT = 1883
topic ='Data'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'pub')
client.connect('localhost', PORT)

for _ in range(5):
    data = group_5_util.create_data()
    string = json.dumps(data)
    client.publish(topic, string)
    print(f"Published: {string}")
    time.sleep(1)

client.disconnect()