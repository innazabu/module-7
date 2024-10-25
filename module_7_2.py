def custom_write(file_name, strings):
    file = open(file_name, 'a')
    c = 0
    b = 0
    strings_positions = {(0,0): ''}

    for i in strings:
        c += 1
        b = file.tell()
        file.write(i + '\n')
        strings_positions[(c, b)] = i

    del strings_positions[(0,0)]


    file.close()

    return strings_positions

    

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
