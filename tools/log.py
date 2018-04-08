import logging, time, os
from tools.config import LOG_PATH, Config

class Log:
    def __init__(self, name='root', log_path = LOG_PATH):
        #文件的命名
        c = Config().get('log')
        self.logname = os.path.join(log_path, '%s.log' %time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(name)

        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else '[%(asctime)s]-%(name)s-%(levelname)s: %(message)s'
        self.formatter = logging.Formatter(pattern)

    def __console(self, level, message):
        #创建FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8') #追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        
        #创建StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        
        if level =='info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'exception':
            self.logger.exception(message)
        
        #删除处理器，避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        
        #关闭文件
        ch.close()
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def info(self, message):
        self.__console('info', message)

    def exception(self, message):
        self.__console('exception', message)

logger = Log()

if __name__ == '__main__':
    log = Log()
    log.info('---start test---')
    log.info('input pw')
    log.info('---test end---')