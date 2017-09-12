# -*- coding:utf-8 -*-
import sys
import requests
import json
from requests.exceptions import ConnectionError

encoding_type = sys.getfilesystemencoding()

def weather_help():
    print("--天气通，基于和风 v5 API--Version 1.0 / Author：CloudEdge / Update:"
          "2017/9/1\n")
    print("请输入中文城市名进行天气查询\nhelp|Help|h|H\t帮助\nquit|Quit|q|Q\t"
          "退出程序\nhistory|History\t显示历史查询结果")


# 调用和风API V5，考虑了中英文字符混排
# 利用except捕捉部分key查询失败和网络查询失败的场景
def web_query(city):
    weather_url = 'https://free-api.heweather.com/v5/weather'
    payload = {'city': city, 'key': 'a0128998f2944f29974894dc432e74ca'}
    try:
        weather_req = requests.get(weather_url, payload)
        req = weather_req.json()
        # 错误返回值位 {'HeWeather5': [{'status': 'unknown city'}]}
        if req["HeWeather5"][0]["status"] != "ok":
            city_daily_weather = None
            print("未知城市名，请重新输入!")
        else:
            city_daily_weather = {
                    "今日天气":req["HeWeather5"][0]["daily_forecast"][1]["cond"]["txt_d"],
                    "最高温度":req["HeWeather5"][0]["daily_forecast"][1]["tmp"]["max"],
                    "最低温度":req["HeWeather5"][0]["daily_forecast"][1]["tmp"]["min"],
                    "风向":req["HeWeather5"][0]["daily_forecast"][1]["wind"]["dir"],
                    "空气质量":req["HeWeather5"][0]["aqi"]["city"]["qlty"],
                    "PM2.5":req["HeWeather5"][0]["aqi"]["city"]["pm25"]
                    }
    except ConnectionError as e:
        print("网络查询失败！%s" %e)
        city_daily_weather = None
    except KeyError as e:
        print("部分参数查询失败! %s"%e)
        city_daily_weather = None
    return city_daily_weather

# 判断是否为中文字符
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
    
#基于中文字符串长度填充半角空格，对齐中英文混排，中文占2位，英文占1位
def align_chinese(text,width,just = "left",padding = " "):
    stext = str(text)
    cn_count = 0
    for uchar in stext:
        if is_chinese(uchar):
            cn_count += 2
        else:
            cn_count += 1
    
    if cn_count <= width:        
        if just == "left":
            return  padding*(width-cn_count)+stext
        if just == "right":
            return stext+padding*(width-cn_count)
        if just == "center":
            return padding*int((width-cn_count)/2)+stext+padding*(int((width-cn_count)/2)+1)
    else:
        return stext

#进行中英文混排
def display_city_weather(city, city_weather):
    print("\n%s" %(align_chinese(city,10,"center","*")))
    for key in city_weather:
        print("%s:%s" %(align_chinese(key,10,"left"), align_chinese(city_weather[key],10,"right")))


def weather_history(history):
    for key in history:
        display_city_weather(key,history[key])

if __name__ == "__main__":
    
    command = input("请输入城市名进行天气查询:\t")
    history = {}
    while True:
        if command in ["help","Help","h","H"]:
            weather_help()
        elif command in ["quit","Quit","q","Q"]:
            break
        elif command in ["history","History"]:
            weather_history(history)
        else:
            city_weather = web_query(command)
            if city_weather != None:
                display_city_weather(command,city_weather)
                history[command] = city_weather
          
                
        command = input("请输入城市名进行天气查询:\t")
