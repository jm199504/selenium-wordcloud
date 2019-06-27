import random
from math import ceil
import pymysql
import time
from selenium import webdriver
def start_spider(url):
    # 启动 Chrome 浏览器并访问指定URL
    brower = webdriver.Chrome()
    brower.get(url)
    # 等待 5 秒, 让评论数据加载完成
    time.sleep(5)
    # 页面嵌套一层 iframe, 必须切换到 iframe, 才能定位的到 iframe 里面的元素
    iframe = brower.find_element_by_class_name('g-iframe')
    brower.switch_to.frame(iframe)
    # 获取评论总数
    new_comments = brower.find_elements_by_xpath("//h3[@class='u-hd4']")[1]
    max_page = get_max_page(new_comments.text)
    current = 1
    is_first = True
    while current <= max_page:
        print('正在爬取第', current, '页的数据')
        if current == 1:
            is_first = True
        else:
            is_first = False
        data_list = get_comments(is_first, brower)
        time.sleep(2)
        go_nextpage(brower)
        time.sleep(random.randint(8, 12))
        current += 1
    print(data_list)

def get_max_page(new_comments):
    # 计算出总子页数
    print('=== ' + new_comments + ' ===')
    max_page = new_comments.split('(')[1].split(')')[0]
    # 每页显示 20 条评论
    offset = 20
    max_page = ceil(int(max_page) / offset)
    print('一共有', max_page, '个子页')
    return max_page

def get_comments(is_first, brower):
    # 获取评论内容
    items = brower.find_elements_by_xpath("//div[@class='cmmts j-flag']/div[@class='itm']")
    # 首页的数据中包含 15 条精彩评论, 20 条最新评论, 只保留最新评论
    if is_first:
        items = items[15: len(items)]
    data_list = list()
    data = dict()
    for each in items:
        # 用户 Id
        userId = each.find_elements_by_xpath("./div[@class='head']/a")[0]
        userId = userId.get_attribute('href').split('=')[1]
        # 用户昵称
        nickname = each.find_elements_by_xpath("./div[@class='cntwrap']/div[1]/div[1]/a")[0]
        nickname = nickname.text
        # 评论内容
        content = each.find_elements_by_xpath("./div[@class='cntwrap']/div[1]/div[1]")[0]
        content = content.text.split('：')[1]  # 中文冒号分割
        # 点赞数
        like = each.find_elements_by_xpath("./div[@class='cntwrap']/div[@class='rp']/a[1]")[0]
        like = like.text
        if like:
            like = like.strip().split('(')[1].split(')')[0]
        else:
            like = '0'
        # 头像地址
        avatar = each.find_elements_by_xpath("./div[@class='head']/a/img")[0]
        avatar = avatar.get_attribute('src')
        data['userId'] = userId
        data['nickname'] = nickname
        data['content'] = content
        data['like'] = like
        data['avatar'] = avatar
        cursor.executemany("INSERT INTO wy_single_mu (userId,nickname,content,likenum,avatar)VALUES(%s,%s,%s,%s,%s)",
                           [(userId,nickname,content,like,avatar)])
        conn.commit()
        data_list.append(data)
        data = dict()
    return data_list

def go_nextpage(brower):
    # 点击下一页 操作
    next_button = brower.find_elements_by_xpath("//div[@class='m-cmmt']/div[3]/div[1]/a")[-1]
    js = "var q=document.documentElement.scrollTop=10000"
    brower.execute_script(js)
    if next_button.text == '下一页':
        next_button.click()

if __name__ == '__main__':
    url = 'https://music.163.com/#/playlist?id=2232237850'
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Guojunming423', db='music', charset='utf8mb4')
    cursor = conn.cursor()
    start_spider(url)
    cursor.close()
    conn.close()