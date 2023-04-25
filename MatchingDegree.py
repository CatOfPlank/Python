# 计算岗位匹配度,八个指标
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import jellyfish
import re

std_vector = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]  # 标准向量

f = open('result3-1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '招聘信息ID',
    '求职者ID',
    '岗位匹配度'
])
csv_writer.writeheader()  # 写入表头


def jaro_winkler_distance(s1, s2):
    # 计算Jaro-Winkler距离
    distance = jellyfish.jaro_winkler(s1, s2)
    return distance


#   计算向量相似度
def cal_vector_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)) * 100.0


def cal_match_degree(job_row, hunter_row):
    match_vector = []
    if job_row[3] in hunter_row[3]:  # 预期岗位与工作岗位
        match_vector.append(1)  # 1.匹配岗位
    else:
        match_vector.append(jaro_winkler_distance(hunter_row[3], job_row[3]))  # 计算相似度

    if '不限' in job_row[15]:  # 2.匹配工作经验,不限工作经验时直接设1
        match_vector.append(1.0)
    else:
        match_vector.append(jaro_winkler_distance(str(hunter_row[10]), str(job_row[15])))  # 计算相似度

    # 3.匹配学历
    match_vector.append(jaro_winkler_distance(re.sub(r'[^\w\s]', '', str(hunter_row[15])), str(job_row[10])))  # 去掉符号

    match_vector.append(jaro_winkler_distance(str(hunter_row[11]) + '' + str(hunter_row[20]),
                                              str(job_row[12]) + '' + str(
                                                  job_row[13])))  # 4.匹配工作技能,求职者的自我评价 + 技能水平 ； 工作的技能关键词 + 职位描述

    match_vector.append(jaro_winkler_distance(str(hunter_row[19]), str(job_row[13])))  # 5.匹配工作经历

    match_vector.append(jaro_winkler_distance(str(hunter_row[4]), str(job_row[9])))  # 6.匹配工作类型

    match_vector.append(jaro_winkler_distance(str(hunter_row[15]), str(job_row[13])))  # 7.匹配专业 ,求职者专业与工作的职位描述匹配
    print(match_vector)
    return match_vector


if __name__ == '__main__':
    # 读取CSV文件
    jobs_data = pd.read_csv('result-1.csv')
    hunters_data = pd.read_csv('new_result-2.csv')
    match_df = pd.read_csv('result3-1-sorted.csv')
    match_df['岗位匹配度'] /= 100
    match_df.to_csv('result3-1-sorted.csv')
    # # 遍历
    # for job_item in range(0, 1575):
    #     for hunter_item in range(0, 212):
    #         job_id = jobs_data.iloc[job_item][1]  # 招聘信息id
    #         hunter_id = hunters_data.iloc[hunter_item][1]  # 求职者id
    #         matching_degree = cal_vector_similarity(
    #             cal_match_degree(jobs_data.iloc[job_item], hunters_data.iloc[hunter_item]),
    #             std_vector)
    #
    #         dic = {
    #             '招聘信息ID': job_id,
    #             '求职者ID': hunter_id,
    #             '岗位匹配度': matching_degree,
    #         }
    #
    #         csv_writer.writerow(dic)
    #         print(
    #             "匹配度：{}".format(
    #                 matching_degree))

