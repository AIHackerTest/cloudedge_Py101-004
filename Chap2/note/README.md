~ 用于存放个人教程，建议使用 Jupyter Notebook 编写。

本章基础任务：完成一个在命令行界面下天气查询程序，实现以下功能：

输入城市名，返回该城市最新的天气数据；
输入指令，获取帮助信息（一般使用 h 或 help）；
输入指令，获取历史查询信息（一般使用 history）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
此外，提交任务时，还需包含：

软件使用说明书 README.md：能令其他同学根据说明书运行程序，使用所有功能。
个人教程：梳理相关技能点，教会六个月前的自己学编程。


了解什么是 API 后，是时候选择一个顺手的天气 API 来完成本章任务啦~

弱水三千，只取一瓢。互联网上有非常多的天气 API，那如何选择一个合适的 API ？

对于本任务，建议你在选择 API 时考虑以下问题：

是否有 Python 的 demo ？
使用上有哪些限制（比如要收费）？
数据源是否可靠？
...

选定了 API ，你就可以通过 Python 来和 API 进行交互啦。

requests 模块是你和 API 进行交互的主要工具。这是非常优秀的第三方网络模块，需要单独安装。安装好后，请你探索：

如何在程序中引入 requests 模块？
如何使用 requests 模块发送请求？
POST 和 GET 是什么意思？如何用 requests 模块发送 POST 或者 GET 请求？

给 API 发送请求后，就要考虑如何处理 API 返回的数据啦：

如何获得 API 返回的数据？
如何在 Python 中处理 JSON 数据？
JSON 的来历是什么？ 为什么绝大多数 API 都选择以 JSON 的方式传递数据？

JSON 是一种存储和交换文本信息的语法。它支持多种编程语言，也是目前最流行的数据交换方式。

想要了解更多关于 JSON 的信息，可以参考：

Introducing JSON
19.2. json — JSON encoder and decoder
JSON Response Content
嗯哼，至此，本章基础任务就完成得差不多啦。

进阶任务：玩转 API（选做）

如果你已完成基础任务，还可以继续探索：

之前只在输入城市名时查询天气，有没有可能指定时间，让程序定时查询天气？
选一个国内 API 和国外 API 分别进行调用，了解不同的调用姿势。更进一步，如果你来设计 API ，你会怎么设计？
给程序增加温度单位转换功能？


ch2 BGM 推荐：Kaishin

Kaishin (1988) S.E.N.S. | 神思者


请注意! 这是二十多年前的专辑! 听来没有任何的过气感觉!
因为其中的每首乐曲的所有旋律,多年来一直顽强的反复不断的出现在各种电视/电影/游戏/广告...的配乐中.

其 fans 早已认定 S.E.N.S 再也难以创新了,
但是,每年依旧在持续的出专辑! 虽然没有轰动,
但是,依然引用频率非常高!

这是为什么!? 因为 S.E.N.S 找到了一种世界音乐的核心 meme 结构,
可以打动所有民族/文化背景的人!

我们进行任何类型系统/软件开发时,也应该找到自个儿的一种思考/调试/增补代码的核心结构,
这样才能从容的感人...

~ CEO(Chief Evangelist Officer) 大妈

特别是 Felucca 这首乐曲, 当年大妈初中时, 在 达喀尔拉力赛 (The Paris Dakar Rally) 的电视转播中听中的惊为天人, 生生哼记下来旋律 11年后无意间才知道是来自日本的 S.E.N.S !


如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

字符	ASCII	Unicode	UTF-8
A	01000001	00000000 01000001	01000001
中	x	01001110 00101101	11100100 10111000 10101101
从上面的表格还可以发现，UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

rw-file-utf-8

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：

web-utf-8

所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的UTF-8编码。

字符串和编码

阅读: 895447
字符编码

我们已经讲过了，字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。

因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。

由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。

但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。

你可以想得到的是，全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。

char-encoding-problem

因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。

Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。

