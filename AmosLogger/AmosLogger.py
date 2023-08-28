from . import *
from .AmosLoggerFormatter import AmosLogFormatter


class AmosLogger(Logger):
    amos_logger = None

    def __init__(self, name: str, log_path: str = "/var/log/"):
        super().__init__(name)
        self.log_name = name
        self.log_path = log_path
        self.log_level = None

    def amos_logs(self):
        logger = super()
        logger.setLevel(self.log_level)
        level_name = logging.getLevelName(self.log_level)
        file_dir = (self.log_path + self.log_name + '/{0}'.format(level_name))
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        filename = os.path.join(file_dir, self.log_name)
        file_handler = TimedRotatingFileHandler(filename=filename, when="MIDNIGHT", interval=1, backupCount=30)
        file_handler.suffix = "%Y-%m-%d.log"
        file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        if self.log_level == logging.INFO:
            status = "\033[32m[%(levelname)s]\033[0m"
        elif self.log_level == logging.WARNING:
            status = "\033[33m[%(levelname)s]\033[0m"
        elif self.log_level == logging.ERROR:
            status = "\033[31m[%(levelname)s]\033[0m"
        else:
            status = "\033[90m[%(levelname)s]\033[0m"
        file_handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s][%(process)d]" + status + "-(%(filename)s:%(lineno)d) - %(message)s"
            )
        )
        logger.addHandler(file_handler)
        return logger

    def set_logger(self, log_path: str = "/var/log/", log_level: int = logging.INFO):
        self.log_path = log_path
        self.log_level = log_level
        self.amos_logger = self.amos_logs()

    def set_all_in_one_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        file_dir = (self.log_path + self.log_name)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file = os.path.join(file_dir, self.log_name)
        file_handler = TimedRotatingFileHandler(filename=file, when="MIDNIGHT", interval=1, backupCount=30)
        file_handler.setLevel(logging.INFO)
        file_handler.suffix = "%Y-%m-%d.log"
        file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        file_handler.setFormatter(
            AmosLogFormatter(
                "[%(asctime)s][%(process)d][%(levelname)s]-(%(filename)s:%(lineno)d) - %(message)s"
            )
        )
        logger.addHandler(file_handler)
        return logger


