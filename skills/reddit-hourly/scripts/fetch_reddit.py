#!/usr/bin/env python3
"""
Reddit Hourly Intel Fetcher
Fetches top posts from configured subreddits for hourly updates.
"""

import json
import urllib.request
import urllib.error
import sys
from datetime import datetime

# Subreddits to track
SUBREDDITS = [
    "coys",           # Spurs news/transfers
    "todayilearned",  # Interesting facts
    "unitedkingdom",  # UK news
    "olympics"        # Olympic updates (WinterOlympics often inactive)
]

REDDIT_USER_AGENT = "Mozilla/5.0 (compatible; OpenClaw-Bot/1.0; +https://openclaw.ai)"

def fetch_subreddit(subreddit, limit=3):
    """Fetch top posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    headers = {"User-Agent": REDDIT_USER_AGENT}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            posts = []
            for child in data.get('data', {}).get('children', []):
                post = child.get('data', {})
                posts.append({
                    'title': post.get('title', ''),
                    'url': f"https://reddit.com{post.get('permalink', '')}",
                    'score': post.get('score', 0),
                    'subreddit': subreddit
                })
            return posts
    except urllib.error.HTTPError as e:
        return [{'error': f'HTTP {e.code}', 'subreddit': subreddit}]
    except Exception as e:
        return [{'error': str(e), 'subreddit': subreddit}]

def format_posts(posts):
    """Format posts into a readable summary."""
    lines = [f"📊 Reddit Intel — {datetime.now().strftime('%H:%M %d/%m/%Y')}\n"]
    
    by_subreddit = {}
    for post in posts:
        sub = post.get('subreddit', 'unknown')
        if sub not in by_subreddit:
            by_subreddit[sub] = []
        by_subreddit[sub].append(post)
    
    subreddit_names = {
        'coys': '⚽ r/coys (Spurs)',
        'todayilearned': '🧠 r/todayilearned',
        'unitedkingdom': '🇬🇧 r/unitedkingdom',
        'olympics': '🏅 r/olympics'
    }
    
    for subreddit in SUBREDDITS:
        name = subreddit_names.get(subreddit, f"r/{subreddit}")
        lines.append(f"\n{name}")
        lines.append("─" * 30)
        
        posts_in_sub = by_subreddit.get(subreddit, [])
        if not posts_in_sub:
            lines.append("  No new posts")
            continue
            
        for post in posts_in_sub:
            if 'error' in post:
                lines.append(f"  ⚠️ Error: {post['error']}")
                continue
            title = post['title'][:60] + "..." if len(post['title']) > 60 else post['title']
            lines.append(f"  • {title}")
            lines.append(f"    👍 {post['score']} | {post['url']}")
    
    return "\n".join(lines)

def main():
    all_posts = []
    for subreddit in SUBREDDITS:
        posts = fetch_subreddit(subreddit)
        all_posts.extend(posts)
    
    output = format_posts(all_posts)
    print(output)
    return 0

if __name__ == "__main__":
    sys.exit(main())
