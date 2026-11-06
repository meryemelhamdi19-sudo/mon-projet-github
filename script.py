
from pathlib import Path
file=Path("file.txt")
if file.exists():
    count = int(file.read_text().split(":")[1])
else:
    count=0

count+=1
file.write_text(str(count))
print(f"execution number : {count}")
