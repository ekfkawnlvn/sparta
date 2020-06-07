import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/month/index.htm#params%5Bidx%5D=1&params%5BrankMonth%5D=202004&params%5BisFirstDate%5D=false&params%5BisLastDate%5D=true',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music_all = soup.select('#lst50')
#lst50 > td:nth-child(2) > div > span.rank
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a
for music in music_all:
    rank = music.select_one('td > div > span.rank')
    name = music.select_one('td > div > div > div.ellipsis.rank01 > span > a')
    singer = music.select_one('td > div > div > div.ellipsis.rank02 > a')
    if music is not None:
        print(rank.text, name.text, singer.text)