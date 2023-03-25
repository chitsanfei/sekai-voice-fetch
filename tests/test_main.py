from pathlib import Path
from unittest import SkipTest, TestCase

class TestMain(TestCase):
    def test_import(self):
        from sekai.Voice import Voice
        from logger.LogManager import LogManager
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from sekai import config_path, config
        import os
        import datetime