import os

LINE = "My AI agent beat the GTA 6 launch queue by joining the in-game police and arresting my own character for loitering outside the store."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
