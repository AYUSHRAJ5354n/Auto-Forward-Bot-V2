from os import environ 

class Config:
    API_ID = environ.get("API_ID", "9102574")
    API_HASH = environ.get("API_HASH", "0861a545777adba2d599304b6474aad1")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7993450137:AAE3Nw31zHrln8YPkIkluV5enwqc6XAWMu") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://kentkouhwcsps:vNJdZFcCPyCShL2J@cluster0.rnjjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1685470205 8087874850').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
