import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import date

def initialize_file_logger():
    """Initializes and configures the file logger with and log output
    directories so descriptive logs can be saved.

    The log contains two handlers; the first prints output to the
    console whereas the second saves output in a log file. For
    convenience, each entry is formatted with a time stamp and log
    level, as follows:

    [HH:MM:SS][LOG_LEVEL] Log message here.

    To ensure that log files remain manageable in size, a new log file
    is created on a daily basis. The log files are stored
    """

    # Step 1 - If not already available, create the directory hierarchy
    # in which log files will be stored
    today = date.today()
    year_str = today.strftime('%Y')
    month_str = today.strftime('%Y-%m')
    date_str = today.strftime('%Y-%m-%d')
    log_root = 'logs/'

    if os.path.exists(log_root) == False:
        os.mkdir(log_root)
    if os.path.exists(log_root + year_str) == False:
        os.mkdir(log_root + year_str)
    if os.path.exists(log_root + year_str + '/' + month_str) == False:
        os.mkdir(log_root + year_str + '/' + month_str)
    # Step 2 - Add a console handler and log file handler
    # TODO: Add threadh name when multithreading is enabled
    # [%(threadName)s]
    log_formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s]  %(message)s',
        datefmt='%H:%M:%S')
    log_path = (log_root + year_str +'/' + month_str + '/' 
                + date_str + 'ml_api.log')
    file_handler = TimedRotatingFileHandler(
            filename=log_path, when='midnight', backupCount=30)
    file_handler.suffix = '%Y-%m-%d'
    file_handler.setFormatter(log_formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    handlers = [
        console_handler, 
        file_handler]

    # Step 3 - Format the log output so it contains a time stamp and log
    # log level
    logging.basicConfig(
        handlers=handlers, level=logging.DEBUG)
    logging.info('File logger initialized successfully.')

    

    