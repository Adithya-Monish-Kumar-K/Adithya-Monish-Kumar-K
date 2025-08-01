import requests, re

USERNAME = "Adithya_Monish_Kumar_K"
README  = "README.md"

# Fetch profile page
res = requests.get(f"https://leetcode.com/{USERNAME}/")
# Extract current streak (update regex if LeetCode HTML changes)
match = re.search(r'"streak":[ ]*([0-9]+)', res.text)
streak = match.group(1) if match else "0"

# New badge URL
new_badge = (
    "https://github-readme-streak-stats.herokuapp.com"
    f"?user=Adithya_Monish_Kumar_K&theme=dark&date_format=M%20j%5B%2C%20Y%5D&streak={streak}"
)

# Replace existing badge URL in README.md
with open(README, "r", encoding="utf-8") as f:
    content = f.read()
content = re.sub(
    r"https://github-readme-streak-stats\.herokuapp\.com\?[^)]+",
    new_badge,
    content
)
with open(README, "w", encoding="utf-8") as f:
    f.write(content)
