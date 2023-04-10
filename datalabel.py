# 分词
import jieba
import pandas as pd

# 加载数据
job_data = pd.read_csv('result1-1.csv')
hunters_data = pd.read_csv('result1-2.csv')


#   定义分词函数
def cut_words(text):
    words = jieba.cut(text)
    return ''.join(words)

#   对每一列分词
    job_data['职位描述关键词'] = job_data['职位描述'].apply(cut_words)

#   保存到新的csv文件
    job_data.to_csv('job_key_work',index=False)