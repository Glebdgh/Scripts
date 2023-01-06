from influxdb import InfluxDBClient
from datetime import datetime
import sys

try:
    client = InfluxDBClient(host='192.168.0.216', port=8086, database='test')
    client.create_database('test')
    print("Success!")
except:
    print("Failed!")

for client in client.get_list_database():
    print(client['name'])

json_body = [
    {
        "measurement" : "ter",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time" : datetime.now(),
        "fields": {
            'open' : 666.8,
            'close': 333.7
        }
    }
]

print(json_body)

client.write_points(json_body)

