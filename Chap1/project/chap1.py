# -*- coding:utf-8 -*-
import sys

type = sys.getfilesystemencoding()

def load_dict_from_file(filepath):
    _dict = {}
    try:
        with open(filepath,"r",encoding=type,errors="ignore") as dict_file:
            for line in dict_file:
                (key,value) = line.strip().split(",")
                _dict[key] = value

    except IOError as ioerr:
        print ("文件%s不存在" % (filepath))

    return _dict

def weather_help(promtString):
    print ("--- Version:PY101-04 v1.0; Author: CloudEdge ---")
    print (promtString)

def display_weather_history(weather_history):
    for key in weather_history.keys():
        print ("%s %s" % (key, weather_history[key]))

def update_weather_history(weather_history, city, weather):
    weather_history[city] = weather
    return weather_history

if __name__ == '__main__' :

    weather_dict = load_dict_from_file ('weather_info.txt')
    weather_histroy = {}
    promtString = "请输入中文城市名查询天气 \nHelp 帮助 \nHistory 查看历史文件 \nQuit 退出\n"
    # print (promtString)
    command = input(promtString)
    while command != "Quit" and command != "quit":
        if command == "Help" or command == "help":
            weather_help(promtString)
        elif command == "History" or command == "history":
            display_weather_history(weather_histroy)
        elif command in weather_dict.keys():
            print ("%s" % weather_dict[command])
            weather_histroy = update_weather_history(weather_histroy, command, weather_dict[command])
        else:
            print ("输入错误，请重新输入\n%s" % (promtString))
        command = input()
    