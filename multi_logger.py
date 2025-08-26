import logging

## Create logger for module 1
logger1 = logging.getLogger('module1')
logger1.setLevel(logging.DEBUG)

## Create logger for module 2
logger2 = logging.getLogger('module2')
logger2.setLevel(logging.WARNING)


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)


logger1.debug("This is debug message")
logger2.warning("This is a warning message")
logger2.error("This is an error message")