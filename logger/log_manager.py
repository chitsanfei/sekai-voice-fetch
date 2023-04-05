import os
import datetime


class LogManager:
    def __init__(self):
        self.log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
        self.log_file = os.path.join(self.log_dir, f"{datetime.datetime.now().strftime('%Y-%m-%d')}.txt")
        self._delete_old_logs()

    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : " + message)

    def _delete_old_logs(self):
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)
        for file in os.listdir(self.log_dir):
            file_path = os.path.join(self.log_dir, file)
            if os.path.isfile(file_path):
                time_diff = datetime.datetime.now() - datetime.datetime.strptime(file[:-4], '%Y-%m-%d')
                if time_diff.days >= 3:
                    os.remove(file_path)
