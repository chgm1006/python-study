import urllib.request
import requests

dir_path = "C:\\Users\\forrest\\Downloads"


def save_video(url, file_name):
    urllib.request.urlretrieve(url, dir_path + "\\" + file_name)
    print("저장완료")


def download_video(url, file_name):
    r = requests.get(url)
    print(r.content)
    open(dir_path + "\\" + file_name, 'wb').write(r.content)
    print("저장완료")


if __name__ == "__main__":
    url = ""
    url_split = url.split("?")
    split = url_split[0].split("/")
    fileName = split[len(split) - 1]
    print(dir_path + "\\" + fileName)

    save_video(url, fileName)
    # download_video(url, fileName)
