import re
import os
import sys

arg_list = sys.argv
path = arg_list[1]
re_author_name = r'\[(.*)\]'
re_book_title = r'\]_(.*)\(z'

with os.scandir(path) as list_file:
    for file in list_file:
        if not file.name.startswith('.') and file.is_file() and 'lib.org' in file.name:

            file_name = file.name

            author_name = re.search(re_author_name, file_name)
            author_name = author_name.group(1)
            author_last_name = author_name.split('_')
            author_last_name = author_last_name[-1]

            book_title = re.search(re_book_title, file_name)
            book_title = book_title.group(1)
            book_title = book_title.replace('_', ' ')

            clean_file_name = book_title + ' - ' + author_last_name
            extension = os.path.splitext(file_name)[1]

            print(file, clean_file_name + extension)
            os.rename(path + '/' + file.name, path + '/' + clean_file_name + extension)
