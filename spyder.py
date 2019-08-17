import requests
import re
import os
import time

def craw_p(url_b,name):
    # 运行前先删除china文件夹，防止重复读
    html = []
    print("obtain HTML")
    # 通过useragent反爬
    agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.1.2.3000 Chrome/55.0.2883.75 Safari/537.36'

    for i in range(10):
        print("start！！")
        time.sleep(0.5)
        url = url_b + "page_" + str(i+1)+".html"
        print(url)
        header = {'user-agent': agent}
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = "utf-8"
        text = r.text
        # print(text)
        html_all = re.findall(r'<h3><a target="_blank" shape="rect" href="(.*?)">', text)
        print(len(html_all))
        for v in html_all:
            # print(i).encode("utf-8")
            html.append(v)
    print("end")
    print("page number : " + str(len(html)))
    r = 0
    for h in html:
        time.sleep(1)
        print("crawling")
        print(h)
        try:
            header = {'user-agent': agent}
            ri = requests.get("http:" + h, headers=header)
            ri.raise_for_status()
            ri.encoding = "utf-8"
            texti = ri.text
            # print(texti)
            try:
                title = re.findall(r'<h1 class="dabiaoti">(.*?)</h1>',texti)[0]
                times = re.findall(r'<div class="xinf-le">(.*?)</div>',texti)[0]
            except:
                title = re.findall(r'<title>(.*?)</title>',texti)[0]
                times = re.findall(r'<div class="xinf-le">(.*?)</div>',texti)[0]
            p2 = re.findall(r'(^[\u4e00-\u9fa5]|[^\x00-\xff].*?)</p>',texti)
            sum = ""
            for u in p2:
                u = u.replace("</strong>","").replace("<strong>","").replace("+attrObj+","").replace("&nbsp;","").replace("<span>","").replace("</span>","")
                sum = sum + u
            sum2 = re.findall(r"([\u4e00-\u9fa5]*?)",sum)
            summ = ""
            for y in sum2:
                summ = summ + y
            path = r"D:\\pythonSpider\\" + name +"\\" + times[0:10]
            if os.path.exists(path):
                print("exists")
                # continue
            else:
                os.makedirs(path)
            with open(r"D:\\pythonSpider\\" + name +"\\" + times[0:10] + "\\" + str(r) + ".txt","w",encoding="utf-8")as f:
                f.write(title)
                f.write("\n")
                f.write(summ)
                f.close()
            r = r+1
            print("finish")
        except:
            print("do not find")
    print("over!!!")


htmlall = ["http://china.chinadaily.com.cn/5bd5639ca3101a87ca8ff636/"]
f_name = ["china"]
for i in range(len(f_name)):
    craw_p(htmlall[i],f_name[i])
# 设置调用编码方式，以防乱码
with open('wc.py', 'r', encoding='utf-8') as f:
    exec(f.read())
