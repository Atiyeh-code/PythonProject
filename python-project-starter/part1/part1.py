import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

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

def calculate_mean(total, num_items):
  
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = round((total / num_items), 1)
    return (mean)

def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    
    with open (forecast_file) as json_file:
        json_data = json.load(json_file)
        num_day = len(json_data["DailyForecasts"])

        lowest_min_temp = json_data["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]

        day_lowest_min_temp = json_data["DailyForecasts"][0]["Date"]

        highest_max_temp = json_data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]

        day_highest_max_temp = json_data["DailyForecasts"][0]["Date"]

        total_low_temp = 0
        avr_low_temp = 0

        total_high_temp = 0
        avr_high_temp = 0

        for i in range(num_day):
            if(lowest_min_temp > json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]):
                lowest_min_temp = json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
                day_lowest_min_temp = json_data["DailyForecasts"][i]["Date"]
            

            if(highest_max_temp < json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]):
                highest_max_temp = json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
                day_highest_max_temp = json_data["DailyForecasts"][i]["Date"]

            total_low_temp += json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
            total_high_temp += json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"] 
        
        avr_low_temp = calculate_mean(total_low_temp, num_day)  
        avr_low_temp = convert_f_to_c(avr_low_temp)
        avr_low_temp = format_temperature(avr_low_temp)       
  
        avr_high_temp = calculate_mean(total_high_temp, num_day)
        avr_high_temp = convert_f_to_c(avr_high_temp)
        avr_high_temp = format_temperature(avr_high_temp)

        lowest_min_temp = convert_f_to_c(lowest_min_temp)
        lowest_min_temp = format_temperature(lowest_min_temp)

        highest_max_temp = convert_f_to_c(highest_max_temp)
        highest_max_temp = format_temperature(highest_max_temp)

        day_lowest_min_temp = convert_date(day_lowest_min_temp)
        day_highest_max_temp = convert_date(day_highest_max_temp) 


        read_buffer = f"{num_day} Day Overview\n"
        read_buffer += f"    The lowest temperature will be {lowest_min_temp}, and will occur on {day_lowest_min_temp}.\n"
        read_buffer += f"    The highest temperature will be {highest_max_temp}, and will occur on {day_highest_max_temp}.\n"
        read_buffer += f"    The average low this week is {avr_low_temp}.\n"
        read_buffer += f"    The average high this week is {avr_high_temp}.\n"
        read_buffer += "\n"
      
        min_temp = 0
        max_temp = 0
        daytime_longPhrase = 0
        daytime_chanceRain = 0
        nighttime_longPhrase = 0
        nighttime_chanceRain = 0

        for i in range(num_day):
            day = json_data["DailyForecasts"][i]["Date"]
            day = convert_date(day)

            min_temp = json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
            min_temp = convert_f_to_c(min_temp)
            min_temp = format_temperature(min_temp)

            max_temp = json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
            max_temp = convert_f_to_c(max_temp)
            max_temp = format_temperature(max_temp)

            daytime_longPhrase = json_data["DailyForecasts"][i]["Day"]["LongPhrase"]
            daytime_chanceRain = json_data["DailyForecasts"][i]["Day"]["RainProbability"]

            nighttime_longPhrase = json_data["DailyForecasts"][i]["Night"]["LongPhrase"]
            nighttime_chanceRain = json_data["DailyForecasts"][i]["Night"]["RainProbability"]

            read_buffer += f"-------- {day} --------\n"
            read_buffer += f"Minimum Temperature: {min_temp}\n"
            read_buffer += f"Maximum Temperature: {max_temp}\n"
            read_buffer += f"Daytime: {daytime_longPhrase}\n"
            read_buffer += f"    Chance of rain:  {daytime_chanceRain}%\n"
            read_buffer += f"Nighttime: {nighttime_longPhrase}\n"
            read_buffer += f"    Chance of rain:  {nighttime_chanceRain}%\n"
            read_buffer += "\n"

    return(read_buffer)

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





