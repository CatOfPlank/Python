# coding=gb2312
# coding = utf-8
# jieba分词程序
# 2023.4.10
import csv
import jieba
import pandas as pd


# 加载数据
# job_data = pd.read_csv('result1-1.csv')
# hunters_data = pd.read_csv('result1-2.csv')
#
#
# #   定义分词函数,对csv文件分词
def cut_words(file, output_file):
    i = 0
    with open(file, "r", encoding="utf-8") as data_f:
        reader = csv.reader(data_f)
        for row in reader:
            key_words = jieba.cut(row[10])
            # for column in columns:
            #     key_words = jieba.cut(column, cut_all=False)  # 对每一列分词
            for key_word in key_words:
                print(key_word)
                i = i + 1
                #     将分词结果保存到CSV文件中
                with open(output_file, 'a', newline='', encoding='utf-8') as save_f:
                    writer = csv.writer(save_f)
                    writer.writerows(key_word)
    print('共有{}条信息'.format(i))


if __name__ == '__main__':
    cut_words('result1-1.csv', 'job_key_works.csv')
    print("分词成功！")
