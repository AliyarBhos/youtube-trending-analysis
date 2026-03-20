import pandas as pd
from sqlalchemy import create_engine, text
import sys
sys.path.append('..')
from config import DB_CONFIG

engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['username']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

with engine.connect() as conn:
    conn.execute(text("""
        CREATE INDEX IF NOT EXISTS idx_region 
            ON videos(region);
        CREATE INDEX IF NOT EXISTS idx_category 
            ON videos(category_name);
        CREATE INDEX IF NOT EXISTS idx_trending_date 
            ON videos(trending_date);
        CREATE INDEX IF NOT EXISTS idx_channel 
            ON videos(channel_title);
    """))
    conn.commit()

print("Indexes created!")