import paho.mqtt.client as mqtt
import group_5_util
import json

PORT = 1883
topic ='Data'

def on_message(client, userdata, message):
    decoded_message = message.payload.decode('utf-8')
    dict = json.loads(decoded_message)
    print(f"{topic}:")
    group_5_util.print_data(dict)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'sub')
client.connect('localhost', PORT)
client.subscribe(topic)
print(f"Subscribed to: {topic}")
client.on_message = on_message

client.loop_forever()