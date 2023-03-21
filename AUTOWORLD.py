import requests
import ssl

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6308011a)'

}
url = 'https://office.chaoxing.com/data/apps/seatengine/getusedseatnums?seatId=602&roomId=1850&startTime=20%3A00&endTime=22%3A00&day=2023-03-12'
response = requests.get(url=url, headers=headers, verify=True)
print(response.content)
