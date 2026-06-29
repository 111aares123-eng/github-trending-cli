import requests
from datetime import datetime, timedelta

week_ago=datetime.now() - timedelta(days=7)
date_str=week_ago.strftime("%Y-%m-%d")
print(date_str)

response = requests.get("https://api.github.com/search/repositories?q=created:>2025-06-22&sort=stars&order=desc&per_page=5")

data = response.json()

repos=data["items"]

for repo in repos:
    print(repo["full_name"],"⭐",repo["stargazers_count"])
    print(repo["description"])
    print()

