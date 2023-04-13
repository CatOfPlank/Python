# coding=gb2312
# coding = utf-8
# jieba分词程序
# 2023.4.10
import csv
import jieba
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 加载数据
# job_data = pd.read_csv('result1-1.csv')
# hunters_data = pd.read_csv('result1-2.csv')
#
#
# #   定义分词函数,对csv文件分词
def cut_words(file, output_file):
    i = 0
    key_word_arr = []
    with open(file, "r", encoding="utf-8") as data_f:
        reader = csv.reader(data_f)
        for row in reader:
            key_words = jieba.cut(row[10])
            # for column in columns:
            #     key_words = jieba.cut(column, cut_all=False)  # 对每一列分词
            for key_word in key_words:
                key_word_arr.append(key_word)
    #     将分词结果保存到CSV文件中
    with open(output_file, 'a', newline='', encoding='utf-8') as save_f:
        writer = csv.writer(save_f)
        writer.writerow(key_word_arr)


# 生成词云图
def create_wordcloud(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split(',')
        #   计算词频
        word_counts = Counter(text)
        # 设置词云图参数

        wc = WordCloud(
            font_path='simhei.ttf',
            width=800,
            height=600,
            max_words=200,
            background_color='white'
        )
        # 生成词云图
        wc.generate_from_frequencies(word_counts)
        # 显示词云图
        plt.figure(figsize=(10, 8))
        plt.imshow(wc)
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    create_wordcloud('job_key_works.txt')
