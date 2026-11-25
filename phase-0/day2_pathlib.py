from pathlib import Path


curr_dir = Path.cwd()
# print(curr_dir)

# file_path = Path(__file__).resolve()



print(Path.cwd())
print(Path(__file__).resolve().parent)


path = Path("history.json")

print(path.name)
print(path.stem)
print(path.suffix)
print(path.exists())


BASE_DIR = Path(__file__).resolve().parent

for file in BASE_DIR.glob("*.py"):
    print(file.name)