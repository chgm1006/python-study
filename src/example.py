import urllib.request as ur

print(ur.urlopen("http://www.naver.com").read().decode('utf-8'))
