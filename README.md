# Amos logger
```text
For easier use of Log
```
## 1. Write logs to different directories
Usage
```python

import logging
from AmosLogger.AmosLogger import AmosLogger

if __name__ == '__main__':
    amos_info_logger = AmosLogger(name='TestLog')
    amos_info_logger.set_logger()
    amos_info_logger.info('Test')

    amos_warn_logger = AmosLogger(name='TestLog')
    amos_warn_logger.set_logger(log_level=logging.WARN)
    amos_warn_logger.warning('Test')

    amos_error_logger = AmosLogger(name='TestLog')
    amos_error_logger.set_logger(log_level=logging.ERROR)
    amos_error_logger.error('Test')
```
```shell
/var/log/TestLog # ls
ERROR  INFO  WARNING

/var/log/TestLog/ERROR # ls
TestLog  TestLog.2023-08-25.log

/var/log/TestLog/ERROR # tailf TestLog
[2023-08-28 09:09:10,127][7335][ERROR]-(main.py:16) - Test
[2023-08-28 09:09:15,128][7389][ERROR]-(main.py:16) - Test
[2023-08-28 09:10:04,423][7770][ERROR]-(main.py:16) - Test
[2023-08-28 09:23:07,312][10550][ERROR]-(main.py:16) - Test
```

## 2. Write all logs to the same file
Usage
```python
from AmosLogger.AmosLogger import AmosLogger

if __name__ == '__main__':
    amos_all_in_one_logger = AmosLogger(name='Test_Log')
    amos_log = amos_all_in_one_logger.set_all_in_one_logger()
    amos_log.info("Info log")
    amos_log.warning("Warning log")
    amos_log.error("Error log")

```
```shell
/var/log/Test_Log # tailf Test_Log
[2023-08-28 09:23:07,312][10550][INFO]-(main.py:20) - Info log
[2023-08-28 09:23:07,312][10550][WARNING]-(main.py:21) - Warning log
[2023-08-28 09:23:07,312][10550][ERROR]-(main.py:22) - Error log
```
