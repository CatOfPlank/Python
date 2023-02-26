import pandas as pd
import requests
import re

# 伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36 Edg/110.0.1587.56 '
}

header_find_job = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36 Edg/110.0.1587.56 '

}
Max_page = 158  # 网站最大页码


# 获取招聘工作id
def get_jobid(str_mes):
    id_cnt = 0
    for j in range(10):  # 一行十个工作
        index_id = str_mes.index('"jobPositionId"')  # 查找id项
        if index_id:
            id_cnt += 1
            print("第{}个招聘信息id：{}".format(id_cnt, str_mes[index_id + 1]))
        str_mes = str_mes[index_id + 50:]  # 跳过本条


# 爬取全部数据
for i in range(1, Max_page):  # 翻页
    url_job = "https://www.5iai.com/api/enterprise/job/public/es?pageSize=10&pageNumber=" + str(i) + "&willNature" \
                                                                                                     "=&function" \
                                                                                                     "=&wageList=%255B%255D" \
                                                                                                     "&workplace" \
                                                                                                     "=&keyword= "  # 招聘信息url

    url_find_job = "https://www.5iai.com/api/resume/baseInfo/public/es?pageSize=10&pageNumber=" + str(i) + "&function" \
                                                                                                           "=&skills" \
                                                                                                           "=&workplace" \
                                                                                                           "=&keyword= "  # 求职者信息url

    response_job = requests.get(url=url_job, headers=header)
    response_hunter = requests.get(url=url_find_job, headers=header_find_job)
    mes_job = re.split(',|:', response_job.text)
    mes_hunter = re.split(',|:', response_hunter.text)  # 分割数据
    print("求职者第" + str(i) + "页信息:")
    print(mes_hunter)
    print("招聘工作第" + str(i) + "页信息:")
    print(mes_job)
