import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('div.newest-list > div > table > tbody > tr')

for music in musics:
    if music is not None:
    
        rank = music.select_one('td.number')
        rank = rank.text.split(' ')[0].replace("\n","")
        name = music.select_one('td.info > a.title.ellipsis')
        singer = music.select_one('td.info > a.artist.ellipsis')
        
        print(rank, name.text.strip(), singer.text.strip())
