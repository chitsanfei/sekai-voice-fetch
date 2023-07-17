import configparser
import os

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
root_dir = os.path.dirname(current_dir)
# 配置文件的路径
config_path = os.path.join(root_dir, 'config', 'setting_fetch.ini')

# 如果配置文件不存在，就创建一个默认的配置文件
if not os.path.exists(config_path):
    # 创建一个 ConfigParser 实例
    config = configparser.ConfigParser()
    # 设置默认配置项
    config['DEFAULT'] = {
        'url': 'https://sekai.best/storyreader/eventStory/15/6',
        'interval': '30',
        'character': '14',
        'proxy_ip': '',
        'proxy_port': ''
    }
    # 写入配置文件
    with open(config_path, 'w') as f:
        config.write(f)

# 导入 config 变量
config = configparser.ConfigParser()
config.read(config_path)
