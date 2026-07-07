import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import argparse
from trending_repos import get_trending_repos
from display import show_repos

def main():
    parser=argparse.ArgumentParser(description="Show github trending repositories")
    parser.add_argument("--duration", default="week", choices=["day","week","month", "year"])
    parser.add_argument("--limit",default = 5, type=int)
    parser.add_argument("--language", default=None)
    args=parser.parse_args()

    repos=get_trending_repos(
        duration=args.duration,
        limit=args.limit,
        language=args.language
    )
    show_repos(repos)

if __name__=="__main__":
    main()
    
