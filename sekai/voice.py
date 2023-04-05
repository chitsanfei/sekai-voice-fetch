import time
import requests
import re
import os
from logger.log_manager import LogManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sekai import config


class Voice:

    def __init__(self):
        # self.config = configparser.ConfigParser()
        # config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'setting_fetch.ini')
        self.config = config
        self.url = config.get('DEFAULT', 'url')
        self.interval = config.getint('DEFAULT', 'interval')
        self.character = config.getint('DEFAULT', 'character')

    def get_mp3_list(self):
        url = self.url
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
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
