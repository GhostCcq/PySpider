#!/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

def get_movie_rank(start, limit):
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': select_movie_type(),
        'interval_id': '100:90',
        'action': '',
        'start': start,
        'limit': limit
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url=url, params=params, headers=headers)
    movies_data = response.json()
    fp = open('./data/douban_movie_rank.txt', mode='a', encoding='utf-8')
    for movies in movies_data:
        movies_info = f"排名: {movies['rank']}, 片名: {movies['title']}, 评分: {movies['rating'][0]},  url: {movies['url']}"
        json.dump(movies_info, fp=fp, ensure_ascii=False)
        print(movies_info)

def select_movie_type():
    rank_type = [
        {'剧情': '11'},
        {'喜剧': '24'},
        {'动作': '5'},
        {'爱情': '13'},
        {'科幻': '17'},
        {'动画': '25'},
        {'悬疑': '10'},
        {'惊悚': '19'},
        {'恐怖': '20'},
        {'纪录片': '1'}
    ]
    for num in range(0, len(rank_type)):
        type_name, = rank_type[num]
        print(f'编号: {num}, 类型: {type_name}')
    print('选择电影类型'.center(20, '-'))
    type_num = input('请输入电影类型对应的编号：')

    try:
        return rank_type[int(type_num)].values()
    except Exception as e:
        print('请输入正确的编号！！！')


if __name__ == '__main__':
    start = input('起始排名编号: ')
    limit = input('获取多少部电影: ')
    get_movie_rank(start, limit)