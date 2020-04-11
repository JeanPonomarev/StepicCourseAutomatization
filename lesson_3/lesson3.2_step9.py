s = "My name is Julia"

if "name" in s:
    print("Substring found")

index = s.find("name")
if index != -1:
    print(f"Substring found at index {index}")
