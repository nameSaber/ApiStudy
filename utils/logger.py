import logging, os, time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

class Logger:
    """
    log日志配置
    """
    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d-%H%M%S")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formatter = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formatter)
        self.console.setFormatter(self.formatter)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

logger = Logger().logger

if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.info("---测试结束---")