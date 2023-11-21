file ="golf.txt"

with open(file, 'r') as file:
    for line in file:
        print(line.strip())