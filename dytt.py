#!/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
import os
import json

def get_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    try:
        page = requests.get(url=url, headers=headers).content
        # print(page.decode('gbk'))
        return page.decode('gbk')
    except Exception as e:
        print('网络连接失败，轻稍后重试！')
        print(f'错误信息：{e}')

def clear_data(data):
    obj = re.compile(r"最新电影下载</a>]<a href='(?P<url>.*?)'>", re.S)
    it = obj.finditer(data)
    #print(it)
    movies = []
    for i in it:
        detail_url = 'https://www.dytt8.net' + i.group('url')

        try:
            data = get_url(detail_url)
            #print(data)
            movies_info = detail_page(data)
            movies.append(movies_info)
            #return movies_info
        except Exception as e:
            print(e)
    return movies

def detail_page(detail_data):
    obj = re.compile(r'<div id="Zoom".*?◎译　　名(?P<film_name>.*?)<br />.*?◎主　　演(?P<actors>.*?)<br /><br />.*?<a href="(?P<download_url>.*?)"', re.S)
    detail_data = obj.finditer(detail_data)
    movie = {}
    try:
        for item in detail_data:
            movie['FilmName'] = item.group('film_name').replace('\u3000', '')
            movie['Actors'] = item.group('actors').replace('&middot', '').replace('\u3000', '').replace('&nbsp', '').replace(';', '').split('<br />')
            movie['MagnetURI'] = item.group('download_url')
        print(f"当前正在爬取：{movie.get('FilmName')}")
        return movie
    except Exception:
        pass

def save_data(data):
    dir = './data/dytt'
    if not os.path.exists(dir):
        os.mkdir(dir)

    fp = open(f'{dir}/dytt.json', mode='w', encoding='utf-8')
    json.dump(data, fp=fp, ensure_ascii=False)

    fp.close()
    print('数据保存完成！')

if __name__ == '__main__':
    page = get_url('https://www.dytt8.net/index.htm')
    movies_info = clear_data(page)
    save_data(movies_info)