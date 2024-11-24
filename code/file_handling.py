file_path = "example.txt"

try:
    with open(file_path, "r") as file:
        contnt = file.read()
        print(contnt)
except FileNotFoundError:
    print("file not found")

