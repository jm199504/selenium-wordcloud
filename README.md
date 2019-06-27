**使用Selenium分析歌单评论**

<img src="https://github.com/jm199504/Selenium-WordCloud/blob/master/images/music.png" width = "300"/>

**涉及内容：**

1. 使用selenium 爬取网易云音乐歌单的评论内容
2. 使用pymysql 将评论内容存入MySQL保存
3. 使用jieba 对中文语句分词提取高频词
4. 使用wordcloud 做词云及可视化

**代码说明**

爬取音乐评论：selenium_music.py

词云及可视化：wordcloud_jieba.py

**自动化测试工具selenium**

一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。这个工具的主要功能包括：测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。测试系统功能——创建回归测试检验软件功能和用户需求。支持自动录制动作和自动生成 .Net、Java、Perl等不同语言的测试脚本。

（1）Selenium是开源的

（2）简单，易于安装，易于工作

（3）selenium ide是selenium的唯一可以在浏览器窗口上记录用户行为的组件

（4）除了火狐上的事件外不会记录你电脑上的任何其他事件

（5）Selenium支持多种浏览器，能够运行与多种操作系统，因此更容易帮助测试人员发现应用程序在不同浏览器上的兼容性问题。通过在不同浏览器中运行测试，更容易发现浏览器的不兼容性；

（6）通过编写模仿用户操作的 Selenium 测试脚本，可以从终端用户的角度来测试应用程序；可以操作 Web 页面上的各种元素，诸如：点击按钮、输入文本框，以及断言 Web 页面上存在某些文本与 Web 元素等.

（7）提供Selenium IDE ，一个FireFox plugin，能自动记录用户的操作，生成测试脚本。生成的测试脚本可以用Selenium Core手工执行，也能基于Selenium RC放入Java，C#，Ruby的单元测试用例中自动运行；

（8）测试用例调用实际的浏览器(如IE、FireFox)来执行测试。和有些开源方案自行实现 Web解释引擎相比，实际的浏览器能模拟更多用户交互和JS语法。

（9）SELENIUM录制的脚本比较灵活，因为它生成的是PERL的脚本程序。作为几乎最为强大和最广泛使用语言之一，PERL这种程序给予我最大的灵活性和控制度。

**安装库**

pip install selenium

pip install pymysql

**导入库**

from selenium import webdriver

**注意**

1. 爬取过程中建议使用time.sleep()操作，目的当然是模拟用户操作，因为用户实际操作中并不会像电脑那么快，这样能伪装身份，另外使用时间设置random.randint(x,y)使得每次等待时间不同，可以让伪装工作更升一级。

2. connect参数中charset为utf8mb4，而不是utf-8，使用utf-8存储过程中报错，原因来自于用户评论有表情包，而表情包只能存储为\\xF0的格式，mysql不能识别4个字节的utf8编码的字符，解决办法：将对应字符类型换成将对应的数据类型改为utf8mb4类型，同时连接类型也要改成utf8mb4_general_ci，注意mysql中对应表和字段字符设置utf8mb4，且在python代码连接中charset也要设置。

**中文分词工具Jieba**

- 支持三种分词模式：

  精确模式，试图将句子最精确地切开，适合文本分析；
  
  全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
  
  搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。

- 支持繁体分词

- 支持自定义词典

- 附上官网：https://amueller.github.io/word_cloud

**数据一览**

<img src="https://github.com/jm199504/Selenium-WordCloud/blob/master/images/db.png" width = "500" />

**效果图**

<img src="https://github.com/jm199504/Selenium-WordCloud/blob/master/images/result.png" width = "500" />
