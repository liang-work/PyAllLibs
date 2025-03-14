
import logging
import os
import colorlog  # 导入 colorlog 库

# 定义一个函数来返回日志记录的目录名
def get_directory_name(record):
    # 从记录中获取文件路径
    pathname = record.pathname
    # 返回目录名
    return os.path.basename(os.path.dirname(pathname))

    # 自定义日志格式
log_format = '%(asctime)s - [%(directory_name)s] - %(filename)s [%(levelname)s]: %(message)s'

class DirectoryNameFilter(logging.Filter):
    def filter(self, record):
        record.directory_name = get_directory_name(record)
        return True

def loging(debug=False,path="run.log"):
    logger = logging.getLogger(__name__)  # 先初始化日志
    logger.addFilter(DirectoryNameFilter())  # 添加目录名过滤器

    console_handler = logging.StreamHandler()
    console_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - [%(directory_name)s] - %(filename)s [%(levelname)s]: %(message)s%(reset)s',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'bold_red',
            'CRITICAL': 'red',
        }
    )
    console_handler.setFormatter(console_formatter)

    file_handler = logging.FileHandler(path)
    file_formatter = logging.Formatter(log_format)
    file_handler.setFormatter(file_formatter)

    # 将处理器添加到日志记录器中
    logger.addHandler(file_handler)

    # 设置日志记录器的最低级别为 DEBUG
    logger.setLevel(logging.DEBUG)

    if debug:
        logger.addHandler(console_handler)
    else:
        logger.setLevel(logging.INFO)

    return logger