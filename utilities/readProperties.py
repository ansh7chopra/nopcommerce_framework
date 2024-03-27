import configparser

config=configparser.RawConfigParser()
config.read(r"C:\Users\ACHOPRA\PycharmProjects\FrameWork\configurations\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURl():
        url=config.get('common info','baseurl')
        return url
    @staticmethod
    def getUsername():
        url=config.get('common info','username')
        return url
    @staticmethod
    def getPassword():
        url=config.get('common info','password')
        return url



