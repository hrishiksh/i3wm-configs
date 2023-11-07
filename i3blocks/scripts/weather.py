#!/bin/python3

import requests

response= requests.get("https://wttr.in/guwahati?format=j1")

weather_code_dict = {
    "113": ["Sunny","sunny"],
    "116": ["PartlyCloudy","cloudy"],
    "119": ["Cloudy","cloudy"],
    "122": ["VeryCloudy","cloudy"],
    "143": ["Fog","fog"],
    "176": ["LightShowers","rain"],
    "179": ["LightSleetShowers","rain"],
    "182": ["LightSleet","snow"],
    "185": ["LightSleet","snow"],
    "200": ["ThunderyShowers","thunderstorm"],
    "227": ["LightSnow","snow"],
    "230": ["HeavySnow","snow"],
    "248": ["Fog","fog"],
    "260": ["Fog","fog"],
    "263": ["LightShowers","rain"],
    "266": ["LightRain","rain"],
    "281": ["LightSleet","snow"],
    "284": ["LightSleet","snow"],
    "293": ["LightRain","rain"],
    "296": ["LightRain","rain"],
    "299": ["HeavyShowers","snow"],
    "302": ["HeavyRain","rain"],
    "305": ["HeavyShowers","rain"],
    "308": ["HeavyRain","rain"],
    "311": ["LightSleet","snow"],
    "314": ["LightSleet","snow"],
    "317": ["LightSleet","snow"],
    "320": ["LightSnow","snow"],
    "323": ["LightSnowShowers","rain"],
    "326": ["LightSnowShowers","rain"],
    "329": ["HeavySnow","snow"],
    "332": ["HeavySnow","snow"],
    "335": ["HeavySnowShowers","snow"],
    "338": ["HeavySnow","snow"],
    "350": ["LightSleet","snow"],
    "353": ["LightShowers","rain"],
    "356": ["HeavyShowers","rain"],
    "359": ["HeavyRain","rain"],
    "362": ["LightSleetShowers","rain"],
    "365": ["LightSleetShowers","rain"],
    "368": ["LightSnowShowers","snow"],
    "371": ["HeavySnowShowers","snow"],
    "374": ["LightSleetShowers","rain"],
    "377": ["LightSleet","snow"],
    "386": ["ThunderyShowers","thunderstorm"],
    "389": ["ThunderyHeavyRain","thunderstorm"],
    "392": ["ThunderySnowShowers","thunderstorm"],
    "395": ["HeavySnowShowers","snow"],
}

icons={
    "sunny": "",
    "cloudy":"",
    "fog":"",
    "rain":"",
    "snow":"",
    "thunderstorm":"",
    "others":""
}

def convert_weathercode_icon(weather_code):
    raw_icon_name = weather_code_dict[weather_code]
    icon = icons[raw_icon_name[1]]
    return icon


if response.ok:
    jsonResp=response.json()
    temperature= jsonResp["current_condition"][0]["temp_C"]
    feels_like=jsonResp["current_condition"][0]["FeelsLikeC"]
    wind_direction=jsonResp["current_condition"][0]["winddir16Point"]
    wind_direction_deg=jsonResp["current_condition"][0]["winddirDegree"]
    wind_speed=jsonResp["current_condition"][0]["windspeedKmph"]
    weather_code= jsonResp["current_condition"][0]["weatherCode"]
    weather_description=jsonResp["current_condition"][0]["weatherDesc"][0]["value"]
    

    print(f'{convert_weathercode_icon(weather_code)} {weather_description} : {temperature}°C ({feels_like}°C)  {wind_direction_deg}°{wind_direction} {wind_speed}Km/h')

