#!/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url = 'https://fanyi.baidu.com/sug'
    kw = input('enter translate keyword: ')
    data = {
        'kw': kw
    }

    response = requests.post(url=url, data=data, headers=headers)

    with open('./data/baidutranslate.txt', mode='a', encoding='utf-8') as f:
        f.write(f'{kw}:\n')
        f.write(json.dumps(response.json(), ensure_ascii=False) + '\n')
    print('翻译完成！')