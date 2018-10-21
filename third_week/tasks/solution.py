class FileReader:
    """Класс FileReader помогает читать из файла"""

    def __init__(self, filename):
        self._filename = filename

    def read(self):
        try:
            with open(self._filename) as file:
                return file.read()
        except FileNotFoundError:
            return ""


if __name__ == "__main__":
    fileReader = FileReader("/Users/fbokovikov/xls2csv.sh")
    print(fileReader.read())