现在，捋一捋ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。

字母A用ASCII编码是十进制的65，二进制的01000001；

字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；

汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。

你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

字符	ASCII	Unicode	UTF-8
A	01000001	00000000 01000001	01000001
中	x	01001110 00101101	11100100 10111000 10101101
从上面的表格还可以发现，UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

rw-file-utf-8

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：

web-utf-8

所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的UTF-8编码。

Python的字符串

搞清楚了令人头疼的字符编码问题后，我们再来研究Python的字符串。

在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：

>>> print('包含中文的str')
包含中文的str
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
如果知道字符的整数编码，还可以用十六进制这么写str：

>>> '\u4e2d\u6587'
'中文'
两种写法完全是等价的。

由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

Python对bytes类型的数据用带b前缀的单引号或双引号表示：

x = b'ABC'
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：

>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

在bytes中，无法显示为ASCII字符的字节，用\x##显示。

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
要计算str包含多少个字符，可以用len()函数：

>>> len('ABC')
3
>>> len('中文')
2
len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：

>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。

由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：


JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

JSON is built on two structures:

A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.
These are universal data structures. Virtually all modern programming languages support them in one form or another. It makes sense that a data format that is interchangeable with programming languages also be based on these structures.

In JSON, they take on these forms:

An object is an unordered set of name/value pairs. An object begins with { (left brace) and ends with } (right brace). Each name is followed by : (colon) and the name/value pairs are separated by , (comma).



An array is an ordered collection of values. An array begins with [ (left bracket) and ends with ] (right bracket). Values are separated by , (comma).



A value can be a string in double quotes, or a number, or true or false or null, or an object or an array. These structures can be nested.



A string is a sequence of zero or more Unicode characters, wrapped in double quotes, using backslash escapes. A character is represented as a single character string. A string is very much like a C or Java string.



A number is very much like a C or Java number, except that the octal and hexadecimal formats are not used.



Whitespace can be inserted between any pair of tokens. Excepting a few encoding details, that completely describes the language.


***
- try except finally
try 来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即 except 语句块，执行完 except 后，如果有 finally 语句块，则执行finally 语句块。

***
with as
由于文件读写时都有可能产生 IOError，一旦出错，后面的 f.close()就
不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用 try ... finally 来实现：
try:
f = open('/path/to/file', 'r')
print(f.read())
finally:
if f:
f.close()
但是每次都这么写实在太繁琐，所以， Python 引入了 with 语句来自动帮我们调用 close()方法：
with open('/path/to/file', 'r') as f:
print(f.read())
这和前面的 try ... finally 是一样的，但是代码更佳简洁，并且不必调用 f.close()方法。

The "with" statement is used to wrap the execution of a block with
methods defined by a context manager (see section With Statement
Context Managers). This allows common "try"..."except"..."finally"
usage patterns to be encapsulated for convenient reuse.

   with_stmt ::= "with" with_item ("," with_item)* ":" suite
   with_item ::= expression ["as" target]

The execution of the "with" statement with one "item" proceeds as
follows:

1. The context expression (the expression given in the "with_item")
   is evaluated to obtain a context manager.

2. The context manager's "__exit__()" is loaded for later use.

3. The context manager's "__enter__()" method is invoked.

4. If a target was included in the "with" statement, the return
   value from "__enter__()" is assigned to it.

   Note: The "with" statement guarantees that if the "__enter__()"
     method returns without an error, then "__exit__()" will always be
     called. Thus, if an error occurs during the assignment to the
     target list, it will be treated the same as an error occurring
     within the suite would be. See step 6 below.

5. The suite is executed.

6. The context manager's "__exit__()" method is invoked.  If an
   exception caused the suite to be exited, its type, value, and
   traceback are passed as arguments to "__exit__()". Otherwise, three
   "None" arguments are supplied.

   If the suite was exited due to an exception, and the return value
   from the "__exit__()" method was false, the exception is reraised.
   If the return value was true, the exception is suppressed, and
   execution continues with the statement following the "with"
   statement.

   If the suite was exited for any reason other than an exception, the
   return value from "__exit__()" is ignored, and execution proceeds
   at the normal location for the kind of exit that was taken.


   ***
