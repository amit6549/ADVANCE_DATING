import aiosqlite

DB_PATH = "dating.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                bio TEXT,
                location TEXT,
                gender TEXT,
                looking_for TEXT,
                stars INTEGER DEFAULT 5,
                subscription_until TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS likes (
                from_user INTEGER,
                to_user INTEGER,
                matched INTEGER DEFAULT 0
            )
        ''')
        await db.commit()
