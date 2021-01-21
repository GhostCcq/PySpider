#!/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com/s'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    kw = input('Search KeyWord: ')
    param = {
        'wd': kw
    }
    response = requests.get(url=url, params=param, headers=headers)

    with open(f'./data/{kw}.html', mode='w', encoding='utf-8') as f:
        f.write(response.text)
    print('爬取完成！')