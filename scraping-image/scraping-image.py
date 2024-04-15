import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib
import os
import requests
from time import sleep

# 最新のchromeドライバーをインストールして、インストール先のローカルパスを取得
driver_path = ChromeDriverManager().install()
# chromeドライバーのあるパスを指定して、起動
driver = webdriver.Chrome(service=Service(executable_path=driver_path))

url = "https://search.yahoo.co.jp/image/search?p=%E3%82%AB%E3%83%95%E3%82%A7&aq=-1&oq=kafe&ai=202b4f32fa06f40-fe8462bc46f368-6fc715d7faa618-99aed221c534a8&at=s&ts=6428&sfp=1&ei=UTF-8&fr=sfp_as"
driver.get(url=url)

# コピーしたXPathを使って画像のWeb要素を取得
elements = driver.find_elements(By.TAG_NAME,"img")
print(elements[0])

# Web上の画像URLを取得
img_urls=[]
for img_url in elements:
    url_p=img_url.get_attribute("src")
    img_urls.append(url_p)
    print(img_urls)

#取得データ保存
save_dir="download/"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

with urllib.request.urlopen(img_urls[0]) as rf:
    img_data = rf.read()
a=1
with open(save_dir + f"カフェ画像{a}.jpg","wb") as wf:
    wf.write(img_data)

"""
    a=1
for elem_url in img_urls:
    try:
        r=requests.get(elem_url)
        with open(save_dir + str("カフェ") + "画像"+str(a)+".jpg","wb") as fp:
            fp.write(r.content0)
        a += 1
        sleep(1)
    except:
        pass
"""
# Webドライバーの終了
driver.quit()
