#!/usr/bin/env python3
"""
Reddit Hourly Intel Fetcher - Raw Headlines Edition
Fetches top posts from configured subreddits with full titles and direct links.
"""

import json
import urllib.request
import urllib.error
import sys
from datetime import datetime

# Subreddits to track
SUBREDDITS = [
    "coys",
    "todayilearned",
    "unitedkingdom",
    "olympics"
]

REDDIT_USER_AGENT = "Mozilla/5.0 (compatible; OpenClaw-Bot/1.0; +https://openclaw.ai)"

def fetch_subreddit(subreddit, limit=5):
    """Fetch hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    headers = {"User-Agent": REDDIT_USER_AGENT}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            posts = []
            for child in data.get('data', {}).get('children', []):
                post = child.get('data', {})
                # Skip stickied/pinned posts
                if post.get('stickied'):
                    continue
                posts.append({
                    'title': post.get('title', '').strip(),
                    'permalink': f"https://reddit.com{post.get('permalink', '')}",
                    'url': post.get('url', ''),
                    'score': post.get('score', 0),
                    'subreddit': subreddit
                })
            return posts
    except Exception as e:
        return [{'error': str(e), 'subreddit': subreddit}]

def format_posts(posts):
    """Format posts with full titles and links."""
    lines = [
        f"📰 Reddit Hourly — {datetime.now().strftime('%H:%M, %A %d %B')}\n",
        "=" * 50
    ]
    
    by_subreddit = {}
    for post in posts:
        sub = post.get('subreddit', 'unknown')
        if sub not in by_subreddit:
            by_subreddit[sub] = []
        by_subreddit[sub].append(post)
    
    subreddit_emoji = {
        'coys': '⚽',
        'todayilearned': '🧠',
        'unitedkingdom': '🇬🇧',
        'olympics': '🏅'
    }
    
    for subreddit in SUBREDDITS:
        emoji = subreddit_emoji.get(subreddit, '📌')
        lines.append(f"\n{emoji} r/{subreddit}")
        lines.append("─" * 50)
        
        posts_in_sub = by_subreddit.get(subreddit, [])
        if not posts_in_sub:
            lines.append("No posts")
            continue
            
        for i, post in enumerate(posts_in_sub, 1):
            if 'error' in post:
                lines.append(f"Error: {post['error']}")
                continue
            
            # Full title, no truncation
            title = post['title']
            score = post['score']
            reddit_link = post['permalink']
            
            lines.append(f"\n{i}. {title}")
            lines.append(f"   👍 {score} | <{reddit_link}>")
            
            # Show external link if different from Reddit discussion
            external_url = post.get('url', '')
            if external_url and external_url != reddit_link:
                lines.append(f"   🔗 External: <{external_url}>")
    
    lines.append("\n" + "=" * 50)
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
