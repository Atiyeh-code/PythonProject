import json
from datetime import datetime
import plotly.express as px


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    celsius = ((temp_in_farenheit - 32) * 5 / 9)
    celsius = round(celsius, 1)
    return(celsius)
    
    
day_list =[]
min_temp_list =[]
max_temp_list =[]
min_real_feel_list=[]
min_real_feel_shade_list=[]


with open ("data/forecast_8days.json") as json_file:
    json_data = json.load(json_file)
    num_day = len(json_data["DailyForecasts"])

    for i in range(num_day):
        day = json_data["DailyForecasts"][i]["Date"]
        day = convert_date(day)
        day_list.append(day)

        min_temp = json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
        min_temp = convert_f_to_c(min_temp)
        min_temp_list.append(min_temp)


        max_temp = json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
        max_temp = convert_f_to_c(max_temp)
        max_temp_list.append(max_temp)

        min_real_feel = json_data["DailyForecasts"][i]["RealFeelTemperature"]["Maximum"]["Value"]
        min_real_feel = convert_f_to_c(min_real_feel)
        min_real_feel_list.append(min_real_feel)

        min_real_feel_shade = json_data["DailyForecasts"][i]["RealFeelTemperatureShade"]["Maximum"]["Value"]
        min_real_feel_shade = convert_f_to_c(min_real_feel_shade)
        min_real_feel_shade_list.append(min_real_feel_shade)

df =  {
    "day": day_list,
    "min_temp": min_temp_list ,
    "max_temp": max_temp_list
}      

fig = px.line(
    df,
    x = "day",
    y = ["min_temp", "max_temp"],
    title = "Forecast Graph1"
)

fig.show()

df =  {
    "day" : day_list,
    "min_temp" : min_temp_list,
    "min_real_feel" : min_real_feel_list,
    "min_real_feel_shade" : min_real_feel_shade_list
    }        

fig = px.line(
    df,
    x = "day",
    y = ["min_temp", "min_real_feel", "min_real_feel_shade" ],
    title = "Forecast Graph2"
)

fig.show()





