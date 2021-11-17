import logging as lg

logger = lg.getLogger(__name__)
logger.setLevel(lg.DEBUG)

file_handler = lg.FileHandler("module.log")

stream_handler = lg.StreamHandler() # to log into console
formatter = lg.Formatter("[%(filename)s: %(asctime)s: [%(funcName)10s:%(lineno)d]: [%(levelname)10s]: %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def func1():
    logger.warning("This is func1 warning")

def func2():
    logger.critical("This is func2 critical")
    
func1()
func2()