import requests
import json
import re
import csv
import pprint
import json
import time

url_job='https://www.5iai.com/api/enterprise/job/public/es?pageSize=1700&pageNumber=1&willNature=&function=&wageList=%255B%255D&workplace=&keyword='

f = open('result_0.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '招聘信息id',
    '公司名称',
    '招聘岗位',
    '招聘人数',
    '最低工资',
    '最高工资',
    '职位福利',
    '工作类型',
    '学历要求',
    '职位关键词',
    '技能关键词',
    '职位描述',
    '工作地点',
    '工作经验要求',
])
csv_writer.writeheader()  # 写入表头

req_job=requests.get(url_job)
js_data=req_job.json()
job_id=[i['id'] for i in js_data['data']['content']]

url_jd='https://www.5iai.com/api/enterprise/job/public'
list_kw = []
list_skills = []
for i in job_id[:1574]:
    dict_job={'id':i}
    req_jd= requests.get(url_jd,params=dict_job)
    mes_job = req_jd.text.strip()
    if 'data' in mes_job:
        json_data = json.loads(mes_job)['data']
    keywordList = json_data['keywordList']
    for index_key in keywordList:
        keyword = index_key['labelName']
        list_kw.append(keyword)
    labelName = ",".join(list_kw[:])
    list_kw.clear()

    skillsList = json_data['skillsList']
    for index in skillsList:
        skillsName = index['labelName']
        list_skills.append(skillsName)
    skills = ",".join(list_skills[:])
    list_skills.clear()

    job_id = json_data['id']
    jobRequirements = json_data['jobRequiredments']
    good = json_data['welfare']
    welfare = good.replace('[', '').replace(']', '').replace('"', '')
    position = json_data['positionName']
    minimumWage = json_data['minimumWage']
    maximumWage = json_data['maximumWage']
    educationalRequirements = json_data['educationalRequirements']
    company = json_data['enterpriseName']
    exp = json_data['exp']
    count = json_data['count']
    willNature = json_data['willNature']
    enterpriseAddress = json_data['enterpriseAddress']
    detailedAddress = enterpriseAddress.get('detailedAddress')

    dit = {
        '招聘信息id': job_id,
        '公司名称': company,
        '招聘岗位': position,
        '招聘人数': count,
        '最低工资': minimumWage,
        '最高工资': maximumWage,
        '职位福利': welfare,
        '工作类型': willNature,
        '学历要求': educationalRequirements,
        '职位关键词': labelName,
        '技能关键词': skills,
        '职位描述': jobRequirements,
        '工作地点': detailedAddress,
        '工作经验要求': exp,
    }
    print(job_id, company, position, count, minimumWage, maximumWage, welfare, willNature,
          educationalRequirements, labelName, skills, jobRequirements, detailedAddress, exp)
    csv_writer.writerow(dit)