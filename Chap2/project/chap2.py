# -*- coding:utf-8 -*-
import sys
import requests
import json


encoding_type = sys.getfilesystemencoding()

def load_city_from_file(filepath):
    _dict = {}
    try:
        with open(filepath,"r",encoding=encoding_type,errors="ignore") as dict_file:
            for line in dict_file:
                (key,value) = line.strip().split(",")
                _dict[key] = value

    except IOError as ioerr:
        print ("\t文件%s不存在" % (filepath))
        _dict = None
        
    return _dict

def weather_help(promtstring):
    print ("---CityWeather Version: v1.0; Author: CloudEdge ---\n")
    print (promtstring)

def display_weather_history(weather_history):
    for key in weather_history.keys():
        print ("%s %s" % (key, weather_history[key]))

def update_weather_history(weather_history, city, weather):
    weather_history[city] = weather
    return weather_history


def query_weather_from_web(city):
    weather_url = 'https://free-api.heweather.com/v5/weather'
    payload = {'city': city, 'key': 'a0128998f2944f29974894dc432e74ca'}
    try:
            weather_req = requests.get(weather_url, params=payload)
            city_daily_weather = weather_req.json()["HeWeather5"][0]["daily_forecast"][1]["cond"]["txt_d"]
    
    except IOError as ioerr:
        print ("\t网络查询失败")
        city_daily_weather = None
        
    return city_daily_weather

if __name__ == '__main__' :

    weather_dict = load_city_from_file ('weather_info.txt')
    if weather_dict != None:
        weather_histroy = {}
        promt_string = "\t请输入中文城市名查询天气 \n\tHelp|help|H|h\t帮助 \n\tHistory|history\t查看历史文件 \n\tQuit|quit|Q|q\t退出\n"
        command = input(promt_string+">>>")
        while True:
            if command in ["Quit","quit","Q","q"]:
                break
            elif command in ["Help","help","H","h"]:
                weather_help(promt_string)
            elif command in [ "History",  "history"]:
                display_weather_history(weather_histroy)
            elif command in weather_dict.keys():
                city_weather = query_weather_from_web(command)
                if city_weather == None:
                    break
                else:
                    print ("---%s\n" % city_weather)
                    weather_dict[command] = city_weather
                    weather_histroy = update_weather_history(weather_histroy, command, weather_dict[command]) 
            else:
                print ("\t输入错误，请重新输入:-(\n%s" % (promt_string))
            command = input(">>>")
    else:
        print ("天气查询失败")
