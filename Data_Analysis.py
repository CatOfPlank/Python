import pandas as pd
import requests
import re

url = 'https://www.5iai.com/api/enterprise/job/public/es?pageSize=10&pageNumber=1&willNature=&function=&wageList' \
      '=%255B%255D&workplace=&keyword= '
# 伪装头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
                  'Safari/537.36 Edg/110.0.1587.56 '
}
id_cnt = 0  # 计数
for i in range(1, 50):  # 翻页
    url = "https://www.5iai.com/api/enterprise/job/public/es?pageSize=10&pageNumber=" + str(i) + "&willNature=&function" \
                                                                                                 "=&wageList=%255B%255D" \
                                                                                                 "&workplace=&keyword= "
    response = requests.get(url=url, headers=header)
    mes = re.split(',|:', response.text)  # 分割数据
    print("第" + str(i) + "页:")
    print(mes)
    for j in range(10):  # 一行十个工作
        index_id = mes.index('"jobPositionId"') # 查找id项
        if index_id:
            id_cnt += 1
            print("第{}个id：{}".format(id_cnt,mes[index_id+1]))
        mes = mes[index_id + 50:]  # 跳过本条
    # str_mes = ','.join(mes)
    # print(str_mes)
    # index_id = str_mes.index("id")
    # print(index_id)
    # for j in range(10):  # 一行十个工作
    #     index_id = mes.index("message")
    #     print(index_id)
    #     # print("id{}:{}".format(id_cnt, mes[7 + 25 * j]))
    #     id_cnt += 1
    # 获取id
    # print(mes)
    # print("id:{}".format(mes[7]))
    # print(mes)
    # print(mes[5])

    # 数据分割
