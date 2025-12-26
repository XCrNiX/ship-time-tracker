import requests, json
from datetime import datetime
from timezonefinder import TimezoneFinder
import pytz

API_KEY = "API_KEY_SE_NE_PISE_OVDI"
MMSI = "UPISI_MMSI"

url = f"http://www.aishub.net/api/getlastposition?apiKey={API_KEY}&mmsi={MMSI}&format=json"
data = requests.get(url, timeout=20).json()[0]

lat = float(data["LATITUDE"])
lon = float(data["LONGITUDE"])

tf = TimezoneFinder()
tz_name = tf.timezone_at(lat=lat, lng=lon)
tz = pytz.timezone(tz_name)
now = datetime.now(tz)

hour = now.hour
call_ok = 8 <= hour <= 22

output = {
  "updated": now.isoformat(),
  "people": [
    {"name":"Miro","local_time":now.strftime("%H:%M"),"call_ok":call_ok},
    {"name":"Ivan","local_time":now.strftime("%H:%M"),"call_ok":call_ok},
    {"name":"Luka","local_time":now.strftime("%H:%M"),"call_ok":call_ok}
  ]
}

with open("data/status.json","w") as f:
  json.dump(output, f, indent=2)
