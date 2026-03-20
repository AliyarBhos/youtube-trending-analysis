import pandas as pd
from sqlalchemy import create_engine, text
import sys
sys.path.append('..')
from config import DB_CONFIG

engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['username']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

df = pd.read_csv('../data/cleaned/videos_cleaned.csv')

df['trending_date'] = pd.to_datetime(df['trending_date'])
df['publish_date']  = pd.to_datetime(df['publish_date'])

df.to_sql(
    name = 'videos',
    con = engine,
    if_exists = 'replace',   
    index=False,
    chunksize = 1000          
)

print("Done! Rows loaded:", len(df))