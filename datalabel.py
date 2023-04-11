# coding=gb2312
# coding = utf-8
# jieba分词程序
# 2023.4.10


import jieba
import pandas as pd

# 加载数据
job_data = pd.read_csv('result1-1.csv')
hunters_data = pd.read_csv('result1-2.csv')


#   定义分词函数,对csv文件分词
def cut_words(file, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for line in open(file, "r", encoding="utf-8"):
            line = line.strip()
            o_str = " ".join(jieba.lcut(line))
            f.write(o_str + "\n")


if __name__ == '__main__':
    cut_words('result1-1.csv', 'job_key_works')
