file = open("README.md", "a+")
# file.write("abc")
content = file.read()
print(content)
print("-" * 50)
print(file.read())
file.close()