# BOT_TOKEN='7671683749:AAEgtMtgOg_317GPTU4dKR5-Z_5MVXTOBJI'
# ADMIN_ID=1241318806
# CONNECT_DB=f"host=127.0.0.1 "\
#             f"port=5432 "\
#             f"user=postgres "\
#             f"password=1234567 "\
#             f"dbname=info "\
#             f"connect_timeout=10"
from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN=os.getenv("BOT_TOKEN")
ADMIN_ID=os.getenv("ADMIN_ID")
CONNECT_DB=os.getenv("CONNECT_DB")
DB_URL=os.getenv("DB_URL")
connection=os.getenv("connection")