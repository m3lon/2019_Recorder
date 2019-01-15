import requests
import re

r = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
t = re.findall('(?<=<!--)([\w\W\r\n]*?)(?=-->)', r.text)[0] #emmm... 这里不太明白？

l = re.findall('[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}', t) # 需要xXXXxXXXXx这种才可以

print(''.join(l))