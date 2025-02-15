import psycopg
from config import CONNECT_DB

async def create_db():
    # connect=f"host=127.0.0.1 "\
    #         f"port=5432 "\
    #         f"user=postgres "\
    #         f"password=1234567 "\
    #         f"connect_timeout=10"
    # conn=psycopg.connect(connect)
    # conn.autocommit=True
    # curs=conn.cursor()
    # try:
    #     curs.execute(f'CREATE DATABASE info WITH OWNER=postgres ENCODING=\'UTF8\'')
    # except Exception as e:
    #     pass
    # curs.close()
    # conn.close()
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
