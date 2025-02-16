import psycopg
from config import CONNECT_DB, DB_URL

async def create_db():
    conn=psycopg.connect(DB_URL)
    conn.autocommit=True
    curs=conn.cursor()
    try:
        curs.execute(f'CREATE DATABASE info WITH OWNER=postgres ENCODING=\'UTF8\'')
    except Exception as e:
        pass
    curs.close()
    conn.close()
    try:
        async with await psycopg.AsyncConnection.connect(CONNECT_DB) as conn:
            async with conn.cursor() as curs:
                await curs.execute(
                    """
                        CREATE TABLE IF NOT EXISTS orders(
                            user_id BIGINT PRIMARY KEY,
                            name VARCHAR(50),
                            last_name VARCHAR(50),
                            zip_code BIGINT,
                            plan VARCHAR(50),
                            phone VARCHAR(50),
                            longitude REAL,
                            latitude REAL
                        );
                    """
                )
                await conn.commit()
    except Exception as e:
        print(f"connection failed {e}")