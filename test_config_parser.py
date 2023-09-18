import configparser

config = configparser.ConfigParser()
config.read(".cfg")

config = config["TEST"]

print(config["hi"])
