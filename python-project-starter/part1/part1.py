import json
from datetime import datetime

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
    celsius = (temp_in_farenheit - 32) * 5/9
    c = round(celsius, 1)
    return(c)
# copy to process_weather nd return -> Ai to do
# open json file
with open ("data/forecast_5days_a.json") as json_file:
    json_data = json.load(json_file)
    no_day = 0
    lowest_min_temp = 0
    read_buffer = f"{no_day} Day Overview\n"
    read_buffer += f"    The lowest temperature will be {lowest_min_temp}, and will occur on Friday 19 June 2020.\n"
    read_buffer += f"    The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.\n"
    read_buffer += f"    The average low this week is 11.7°C.\n"
    read_buffer += f"    The average high this week is 20.1°C.\n"
    read_buffer += "\n"


    for i in range(5):
        day = json_data["DailyForecasts"][i]["Date"]
        day = convert_date(day)

        min_temp = json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
        min_temp = convert_f_to_c(min_temp)

        max_temp = json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
        max_temp = convert_f_to_c(min_temp)

        daytime_longPhrase = json_data["DailyForecasts"][i]["Day"]["LongPhrase"]

        daytime_chanceRain = json_data["DailyForecasts"][i]["Day"]["RainProbability"]

        nighttime_longPhrase = json_data["DailyForecasts"][i]["Night"]["LongPhrase"]

        nighttime_chanceRain = json_data["DailyForecasts"][i]["Night"]["RainProbability"]
        


        read_buffer += f"-------- {day} --------\n"
        read_buffer += f"Minimum Temperature: {min_temp}\n"
        read_buffer += "Maximum Temperature: 17.8°C\n"
        read_buffer += "Daytime: Sunshine mixing with some clouds\n"
        read_buffer += "    Chance of rain:  1%\n"
        read_buffer += "Nighttime: Clear\n"
        read_buffer += "    Chance of rain:  0%\n"
        read_buffer += "\n"
        print(read_buffer)


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# def convert_date(iso_string):
#     """Converts and ISO formatted date into a human readable format.
    
#     Args:
#         iso_string: An ISO date string..
#     Returns:
#         A date formatted like: Weekday Date Month Year
#     """
#     d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
#     return d.strftime("%A %d %B %Y")


# def convert_f_to_c(temp_in_farenheit):
#     """Converts an temperature from farenheit to celcius

#     Args:
#         temp_in_farenheit: integer representing a temperature.
#     Returns:
#         An integer representing a temperature in degrees celcius.
#     """
#     pass


def calculate_mean(total, num_items):
  
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    pass


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    pass


if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





