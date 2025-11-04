"""
In logger classic we define a typical classic use case of singleton patter
the logger can only have one instance reading and writing to a file
so it will need to check the class __dict__ to make sure no other instance is performing
"""
from datetime import datetime

class Logger:
    log_file = None

    # used to access one instance therefore static method
    @staticmethod
    def instance():
        # checks the instance in the class dictionary if its not in there it adds it to the dictionary instance
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
        return Logger._instance
    
    def open_log(self, path: str):
        self.log_file = open(path, mode='w') # open log file for writing

    def write_log(self, log_record: str) -> None:
        now = str(datetime.now()) # set time
        record = f'{now}: {log_record}\n' # create log record
        self.log_file.write(record) # write log

    def close_log(self) -> None:
        self.log_file.close() # close when done, no memory leak


logger = Logger.instance()
logger.open_log('my.log')
logger.write_log('Logging with classic Singleton pattern')
logger.close_log()

with open('my.log', 'r') as f:
    for line in f:
        print(line, end='')


# violate single responsibility
# non standard class access
# harder to test
# carry global state
# singletons considered harmful :'( - considered anti pattern
    