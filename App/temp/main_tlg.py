#!/usr/bin/python
# -*- coding: utf-8 -*-
# TELEGRAM

import os
from bs4 import BeautifulSoup
import re


def get_files_name_in_folder():
    directory = './tlg_temp'
    listdir = os.listdir(directory)
    list_files_name = [i for i in listdir if re.match(r'messages', i)]
    return list_files_name


def get_page_html():
    # Номер обрабатываемой страницы из архива
    z = 0
    # Счетчик сообщений (сырые данные)
    # flag = 0
    list_files_name = get_files_name_in_folder()

    for file_name in list_files_name:
        f = open("./tlg_temp/" + file_name, 'r', encoding='utf-8')

        soup = BeautifulSoup(f, 'lxml')
        blocks = soup.find('div', 'history').find_all('div', 'message default clearfix')

        z += 1
        print(f'File: {z}', file_name, '\n')

        list_sms = []

        for block in blocks:
            # flag += 1
            # print(flag)
            try:
                date_time = block.find('div', 'body').find('div', 'pull_right date details').get('title')
                date_time = date_time.split()
                text = block.find('div', 'body').find('div', 'text').text.strip()
                print(date_time, text)

            except AttributeError:
                date_time = ''
                text = ''

            list_sms.append([*date_time, text])
        print()
        # break


if __name__ == '__main__':
    get_page_html()
