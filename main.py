from logger.log_manager import LogManager
from sekai.voice import Voice


def main():
    # 初始化对象，标记程序开始
    log_manager = LogManager()
    voice = Voice()
    log_manager.log("开始执行程序")

    # 获取mp3列表
    log_manager.log('开始获取mp3列表')
    count = 0

    # 执行循环，直到获取成功为止
    while True:
        count += 1
        log_manager.log('正在尝试获取mp3列表，已执行' + str(count) + '次')
        mp3_list = voice.get_mp3_list
        if len(mp3_list) != 0:
            break
    
    # 筛选器工作
    log_manager.log('开始筛选mp3列表')
    mp3_list = voice.filter_mp3_list(mp3_list)

    # 下载器工作
    log_manager.log('开始下载mp3文件')
    voice.download_mp3(mp3_list)

    # 程序结束
    log_manager.log('程序执行完成')


if __name__ == '__main__':
    main()
