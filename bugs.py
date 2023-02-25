import urllib.request
import urllib
import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/question/50426133/answer/483139994'
def get_soup(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup
def get_question_title(soup):
    title=soup.find_all('h1', class_='QuestionHeader-title')[0].text
    print('问题：{}'.format(title))

def get_hot_answer(soup):
    auther=soup.find_all('div', class_='AuthorInfo-content')[0]
    autherinfo=auther.find_all('a')[0].text
    print('回答者：{}'.format(autherinfo))
def get_img(soup):
    imglist=[]
    for item in soup.find_all('div', class_='QuestionAnswer-content'):
        figure=item.find_all('figure')
    for t0 in figure:
        t1=t0.find_all('img')
        for t2 in t1:
            t3=t2.get('src')
            imglist.append(t3)
  # 表示在整个网页中过滤出所有图片的地址，放在imglist中
    path = 'image'
    print(imglist)
    paths=''
  # 将图片保存到image文件夹中，如果没有image文件夹则创建
    if not os.path.isdir(path):
        os.makedirs(path)
        paths = path + '\\'  # 保存在image路径下
    else:
        paths='image'+'\\'
    idx = 1
    for imgurl in imglist:
        a = imgurl.startswith('http')
        if (a):
            urllib.request.urlretrieve(imgurl,'{0}{1}.png'.format(paths,idx))  # 打开imglist中保存的图片网址，并下载图片保存在本地，format格式化字符串
            idx = idx + 1
if __name__ == '__main__':
    soup=get_soup(url)
    get_question_title(soup)
    get_hot_answer(soup)
    get_img(soup)
