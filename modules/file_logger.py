import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import date, datetime

def create_log_name(filename: str) -> str:
    """Generates a unique filename for a new log file. File names are
    created with the following format:
    
    ml_api_YYYY_MM_DD.log_idx.log

    In the above example, log_idx represents the log number, in case
    there are already logs with the same prefix in the log directory.
    """
    log_dir = os.path.split(filename)[0]
    today = datetime.now()
    date_str = today.strftime('%Y_%m_%d')

    log_name_prefix = 'ml_api_' + date_str
    log_idx = 1
    log_name = '{}.{}.log'.format(log_name_prefix, str(log_idx))
    while os.path.exists(os.path.join(log_dir, log_name)):
        log_idx += 1
        log_name = '{}.{}.log'.format(log_name_prefix, str(log_idx))
    
    filename = os.path.join(log_dir, log_name)
    return filename

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
                + 'ml_api_')
    file_handler = TimedRotatingFileHandler(
            filename=log_path, when='midnight', backupCount=30)
    
    file_handler.setFormatter(log_formatter)
    file_handler.namer = create_log_name
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    handlers = [
        console_handler, 
        file_handler]

    # Step 3 - Format the log output so it contains a time stamp and log
    # log level
    logging.basicConfig(handlers=handlers, level=logging.DEBUG)
    logging.info('File logger initialized successfully.')
    

    