```
if __name__ == '__main__' :
```
- Automatically created module for IPython interactive environment

***
## JSON
JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired by JavaScript object literal syntax (although it is not a strict subset of JavaScript [1] ).

json exposes an API familiar to users of the standard library marshal and pickle modules.
JSON 表示的对象就是标准的 JavaScript 语言的对象

比XML 更快
JSON 标准规定 JSON 编码是 UTF-8

JSON类型    | Python类型
--|--
{}  |   dict
[]  |  list
"string"  | 'str'或u'unicode'
1234.56  |  int或float
true/false  |True/False
null  |  None



![](assets/markdown-img-paste-20170823145248214.png)
array类似python中list

![](assets/markdown-img-paste-20170823145357518.png)

string类似python中str
![](assets/markdown-img-paste-20170823145557210.png)
number类似python中int或float
![](assets/markdown-img-paste-20170823145627713.png)

最终的值为上述各对象的嵌套

![](assets/markdown-img-paste-20170823145715570.png)

```
json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
```
Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object) using this conversion table.

dump()方法可以直接把 JSON 写入一个 file-like Object

dumps()方法返回一个 str，内容就是标准的 JSON Object
即完成Python 对象到 JSON 格式的转换。准备序列化为标准格式，用于存储磁盘或网络传输
```
json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}'
# 完成python对象d 到json对象的转换

from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)

>>> io.getvalue()
'["streaming API"]'
# 将python对象转化为json对象写入文件对象IO
```
要把 JSON 反序列化为 Python 对象，用 loads()或者对应的 load()方法，
loads把 JSON 的字符串反序列化为python对象，load从 file-like Object 中读取字符串并反序列化为python对象：

If specified, separators should be an (item_separator, key_separator) tuple. The default is (', ', ': ') if indent is None and (',', ': ') otherwise. To get the most compact JSON representation, you should specify (',', ':') to eliminate whitespace.

```
>>> import json
>>> json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',', ':'))
'[1,2,3,{"4":5,"6":7}]'
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}
```
Python 的 dict 对象可以直接序列化为 JSON 的{}，不过，很多时候，我
们更喜欢用 class 表示对象，比如定义 Student 类，然后序列化：
把任意 class 的实例变为 dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))
同样的道理，如果我们要把 JSON 反序列化为一个 Student 对象实例，
loads()方法首先转换出一个 dict 对象，然后，我们传入的 object_hook
函数负责把 dict 转换为 Student 实例
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> print(json.loads(json_str, object_hook=dict2student))
***
list  []
Python内置的一种数据类型是列表：list。list是一种有序的集合
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名
字
tuple ()



***
request

```
>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()
{u'private_gists': 419, u'total_private_repos': 77, ...}

```

***
GET/POST

GET 方法
请注意，查询字符串（名称/值对）是在 GET 请求的 URL 中发送的：
/test/demo_form.asp?name1=value1&name2=value2

有关 GET 请求的其他一些注释：
GET 请求可被缓存
GET 请求保留在浏览器历史记录中
GET 请求可被收藏为书签
GET 请求不应在处理敏感数据时使用
GET 请求有长度限制
GET 请求只应当用于取回数据

POST 方法
请注意，查询字符串（名称/值对）是在 POST 请求的 HTTP 消息主体中发送的：
POST /test/demo_form.asp HTTP/1.1
Host: w3schools.com
name1=value1&name2=value2

有关 POST 请求的其他一些注释：
POST 请求不会被缓存
POST 请求不会保留在浏览器历史记录中
POST 不能被收藏为书签
POST 请求对数据长度没有要求



***
##PEP8
1 变量

