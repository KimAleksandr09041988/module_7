def  custom_write(file_name: str, strings: list):
    strings_positions = {}
    file = open(file_name, 'a+', encoding='utf-8')
    i = 1
    for item in strings:
        strings_positions[(i,file.tell())] = item
        file.write(f'{item}\n')
        i += 1
    file.close()
    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
