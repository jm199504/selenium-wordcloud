from wordcloud import WordCloud
#设置噪声词
stopwords = {'工作职责':0,'任职要求':0,'职位描述':0,'岗位职责':0,'岗位描述':0,
             '岗位要求': 0,'熟悉':0,'任职资格':0,'职位要求':0,'本科以上学历':0}
with open ('java.txt') as fp:
    text = fp.read()
    #1.英文方块图
    #wordcloud = WordCloud().generate(text)
    #2.英文方块图--->改变背景(默认黑色背景)
    #wordcloud = WordCloud(background_color='white').generate(text)
    #3.中文方块图，要求指定字体，不然中文字体将无法正常显示(比如显示□□)
    # wordcloud = WordCloud(font_path='KAI_GB2312.TTF').generate(text)
    #4.中文方块图，指定关键词个数
    # wordcloud = WordCloud(font_path='KAI_GB2312.TTF',max_words=10).generate(text)
    #5.中文方块图，指定关键词的尺寸最大值
    # wordcloud = WordCloud(font_path='KAI_GB2312.TTF', max_font_size=60,stopwords=stopwords).generate(text)
    #6.中文方块图，设置噪声词（但是会覆盖原有默认噪声词）
    wordcloud = WordCloud(font_path='KAI_GB2312.TTF', stopwords=stopwords).generate(text)
    image = wordcloud.to_image()
    image.show()