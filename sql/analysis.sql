-- Q1: Which categories appear in trending the most?
SELECT 
    category_name,
    COUNT(*) AS trending_appearances,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM videos
GROUP BY category_name
ORDER BY trending_appearances DESC;


-- Q2: Top 10 channels by average views
select 
	 channel_title,
	 count(distinct video_id) as total_videos,
	 round(avg(views)) as avg_views,
	 round(avg(like_ratio)::numeric, 2) as avg_like_ratio
from videos
group by channel_title
having count(distinct video_id) >= 5 -- channels 5+ videos
order by avg_views desc
limit 10;


-- Q3: How quickly do videos reach trending? (by category)
select 
    category_name,
    round(avg(days_to_trend), 1) as avg_days_to_trend,
    min(days_to_trend) as fastest,
    max(days_to_trend) as slowest
from videos
where days_to_trend between 0 and 60     
group by category_name
order by avg_days_to_trend asc;


-- Q4: Views vs engagement — correlation by region
select 
    region,
    round(avg(views)) as avg_views,
    round(avg(likes)) as avg_likes,
    round(avg(comment_count)) as avg_comments,
    round(avg(like_ratio)::numeric, 2) as avg_like_ratio,
    round(avg(comment_ratio)::numeric, 4) as avg_comment_ratio
from videos
group by region
order by avg_views desc;


-- Q5: Monthly trending volume over time
select 
    date_trunc('month', trending_date) as month,
    region,
    count(*) as trending_count
from videos
group by month, region
order by month, region;


-- Q6: Top 10 most consistently trending videos
select 
    title,
    channel_title,
    category_name,
    region,
    count(*) as days_in_trending
from videos
group by title, channel_title, category_name, region
order by days_in_trending desc
limit 10;


-- Q7: Do disabled comments/ratings affect views?
select 
    comments_disabled,
    ratings_disabled,
    count(*) as video_count,
    round(avg(views)) as avg_views,
    round(avg(like_ratio)::numeric,2) as avg_like_ratio
from videos
group by comments_disabled, ratings_disabled
order by avg_views desc;


-- Q8: Best performing category per region (window function)
select distinct on (region)
    region,
    category_name,
    round(avg(views) over (partition by region, category_name)) as avg_views,
    count(*)        OVER (partition by region, category_name)   as appearances
from videos
order by region, avg_views desc;