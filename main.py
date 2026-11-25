import os

LINE = "My therapist says talking to my plants is healthy, so I haven't mentioned they talk back — and they're unionizing."

assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

try:
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass
