import logging
import sys




def get_logger(name, log_file_name):

    logger = logging.getLogger(name)
    logging.basicConfig(
        filename=log_file_name, 
        level=logging.INFO,
        format="%(asctime)s (%(levelname)s: __%(module)s__) %(message)s"
    )
    
    sys.stdout = open(log_file_name, "a")
