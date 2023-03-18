import pandas as pd
import requests
import re
import xlwings as xw
import csv
import pprint
import json
import time

# 泰迪杯数据挖掘C题---招聘网站双向推荐系统

# 伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36 Edg/110.0.1587.56 '
}  # 招聘页面

header_find_job = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36 Edg/110.0.1587.56 '

}  # ‘找工作’页面

header_job_detail = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36 Edg/110.0.1587.57'

}  # 招聘工作具体要求

header_hunter_detail = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'

}  # 求职者具体信息

Max_page = 2  # 网站最大页码

education_requirement = {"不限": 1, "技工": 1, "大专": 2, "本科": 3, "硕士": 4, "博士": 5}  # 学历要求，网站以代码形式展现


# 数据导出
f = open('result_1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '招聘信息id',
    '岗位名称',
    '公司名称',
    '职位关键词',
])
csv_writer.writeheader()  # 写入表头


def export_data(mes):
    json_data = json.loads(mes)  # 转成dict格式
    pprint.pprint(json_data)  # 格式化输出


# 遗传算法计算权重
def cal_weight(data):
    data


# 构建招聘工作数学模型
def create_recruit_model(job_detail):
    job_detail


# 创建求职者数学模型
def create_hunters_model(hunters_detail):
    hunters_detail


# 计算向量相似度
def cal_vector_similarity(vec1, vec2):
    cos_sim = vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)) * 100
    print("向量相似度为：{:.5f}%".format(cos_sim))


# 获取招聘工作id
def get_jobid(str_mes):
    jobid_list = []
    id_cnt = 0
    for j in range(10):  # 一行十个工作
        index_id = str_mes.index('"jobPositionId"')  # 查找工作Id项
        if index_id >= 0:
            id_cnt += 1  # id数加一
            if str_mes[index_id + 1] != "null":
                print("第{}个招聘信息id：{}".format(id_cnt, str_mes[index_id + 1]))
                jobid_list.append(str_mes[index_id + 1])
            else:
                print("error!")
        str_mes = str_mes[index_id + 50:]  # 跳过本条
    return jobid_list  # 返回工作id列表


# 根据招聘工作id获取工作要求详细信息
def get_job_details(job_id_list):
    for index_list in range(0, 10):  # 一页十条数据
        job_detail_url = "https://www.5iai.com/api/enterprise/job/public?id=" + "".join(
            list(filter(str.isdigit, job_id_list[index_list])))
        detail_job_response = requests.get(url=job_detail_url, headers=header_job_detail)  # 获取详细信息
        print("第{}个招聘工作详细要求".format(index_list + 1))
        export_data(detail_job_response.text)


# 提取求职者id
def get_hunters_id(str_mes):
    id_list = []  # 存储id的列表
    hunter_cnt = 0
    for k in range(10):  # 一页十条
        hunter_id_index = str_mes.index('"username"')  # 查找id项
        if hunter_id_index >= 0:  # 可靠
            hunter_cnt += 1
            print("第{}个求职者id：{}".format(hunter_cnt, str_mes[hunter_id_index - 1]))
            id_list.append(str_mes[hunter_id_index - 1])
        str_mes = str_mes[hunter_id_index + 10:]  # 跳过本条
    return id_list  # 返回id列表6


# 获取求职者具体简历
def get_hunter_detail(hunter_id_list):
    for index_list in range(0, 10):
        hunter_detail_url = "https://www.5iai.com/api/resume/baseInfo/public/" + "".join(
            list(filter(str.isdigit, hunter_id_list[index_list])))
        detail_hunter_response = requests.get(url=hunter_detail_url, headers=header_hunter_detail)  # 获取求职者简历
        print("第{}个求职者简历：".format(index_list + 1))
        export_data(detail_hunter_response.text)


# 爬取全部数据
def get_all_message():
    for i in range(1, Max_page):  # 翻页
        time.sleep(1)
        url_job = "https://www.5iai.com/api/enterprise/job/public/es?pageSize=10&pageNumber=" + str(i) + "&willNature" \
                                                                                                         "=&function" \
                                                                                                         "=&wageList=%255B%255D" \
                                                                                                         "&workplace" \
                                                                                                         "=&keyword= "  # 招聘信息url

        url_find_job = "https://www.5iai.com/api/resume/baseInfo/public/es?pageSize=10&pageNumber=" + str(
            i) + "&function" \
                 "=&skills" \
                 "=&workplace" \
                 "=&keyword= "  # 求职者信息url

        response_job = requests.get(url=url_job, headers=header)
        response_hunter = requests.get(url=url_find_job, headers=header_find_job)
        mes_job = response_job.text.strip()
        # job_data = mes_job.replace("\"", "'")
        # mes_job = re.split(',|:', response_job.text[50:]) # 前缀处理
        # mes_hunter = re.split(',|:', response_hunter.text)  # 分割数据
        # print("求职者第" + str(i) + "页信息:")
        # print(mes_hunter)
        # get_hunters_id(mes_hunter)  # 求职者id
        # print("招聘工作第" + str(i) + "页信息:")
        json_data = json.loads(mes_job)['data']['content']  # 得到查看content里的数据
        # print(json_data)
        # print(type(json_data))
        # pprint.pprint(json_data['content'])
        for index in json_data:
            job_id = index['id']
            position = index['positionName']
            enterpriseExtInfo = index['enterpriseExtInfo']
            company = enterpriseExtInfo.get('shortName')
            industry = enterpriseExtInfo.get('industry')
            keyword = industry.replace('[', '').replace(']', '').replace('"', '')
            dit = {
                '招聘信息id': job_id,
                '岗位名称': position,
                '公司名称': company,
                '职位关键词': keyword,
            }
            print(job_id, position, company, keyword)
            csv_writer.writerow(dit)


if __name__ == '__main__':
    get_all_message()
