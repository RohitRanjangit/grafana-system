from datetime import date, datetime
from time import sleep
from influxdb import InfluxDBClient
import psutil

client = InfluxDBClient()
client.create_database('system')
client.switch_database('system')

def get_points():
    points = [
        {
            "measurement": "cpu",
            "tags": {
                "machine":'bullst'
            },
            "time": datetime.utcnow().isoformat('T')+'Z',
            "fields": {
                "cpu_load":psutil.cpu_percent()
            }
        },
        {
            "measurement": "ram",
            "tags": {
                "machine":'bullst'
            },
            "time": datetime.utcnow().isoformat('T')+'Z',
            "fields": {
                "ram_usage":psutil.virtual_memory().percent
            }
        }
    ]
    return points

while True:
    client.write_points(get_points())
    client.write_points(get_points())
    sleep(1)

