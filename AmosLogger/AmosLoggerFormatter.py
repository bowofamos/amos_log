from . import *


class AmosLogFormatter(logging.Formatter):
    def __init__(self, fmt, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)

    def format(self, record):
        # 设置颜色
        level_color = {
            logging.INFO: '\033[0;32m',
            logging.WARNING: '\033[0;33m',
            logging.ERROR: '\033[0;31m',
            logging.CRITICAL: '\033[0;35m'
        }
        record.levelname = level_color.get(record.levelno) + record.levelname + '\033[0m'
        return super().format(record)
