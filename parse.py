"""
Программа парсинга файлов (Report:Assigned Modules) DeltaV в
.csv- файл для послеющего импорта в excel.

txt. файлы из DeltaV необходимо пересохранить в кодировке UTF-8

Для исполнения программы использовать интерпретатор PYTHON 3 версии
Скрипт запускать в одной папке с файлами.

Примеры команды запуска из консоли:
python parse.py
python3 parse.py
py parse.py
py3 parse.py

Или же двойным нажатием на иконке файла parse.py
"""
import os
import csv

"""В этой переменной указываем имена файлов (массив строк) """
FILE_NAMES = ['40127-DCS-01-01A.txt',
              '40127-DCS-01-02A.txt',
              '40127-ESD-01-03A.txt',
              '40127-ESD-01-04A.txt']



def parse_data(file_list):
    data_files = []
    dict = {}
    csv_columns = ['Name', 'Description', 'Node Assignment']
    for i in range(len(file_list)):
        if os.path.isfile(file_list[i]):
            f = open(file_list[i], encoding='utf-8')

            for line in f:
                raw = line.split(':')

                if raw[0] == 'Name':
                    dict[raw[0]] = raw[1].strip()

                if raw[0] == 'Description':
                    dict[raw[0]] = raw[1].strip()

                if raw[0] == 'Node Assignment':
                    dict[raw[0]] = raw[1].strip()
                    data_files.append(dict)
                    dict = {}

            f.close()
            if len(data_files) > 0:
                csv_file_name = 'csv' + file_list[i].split('.')[0] + '.txt'
                print(csv_file_name)
                try:
                    with open(csv_file_name, 'w') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                        writer.writeheader()
                        for data in data_files:
                            writer.writerow(data)
                except IOError:
                    print("Ошибка ввода/вывода при создании файла .csv")
            data_files = []
            dict = {}
        else:
            print('Файла не существует')

if __name__ == '__main__':
    parse_data(FILE_NAMES)
