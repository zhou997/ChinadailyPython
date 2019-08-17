import os
import importlib
import sys
from wordcloud import WordCloud
# 自行修改日期
for filename in os.listdir("D:/pythonSpider/china/2019-08-16"):
    print("D:/pythonSpider/china/2019-08-16/" + filename)
    importlib.reload(sys)
    # sys.setdefaultencoding('gbk')
    with open("D:/pythonSpider/china/2019-08-16/" + filename, encoding='utf-8', errors='ignore') as f:
        # lines = f.readlines()
        # f.close()

        for line in f.readlines():
            print(line)
            # with open("D:/pythonSpider/china/2019-08-12/词库.txt", "a",encoding='ISO-8859-1') as mom:
            with open("D:/pythonSpider/china/2019-08-16/词库.txt", "a", encoding='utf-8', errors='ignore') as mom:
                mom.write(line)

import jieba

f = open("D:/pythonSpider/china/2019-08-16/词库.txt", 'r', encoding='utf-8')
txt = f.read()
f.close()
words = jieba.lcut(txt)
print(words)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

mytext = " ".join(words)
# wordcloud默认不支持中文，自行设置字体
font = 'C:\Windows\Fonts\msyh.ttc'
wordcloud = WordCloud(background_color="white",
                      font_path=font,
                      width=1920, height=1080, margin=2).generate(mytext)
import matplotlib.pyplot as plt

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
