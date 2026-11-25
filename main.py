import os

ENTRY = "I pushed your untested code to main at 4:59 PM on a Friday. Production is down. Good news: your weekend is now free. Permanently."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
