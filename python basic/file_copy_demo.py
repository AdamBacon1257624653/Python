source_file = open("README.md")
target_file = open("README-copied", "a")
while True:
    content = source_file.readline()
    if not content:
        break
    target_file.write(content)
source_file.close()
target_file.close()
print("=" * 50)
print("Copy Completed")
