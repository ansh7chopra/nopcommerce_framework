import logging

class LogGen:
    def loggen():
        logger=logging.getLogger(__name__)
        filehandler=logging.FileHandler(r'C:\Users\ACHOPRA\PycharmProjects\FrameWork\logs\automation.log')
        formatter=logging.Formatter("%(asctime)s: %(levelname)s: %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger




#hierarchy  in logs
    # debug
    # info
    # warnings
    # error
    # critical
