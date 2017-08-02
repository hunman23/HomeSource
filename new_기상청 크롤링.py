
import requests
from bs4 import BeautifulSoup
from fbchat import Client

url = requests.get('http://m.kma.go.kr/m/forecast/forecast_01.jsp#')
response = url.text
bs4 = BeautifulSoup(response,'html.parser')


result = []
for x in bs4.find_all('td'):
    try:
        if not x.contents[0].get('alt') is None:
            fst_check = x.contents[0].get('alt')
            if '시' in fst_check :
                result.append('시간: ' + fst_check)
            elif '흐림' in fst_check or '비' in fst_check or '구름 많음' in fst_check:
                result.append('날씨: ' + fst_check)
        elif not x.contents[0].text is None:
            scd_check = x.contents[0].text
            if '℃' in scd_check :
                result.append('기온: ' + scd_check)
            elif 'm/s' in scd_check :
                result.append('바람: ' + scd_check)
            elif '%' in scd_check :
                result.append('습도: ' + scd_check)
    except:
        pass

# 아래 For문 변수 지정
i = 0
sum_text = ""
result_sum = ""

for r in result:
    if i < 5:
        i += 1
        if i == 5:
            sum_text += r
        else:
            sum_text += r + ', '
    if i == 5:
        result_sum += sum_text + '\n' 
        sum_text = ""
        i = 0

fc = Client('hunman23@gmail.com', 'hsy1685020')
friends = fc.searchForUsers('한세영')
friend = friends[0]
sent = fc.sendMessage(result_sum, thread_id=friend.uid)
if sent:
    print("Message sent successfully!")



