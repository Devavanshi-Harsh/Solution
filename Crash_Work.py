

import logging
log_format="%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="newlog.log", level=logging.DEBUG, format=log_format, filemode='w')

logger=logging.getLogger()
logger.info("printanything")