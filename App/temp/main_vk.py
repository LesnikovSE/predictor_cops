#!/usr/bin/python
# -*- coding: utf-8 -*-
# VKONTAKTE

import os
from bs4 import BeautifulSoup


def get_page_name_in_folder():
    directory = './vk_temp'
    list_name_files = os.listdir(directory)

    return list_name_files


def get_page_html():
    z = 0
    list_page_name = get_page_name_in_folder()

    for file_name in list_page_name:
        f = open("./vk_temp/" + file_name)

        soup = BeautifulSoup(f, 'lxml')
        blocks = soup.find_all('div', 'item')

        z += 1
        print(f'File №: {z}', file_name, '\n')

        list_sms = []

        for block in blocks:
            list_sms.append([a.text.strip() for a in block.find('div', 'message').find_all('div')])

        for i in list_sms:
            name = i[0].strip().split(',')
            name = name[1].strip().split(' в ')
            print(name, i[1])

        break


if __name__ == '__main__':
    get_page_html()
