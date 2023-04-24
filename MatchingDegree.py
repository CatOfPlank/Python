# 计算岗位匹配度,八个指标
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import jieba
from jieba import analyse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import jellyfish
def jaro_winkler_distance(s1, s2):
    # 计算Jaro-Winkler距离
    distance = jellyfish.jaro_winkler(s1, s2)
    print(distance)
    return distance


def cal_match_degree(job_row, hunter_row):
    match_vector = []
    if job_row[3] in hunter_row[3]:  # 预期岗位与工作岗位
        match_vector.append(1)  # 匹配岗位

    if '不限' in job_row[15]:  # 匹配学历,不限工作经验时直接设1
        match_vector.append(1)
    else:
        match_vector.append(jaro_winkler_distance(hunter_row[10],job_row[15]))  #计算相似度
        # 匹配工作经验
        # 匹配工作技能
        # 匹配工作经历
        # 匹配工作类型
        # 匹配专业
    print(match_vector)


if __name__ == '__main__':
    # 读取CSV文件
    # jobs_data = pd.read_csv('result-1.csv')
    # hunters_data = pd.read_csv('new_result-2.csv')
    # cal_match_degree(jobs_data.iloc[0], hunters_data.iloc[0])
    # print(jobs_data.iloc[0])
