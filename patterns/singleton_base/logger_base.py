from singleton_base import SingletonBase
from datetime import datetime

class Logger(SingletonBase):
    log_file = None
    def __init__(self, path: str):
        self.log_file = open(path, mode='w') if self.log_file is None else self.log_file

    def write_log(self, log_record: str) -> None:
        now = str(datetime.now()) # set time
        record = f'{now}: {log_record}\n' # create log record
        self.log_file.write(record) # write log

    def close_log(self) -> None:
        self.log_file.close() # close when done, no memory leak
        self.log_file = None