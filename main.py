import requests
import smtplib
import datetime
import json
import logging

with open('data.json', 'r') as json_file:
  data = json.load(json_file)
  my_email = data["my_email"]
  password = data["password"]
  recipient_mail = data["recipient_mail"]

def get_weather_data():
    response = requests.get(url="https://api.open-meteo.com/v1/forecast?latitude=50.088&longitude=14.4208&hourly=temperature_2m&daily=sunshine_duration&timezone=Europe%2FBerlin&forecast_days=1")
    response.raise_for_status()
    data = response.json()
    sunshine_duration_seconds = data["daily"]["sunshine_duration"][0]
    sunshine_duration_hours = sunshine_duration_seconds / 3600
    selected_temperatures = data["hourly"]["temperature_2m"][7:20] 
    average_temperature = round(sum(selected_temperatures) / len(selected_temperatures), 2) 
    return average_temperature, round(sunshine_duration_hours, 2)


def generate_message(average_temperature, sunshine_duration_hours):
    todays_date = datetime.date.today()
    today = todays_date.strftime("%d.%m.%Y")
    message = f"Hello! \nToday is {today}. \nThe average temperature for today is {average_temperature} C. \nSun will be shining for {sunshine_duration_hours} hours.\nHave a nice day!"
    return message


def send_email(message):
    connection = smtplib.SMTP('smtp.gmail.com',  587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_mail,
        msg=f"Subject:Weather Report\n\n{message}"
    )
    logging.info("Email sent")
    connection.close()


average_temperature, sunshine_duration_hours = get_weather_data()
message = generate_message(average_temperature, sunshine_duration_hours)
send_email(message)

