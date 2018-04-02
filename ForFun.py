# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# 读取文本
text = open(path.join(d, '22.txt'), encoding='utf-8').read()

import jieba

# 结巴分词
wordlist = jieba.cut(text, cut_all=True)
wl = " ".join(wordlist)
print(wl)

coloring = np.array(Image.open(path.join(d, "14.jpg")))

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("Hangingter")


my_wordcloud = WordCloud(background_color="white", max_words=500, mask=coloring,
                         max_font_size=50, stopwords=stopwords, random_state=42, font_path='C:\Windows\Fonts\simfang.ttf')
my_wordcloud.generate(wl)
# 涂色
image_colors = ImageColorGenerator(coloring)

plt.imshow(my_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
