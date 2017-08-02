
import requests
from bs4 import BeautifulSoup



url = requests.get('http://m.kma.go.kr/m/forecast/forecast_01.jsp#')
response = url.text
bs4 = BeautifulSoup(response,'html.parser')

# for x in bs4.find_all('p',{'class':'letter_box_multiline'}):
#     result = str(x.span)
#     result = result.replace('<br/>',' : ')
#     result = result.replace('<span>',"")
#     result = result.replace('</span>',"")
#     print(result)


result = []

for x in bs4.find_all('td'):
    try:
        if not x.contents[0].get('alt') is None:
            if not "구름" in x.contents[0].get('alt'):
                result.append(x.contents[0].get('alt'))
        elif not x.contents[0].text is None:           
            result.append(x.contents[0].text)
    except:
        pass
i = 0
sum_text = ""
for r in result:
    if i < 5:
        i += 1
        if i == 5:
            sum_text += r
        else:
            sum_text += r + ', '
    if i == 5:
        print(sum_text)
        sum_text = ""
        i = 0
        



