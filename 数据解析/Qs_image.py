#!/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import os

def init_conf(page_type, url):
    url = url
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    if page_type == 'text':
        page_text = requests.get(url=url, headers=headers)
        return page_text.text
    elif page_type == 'content':
        for img in url:
            img = "https:" + img
            content = requests.get(url=img, headers=headers).content
            save_data(content, img.split('/')[-1])
            print(f"{img.split('/')[-1]} 下载成功！！！" )
    else:
        print(f"{page_type} error!!")


def data_clean(page):
    data = re.findall('<div class="thumb">.*?src="(.*?)" alt=.*?', page, re.S)
    return data


def save_data(data, filename):
    with open(f'./qiushi/{filename}', mode='wb') as f:
        f.write(data)


def create_dir():
    if not os.path.exists('./qiushi'):
        os.mkdir('./qiushi')

if __name__ == '__main__':
    # save_data(init_conf())
    #color_red = f'\033[41;1m{}\033[0m'
    create_dir()
    start_page = int(input('start page: '))
    end_page = int(input('end page: '))
    for page in range(start_page, end_page + 1):
        url = f'https://www.qiushibaike.com/imgrank/page/{page}/'
        s = f'download page {page} picture'
        print(f'{s}'.center(40, '-'))
        page_text = init_conf('text', url)
        image_url = data_clean(page_text)
        init_conf('content', image_url)
    # save_data(image_data, filename)
