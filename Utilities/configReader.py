from configparser import ConfigParser

def readConfig(section,key):
    config = ConfigParser()
    config.read("C:\\Users\\aprat\\PycharmProjects\\Regression-Web-Automation\\ConfigurationData\\conf.ini")
    return config.get(section,key)