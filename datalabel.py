# �ִ�
import jieba
import pandas as pd

# ��������
job_data = pd.read_csv('result1-1.csv')
hunters_data = pd.read_csv('result1-2.csv')


#   ����ִʺ���
def cut_words(text):
    words = jieba.cut(text)
    return ''.join(words)

#   ��ÿһ�зִ�
    job_data['ְλ�����ؼ���'] = job_data['ְλ����'].apply(cut_words)

#   ���浽�µ�csv�ļ�
    job_data.to_csv('job_key_work',index=False)