常量 : 大写加下划线
USER_CONSTANT
对于不会发生改变的全局变量，使用大写加下划线。

私有变量 : 小写和一个前导下划线
_private_value
Python 中不存在私有变量一说，若是遇到需要保护的变量，使用小写和一个前导下划线。但这只是程序员之间的一个约定，用于警告说明这是一个私有变量，外部类不要去访问它。但实际上，外部类还是可以访问到这个变量。

内置变量 : 小写，两个前导下划线和两个后置下划线
__class__
两个前导下划线会导致变量在解释期间被更名。这是为了避免内置变量和其他变量产生冲突。用户定义的变量要严格避免这种风格。以免导致混乱。


2 函数和方法

总体而言应该使用，小写和下划线。但有些比较老的库使用的是混合大小写，即首单词小写，之后每个单词第一个字母大写，其余小写。但现在，小写和下划线已成为规范。

私有方法 ： 小写和一个前导下划线
def _secrete(self):
    print "don't test me."
这里和私有变量一样，并不是真正的私有访问权限。同时也应该注意一般函数不要使用两个前导下划线(当遇到两个前导下划线时，Python 的名称改编特性将发挥作用)。特殊函数后面会提及。

特殊方法 ： 小写和两个前导下划线，两个后置下划线

def __add__(self, other):
    return int.__add__(other)
这种风格只应用于特殊函数，比如操作符重载等。

函数参数 : 小写和下划线，缺省值等号两边无空格

def connect(self, user=None):
    self._user = user


3 类

类总是使用驼峰格式命名，即所有单词首字母大写其余字母小写。类名应该简明，精确，并足以从中理解类所完成的工作。常见的一个方法是使用表示其类型或者特性的后缀，例如:
SQLEngine
MimeTypes

对于基类而言，可以使用一个 Base 或者 Abstract 前缀
BaseCookie
AbstractGroup
class UserProfile(object):
    def __init__(self, profile):
        return self._profile = profile

    def profile(self):
        return self._profile


4 模块和包

除特殊模块 __init__ 之外，模块名称都使用不带下划线的小写字母。
若是它们实现一个协议，那么通常使用lib为后缀，例如:
import smtplib
import os
import sys


5 关于参数

5.1 不要用断言来实现静态类型检测
断言可以用于检查参数，但不应仅仅是进行静态类型检测。 Python 是动态类型语言，静态类型检测违背了其设计思想。断言应该用于避免函数不被毫无意义的调用。

5.2 不要滥用 *args 和 **kwargs
*args 和 **kwargs 参数可能会破坏函数的健壮性。它们使签名变得模糊，而且代码常常开始在不应该的地方构建小的参数解析器。


6 其他

6.1 使用 has 或 is 前缀命名布尔元素

is_connect = True
has_member = False

6.2 用复数形式命名序列

members = ['user_1', 'user_2']

6.3 用显式名称命名字典

person_address = {'user_1':'10 road WD', 'user_2' : '20 street huafu'}

6.4 避免通用名称
诸如 list, dict, sequence 或者 element 这样的名称应该避免。

6.5 避免现有名称
诸如 os, sys 这种系统已经存在的名称应该避免。


7 一些数字
一行列数 : PEP 8 规定为 79 列，这有些苛刻了。根据自己的情况，比如不要超过满屏时编辑器的显示列数。这样就可以在不动水平游标的情况下，方便的查看代码。

一个函数 : 不要超过 30 行代码, 即可显示在一个屏幕类，可以不使用垂直游标即可看到整个函数。
一个类 : 不要超过 200 行代码，不要有超过 10 个方法。
一个模块 不要超过 500 行。

疑问：字符串的表达f'
def show_weather(jd):
    temperature = jd['results'][0]['now']['temperature']
    text = jd['results'][0]['now']['text']
    code = jd['results'][0]['now']['code']
    weather = f'\n{order} 温度：{temperature}\n天气状况：{text}\n天气指数：{code}\n'


