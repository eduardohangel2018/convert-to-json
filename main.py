# -*- coding: utf-8 -*-
import json, os
from funcs import format_date, convert_size

print("------------------")
print("------Movies------")
print("------------------")


def convert_value():
    if not os.path.isfile('movies.txt'):
        print("O arquivo movies.txt não existe")
        return

    movie_dict = {}

    with open('movies.txt', 'r', encoding='utf-8') as file:
        for line in file:
            values = line.strip().split()
            if len(values) < 5:
                continue
            name = values[0]
            date = values[1]
            path = values[2]
            director = values[3]
            size = values[4]

            movie_dict[name] =  {'name': name, 'date': format_date(date), 'path': path, 'director': director, 'size': convert_size(size)}

        with open('new_movies.json', 'w') as file:
            json.dump(movie_dict, file)


if __name__ == "__main__":
    convert_value()