import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 42.697708
MY_LONG = 23.321867


def is_iss_overhead():
    url_iss = 'http://api.open-notify.org/iss-now.json'
    data = requests.get(url_iss)
    longitude = data.json()['iss_position']['longitude']
    latitude = data.json()['iss_position']['latitude']

    if MY_LAT - 5 <= longitude <= MY_LAT + 5 and MY_LONG <= latitude <= MY_LONG + 5:
        return True


def is_night():
    url_sunrise_sunset = 'http://api.subrise-sunset.org/json'
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url_sunrise_sunset, params=parameters)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset <= time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login('<EMAIL>', '<PASSWORD>')
        connection.sendmail(
            from_addr='<EMAIL>',
            to_addrs='<EMAIL>',
            msg="Subject:Look up\n\nThe ISS is above you in the sky."
        )

