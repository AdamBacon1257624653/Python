find_name = "Tom"
names = ["Peter", "Tom", "Julie"]
for name in names:
    if name == find_name:
        print(find_name + " is in the list")
        break
else:
    print("No Result!")
print("Search completed")
