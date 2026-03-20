# youtube-trending-analysis
End-to-end analysis of 120,000+ YouTube trending videos across US, UK and India — Python, PostgreSQL, Power BI
=======
# YouTube Trending Videos Analysis

## Overview
Analysis of 120,000+ trending videos across US, UK, and India
to uncover what makes a video trend on YouTube.

## Key Findings
- Entertainment and Music account for 45% of all trending videos
- US videos average 2.1M views vs IN at 800K
- Videos trend fastest in the News category (avg 1.2 days)
- High like ratio (5%+) videos get 3x more comments on average

## Tech Stack
- Python (Pandas, Matplotlib, Seaborn) — data cleaning & EDA
- PostgreSQL — data storage & analytical queries  
- Power BI — interactive dashboard

## Dashboard Preview
![Dashboard](data/cleaned/dashboard_screenshot.png)

## Project Structure
data/ → raw and cleaned datasets
notebooks/ → Jupyter cleaning & EDA notebook
sql/ → schema, indexes, 8 analytical queries
dashboard/ → Power BI .pbix file