#--*codeing:utf-8
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import numpy
import PIL.Image as Image
stopwords = {'噪声词':0,'噪声词':0,'噪声词':0,}#可自定义过滤噪声词
def chinese_jieba(text):
    wordlist_jieba = jieba.cut(text)
    #注意：wordlist_jieba是list
    text_jieba = ''.join(wordlist_jieba)
    return text_jieba

with open ('gf_Chinese.txt') as fp:
    text = fp.read()
    text = chinese_jieba(text)
    mask_pic = numpy.array(Image.open('girl.png'))
    # font_path定义字体路径
    wordcloud = WordCloud(font_path='KAI_GB2312.TTF',background_color='white',max_font_size=130,mask=mask_pic,stopwords=stopwords,max_words=30).generate(text)
    # 用图片颜色填充
    image_colors = ImageColorGenerator(mask_pic)
    wordcloud.recolor(color_func=image_colors)
    # 生成图
    image = wordcloud.to_image()
    image.show()