import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib
import os
import requests
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# WebDriverのオプションを設定
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--no-sandbox")  # セキュリティ上の制限を回避
options.add_argument("--lang=ja")     # 言語設定を日本語に

# ChromeDriverを使用してWebDriverのインスタンスを作成
driver = webdriver.Chrome(options=options)

# URL開く
driver.get("https://search.yahoo.co.jp/image")
# 待機処理
driver.implicitly_wait(10)
#sleep(10)
wait = WebDriverWait(driver=driver, timeout=10)
 #検索窓 
Word = "カフェ"
# 最新のchromeドライバーをインストールして、インストール先のローカルパスを取得
#driver_path = ChromeDriverManager().install()
# chromeドライバーのあるパスを指定して、起動
#driver = webdriver.Chrome(service=Service(executable_path=driver_path))

driver.find_element(By.CLASS_NAME, "SearchBox__searchInput").send_keys(Word)
sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/form/div[1]/button").click()
sleep(3)

height=1000
while height <5000:
    driver.execute_script("window.scrollTo(0,{});".format(height))
    height += 100
    sleep(1)
#待機処理
wait.until(EC.presence_of_all_elements_located)

# コピーしたXPathを使って画像のWeb要素を取得
elements = driver.find_elements(By.TAG_NAME,"img")

# Web上の画像URLを取得
img_urls=[]
for img_url in elements:
    url_p=img_url.get_attribute("src")
    img_urls.append(url_p)
    #print(img_urls)

#保存フォルダ作成、パス指定
save_dir="download/"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

#バイナリデータ読み込み、保存
a=1
for img_url in img_urls:
    try:
        with urllib.request.urlopen(img_url) as rf:
            img_data = rf.read()
        with open(save_dir + f"{Word}画像{a}.jpg","wb") as wf:
            wf.write(img_data)
        a=a+1
        sleep(1)
    except:
        pass

# Webドライバーの終了
driver.quit()
