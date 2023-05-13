# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime


def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        date_str = date_obj.strftime('%d/%m/%Y')
    except ValueError:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        date_str = date_obj.strftime('%d/%m/%Y')
    return date_str


def convert_size(new_size: str) -> str:
    value = int(new_size) / 1024 / 1024 / 1024
    if value != '':
        return f"{value:.2f} GB"
    return f"{int(value)}GB"


def load_movies(all_movies):
    all_movies = {}
    if os.path.exists('new_movies.json'):
        with open('new_movies.json', 'r') as file:
            all_movies = json.load(file)
    return all_movies
