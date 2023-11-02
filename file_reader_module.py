def file_reader_module(file_name):
    with open(file_name, encoding='utf-8') as file:
        keys = file.readline().strip().lower().split(';')
        lines = [line.strip().split(';') for line in file]
        return [dict(zip(keys, line)) for line in lines]  # noqa: B905

