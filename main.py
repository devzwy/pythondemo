import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
import os  #导入os模块
import json
class BeautifulPicture():

    def __init__(self,i):  #类的初始化操作
        print(i)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  #给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://unsplash.com/napi/topics/spirituality/photos?page={}&per_page=200'.format(i)  #要访问的网页地址
        self.folder_path = '../images_wenwen'  #设置图片要存放的文件目录

    def get_pic(self):
        print('开始网页get请求:'+self.web_url)
        r = self.request(self.web_url)
        # for url in aa:
        #     print(url['urls']['raw'])
        # print('开始获取所有a标签')


        # jso = json.load(r.text)
        # soup = BeautifulSoup(r.text, 'lxml')
        # find = soup.find_all('a')
        # for a in find:
        #     print(a['href'])


        # all_a = BeautifulSoup(r.text, 'lxml').find_all('a')  #获取网页中的class为cV68d的所有a标签
        print('开始创建文件夹')
        self.mkdir(self.folder_path)  #创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path)   #切换路径至上面创建的文件夹

        for url in json.loads(r.text): #循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
            try:

                img_str = url['urls']['raw']  # a标签中完整的style字符串
                print('爬取图片内容：', img_str)
                # first_pos = img_str.index('"') + 1
                # second_pos = img_str.index('"', first_pos)
                # img_url = img_str[first_pos: second_pos]  # 使用Python的切片功能截取双引号之间的内容
                # # 获取高度和宽度的字符在字符串中的位置
                # width_pos = img_url.index('&w=')
                # height_pos = img_url.index('&q=')
                # width_height_str = img_url[width_pos: height_pos]  # 使用切片功能截取高度和宽度参数，后面用来将该参数替换掉
                # print('高度和宽度数据字符串是：', width_height_str)
                # img_url_final = img_url.replace(width_height_str, '')  # 把高度和宽度的字符串替换成空字符
                # print('截取后的图片的url是：', img_url_final)
                # # 截取url中参数前面、网址后面的字符串为图片名
                name_start_pos = img_str.index('photo')
                # name_end_pos = img_url.index('?')
                # img_name = img_url[name_start_pos: name_end_pos]

                print(img_str[name_start_pos+8:name_start_pos+8+20])
                self.save_img(img_str, img_str[name_start_pos+8:name_start_pos+8+20])  # 调用save_img方法来保存图片
            except:
                pass

    def save_img(self, url, name): ##保存图片
        print('下载图片到本地...')
        img = self.request(url)
        file_name = name + '.jpg'
        # print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name,'图片保存成功')
        f.close()

    def request(self, url):  #返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

for i in range(0,1000):
    beauty = BeautifulPicture(i)  #创建类的实例
    beauty.get_pic()  #执行类中的方法