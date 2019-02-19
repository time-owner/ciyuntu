import jieba
import matplotlib.pyplot as plt
from wordcloud import  WordCloud

with open(r'ciyuntu.txt') as f:
    text=' '.join(jieba.cut(f.read()))

wc=WordCloud(font_path='C:\Windows\Fonts\SIMLI.TTF',width=2000,height=1000,background_color='black').generate(text)

plt.imshow(wc)
plt.axis('off')
plt.show()
