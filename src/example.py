import urllib.request as ur

print(ur.urlopen("http://www.example.com").read().decode('utf-8'))
