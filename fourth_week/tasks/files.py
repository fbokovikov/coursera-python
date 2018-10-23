from tempfile import gettempdir
from os.path import join


class File:

    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return self.filename

    def write(self, string):
        with open(self.filename, 'w') as f:
            f.write(string)

    def __iter__(self):
        with open(self.filename) as f:
            return iter(f.readlines())

    def __add__(self, obj):
        with open(self.filename) as first_file:
            first_content = first_file.read()

        with open(obj.filename) as second_file:
            second_content = second_file.read()

        content = first_content + second_content

        dir = gettempdir()
        full_path = join(dir, self.filename)
        new_file = File(full_path)
        new_file.write(content)
        return new_file


if __name__ == "__main__":
    file = File("test")
    print(file)

    file.write("value")

    for line in file:
        print(line)

    file2 = File("test_2")
    file2.write("qwerty")

    file3 = file + file2
    for line in file3:
        print(line)
