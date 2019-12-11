def open_file(filename):
    with open(filename, encoding='utf-8') as content:
        return content.read()


def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)



