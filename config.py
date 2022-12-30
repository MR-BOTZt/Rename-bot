import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22359038")

API_HASH = os.environ.get("API_HASH", "b3901895dc193c30c808ba4f1b550ed0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5687723921:AAHKpx7sjRAWeJyxSyLr2E-fHrvTZ79t7P0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001870353033") 

DB_NAME = os.environ.get("DB_NAME","@lucascinemahubbot")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://CM:CM@cluster0.gsghs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/61ced6ea9f257377bc65a.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5531461861 5783190735').split()]

