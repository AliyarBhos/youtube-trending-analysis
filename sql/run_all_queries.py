import pandas as pd
from sqlalchemy import create_engine, text
import sys
sys.path.append('..')
from config import DB_CONFIG

engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['username']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

with open("analysis.sql", "r", encoding="utf-8") as f:
    sql_text = f.read()

# split queries by semicolon
queries = [q.strip() for q in sql_text.split(";") if q.strip()]


for i, query in enumerate(queries, start=1):
    df = pd.read_sql(query, engine)
    
    filename = f"../data/cleaned/q{i}.csv"
    df.to_csv(filename, index=False)
    
    print(f"Saved Q{i} → {filename} ({len(df)} rows)")