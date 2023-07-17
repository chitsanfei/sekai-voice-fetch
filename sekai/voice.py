import time
import requests
import re
import os

from logger.log_manager import LogManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Proxy

from sekai import config


class Voice:

    def __init__(self):
        # self.config = configparser.ConfigParser()
        # config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'setting_fetch.ini')
        self.config = config
        self.url = config.get('DEFAULT', 'url')
        self.interval = config.getint('DEFAULT', 'interval')
        self.character = config.getint('DEFAULT', 'character')
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    @property
    def get_mp3_list(self):
        url = self.url
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"user-agent={self.user_agent}")

        proxy_ip = "http://127.0.0.1"
        proxy_port = "7890"
        proxy = Proxy({
            'proxyType': 'MANUAL',
            'httpProxy': f'{proxy_ip}:{proxy_port}',
            'sslProxy': f'{proxy_ip}:{proxy_port}',
        })
        chrome_options.add_argument('--proxy-server=%s' % proxy.httpProxy)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        # 显式等待，等待 JavaScript 加载完成
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # 等待页面上某个元素加载完成
        # wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='MuiContainer-root MuiContainer-maxWidthLg css-1qos7gm']")))

        html = driver.page_source

        mp3_list = []
        for a in re.findall(r'<a.*?</a>', html):
            mp3 = re.findall(r'href="(.*?\.mp3)"', a)
            if mp3:
                mp3_list.append(mp3[0])
        driver.quit()
        return mp3_list

    def filter_mp3_list(self, mp3_list):
        mp3_list = [url for url in mp3_list if url.endswith(f"{self.character}.mp3")]
        return mp3_list

    def download_mp3(self, mp3_list):
        log_manager = LogManager()
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resource')
        if not os.path.exists(path):
            os.mkdir(path)
        for mp3 in mp3_list:
            filename = mp3.split('/')[-1]
            filepath = os.path.join(path, filename)
            if os.path.exists(filepath):
                log_manager.log(f'{filename} 已存在，跳过下载')
                continue
            response = requests.get(mp3)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            # 获取mp3_list中项目数量，并且输出现在正在下载第几个文件
            log_manager.log(f'正在下载第 {mp3_list.index(mp3) + 1} 个文件，共 {len(mp3_list)} 个文件')
            log_manager.log(f'下载完成 {filename}')
            time.sleep(self.interval)
