

def write_file(_file_name, _data):
    _file = open(_file_name, "w")
    _file.write(_data)
    _file.close()


def file_read(_file_name):
    with open(_file_name, "r") as _file:
        _data = _file.read()
        print(_data)


file_name = "sara's_file.txt"
data = 'Hey you,\nwhat are you looking for here?\nThis file is mine..'
write_file(file_name, data)
file_read(file_name)