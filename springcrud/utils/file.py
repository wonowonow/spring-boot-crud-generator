import os

def make_dirs(path):
    os.makedirs(path, exist_ok=True)

def to_path(package):
    return package.replace(".", "/")

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)
