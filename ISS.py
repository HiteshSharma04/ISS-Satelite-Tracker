import requests 
import datetime as dt
import smtplib
import time

LAT = "Your Latitude"
LNG = "Your Longitude"
 
EMAIL = "Your Email"
PASSWORD = "Your Password"

def iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    long = float(data["iss_position"]["longitude"])
    lat = float(data["iss_position"]["latitude"])
    position = (long,lat)
    # print(position)
    place = {
        "lat" : LAT,
        "lng" : LNG,
        "formatted" : 0,
    }
    if LAT-5 <= lat <= LAT+5 and LNG-5 <= long <= LNG+5:
        return True


def night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=place)
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    rise = int(sunrise.split("T")[1].split(":")[0])
    sett = int(sunset.split("T")[1].split(":")[0])
    time = (rise,sett)
    # print(time)

    now = dt.datetime.now().hour
        # print(now)
    if now <= rise or now >= sett:
        return True

while True:
    time.sleep(60)
    if iss() and night():
        connect = smtplib.SMTP("smtp.gmail.com")
        connect.starttls()
        connect.login(user=EMAIL, password=PASSWORD)
        connect.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject : ISS \n\n watch the sky ISS is there")
        