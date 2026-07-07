import requests
from datetime import datetime, timedelta

def get_trending_repos(duration="week", limit=5, language=None):
    duration_days = {
        "day": 1,
        "week": 7,
        "month": 30,
        "year": 365
    }
    days = duration_days[duration]
    since = datetime.now() - timedelta(days=days)
    date_str = since.strftime("%Y-%m-%d")

    query = "created:>" + date_str
    if language:
        query = query + " language:" + language

    response = requests.get(
        "https://api.github.com/search/repositories?q=" + query +
        "&sort=stars&order=desc&per_page=" + str(limit)
    )
    data = response.json()
    return data["items"]