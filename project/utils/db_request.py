from psycopg import AsyncConnection


class Request:
    def __init__(self, connector: AsyncConnection):
        self.connector=connector
    async def add_data(self, user_id: int, name: str, last_name: str, zip_code: str, plan: str,
                        phone: str, longitude: float, latitude: float):
        query=f"INSERT INTO orders (user_id, name, last_name, zip_code, plan, phone, longitude, latitude) "\
        f"VALUES(%s, %s, %s, %s, %s, %s, %s, %s) "\
        f"ON CONFLICT (user_id) DO NOTHING"
        async with self.connector.cursor() as curs:
            await curs.execute(query, (user_id, name, last_name, zip_code, plan, phone, longitude, latitude))
            await self.connector.commit()