import threading
from queue import Queue
from spider import Spider
from domain import *
from crawlerConfiguration import *

PROJECT_NAME = 'thesite'
HOME_PAGE = 'https://xn--kttim-kva.dev/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
