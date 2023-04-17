# coding=gb2312
# coding = utf-8
# jieba�ִʳ���
# 2023.4.10
import csv
import jieba
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import string
import re


# ��������
# job_data = pd.read_csv('result1-1.csv')
# hunters_data = pd.read_csv('result1-2.csv')
#
#
# #   ����ִʺ���,��csv�ļ��ִ�
def cut_words(file, output_file):
    i = 0
    key_word_arr = []
    with open(file, "r", encoding="utf-8") as data_f:
        reader = csv.reader(data_f)
        for row in reader:
            jieba.load_userdict('dic.txt')  # �Զ���ʿ�
            key_words = jieba.cut(row[21])  # ��ְ��Ϊ21��ְλ10
            # for column in columns:
            #     key_words = jieba.cut(column, cut_all=False)  # ��ÿһ�зִ�
            for key_word in key_words:
                key_word_arr.append(key_word)
    #     ���ִʽ�����浽CSV�ļ���
    with open(output_file, 'a', encoding='utf-8') as save_f:
        writer = csv.writer(save_f)
        writer.writerow(key_word_arr)


# ���ɴ���ͼ
def create_wordcloud(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split(',')
        #        text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]+', ',', text)  # ����
        # ���ô���ͼ����
        wc = WordCloud(
            font_path='simhei.ttf',
            width=800,
            height=600,
            max_words=200,
            background_color='white',
            relative_scaling=0.4,
            max_font_size=160,
        )

        #   �����Ƶ
        word_counts = Counter(text)
        delete_words = ['"', '"', '/', '��', '��']
        # ɾ��ָ���ʻ�
        for delete_word in delete_words:
            if delete_word in word_counts:
                del word_counts[delete_word]
        # ���ɴ���ͼ
        wc.generate_from_frequencies(word_counts)
        # ��ʾ����ͼ
        plt.figure(figsize=(10, 8))
        plt.imshow(wc)
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    # cut_words('result1-1.csv', 'job_key_works.txt')
    cut_words('result1-2.csv', 'hunter_key_works.txt')
    create_wordcloud('hunter_key_works.txt')
