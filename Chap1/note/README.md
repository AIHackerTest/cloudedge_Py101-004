~ 用于存放个人教程，建议使用 Jupyter Notebook 编写。
* 解决中文乱码：
系统使用UTF-8 
# -*- coding:utf-8 -*-
检查打开文件格式并采用相应的编码格式打开，一开始用了GBK等格式未果
import sys
type = sys.getfilesystemencoding()
open(filepath,"r",encoding=type,errors="ignore")


* 利用指定分隔符建立字典并回写的例程
def load_dict_from_file(filepath):
    _dict = {}
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split(':')
                _dict[key] = value
    except IOError as ioerr:
        print "文件 %s 不存在" % (filepath)
    
    return _dict

def save_dict_to_file(_dict, filepath):
    try:
        with open(filepath, 'w') as dict_file:
            for (key,value) in _dict.items():
                dict_file.write('%s:%s\n' % (key, value))
    except IOError as ioerr:
        print "文件 %s 无法创建" % (filepath)

* 主程序：
if __name__ == '__main__' :
    _dict = load_dict_from_file ('dict.txt')


* Open issue:Print函数奇怪的格式问题：
  print ("输入错误，请重新输入\n%s", promtString)  会导致换行后第二个字符串之前多一个空格
  采用print ("输入错误，请重新输入\n%s" % (promtString))搞定