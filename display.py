# from sys import argv

# script, file = argv

# Print the content of the file.
def read(file):
    with open(file, 'r') as f:
        data = f.read()
        print(data)

if __name__ == "__main__":
    pass
