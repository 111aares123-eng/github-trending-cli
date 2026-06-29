import requests
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument("--duration", default="week")
parser.add_argument("--limit", default=5, type=int)
parser.add_argument("--language", default=None)
args = parser.parse_args()

duration_days = {
    "day": 1,
    "week": 7,
    "month": 30,
    "year": 365
}

days = duration_days[args.duration]
since = datetime.now() - timedelta(days=days)
date_str = since.strftime("%Y-%m-%d")

query = "created:>" + date_str
if args.language:
    query = query + " language:" + args.language

response = requests.get("https://api.github.com/search/repositories?q=" + query + "&sort=stars&order=desc&per_page=" + str(args.limit))

data = response.json()
repos = data["items"]

for repo in repos:
    print(repo["full_name"], "⭐", repo["stargazers_count"])
    print(repo["description"])
    print()