from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="bot1/.env")
BOT_TOKEN=os.getenv("BOT_TOKEN")
ADMIN_ID=os.getenv("ADMIN_ID")
CONNECT_DB=os.getenv("CONNECT_DB")
DB_URL=os.getenv("DB_URL")