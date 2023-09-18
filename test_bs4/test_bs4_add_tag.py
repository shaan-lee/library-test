import re
from bs4 import BeautifulSoup


html = """
<div class="col"><div class="list-item"><a href="/movie/guardians-of-the-galaxy-vol-3-6105" class="list-media"><div class="list-media-attr"><div class="imdb"><svg class="icon"><use xlink:href="/static/img/sprite.svg#star"></use></svg> N/A </div></div><div class="play-btn"><svg class="icon"><use xlink:href="/static/img/sprite.svg#play"></use></svg></div><div class="media media-cover" style="background-image: url('https://static.soap2day-official.com/FHT:xxrz/250x400/379/91/67/91670229ac9f3b6fb4d242d6b5511644/91670229ac9f3b6fb4d242d6b5511644.jpg')"></div></a><div class="list-caption"><span class="list-title">Guardians of the Galaxy Volume 3</span><div class="list-year"> 2023 • 150 min • HD </div></div></div></div>
"""

def get_soup(html):
    soup = BeautifulSoup(html,features="html.parser")
    return soup
    

def add_tag():
    soup = get_soup(html)
    div_background = soup.find("div", {"style":re.compile("^background")})
    background_style = div_background['style']
    print(background_style)
    img_url = re.findall(".*(http.*jpg).*",background_style)[0]
    print(img_url)
    new_tag = soup.new_tag("img",src=img_url)
    soup.insert(1,new_tag)
    print(soup)

add_tag()