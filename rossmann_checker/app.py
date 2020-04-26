from code.checker import check_product
from config.config import Config
from helpers.email import send_email
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    filename='rossmann.log',
    level=logging.INFO
)

config: Config = Config()

if check_product(*config.get_product_args()):
    send_email(*config.get_email_args())
else:
    logging.info('NOT FOUND')
