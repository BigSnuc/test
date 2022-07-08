giimport requests
from bs4 import BeautifulSoup as BS
topDiary = {}

my_url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&filefrom=%D0%90&subcatuntil=%D0%90&pageuntil=%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D0%BF%D0%B0%D1%80%D0%B0%D0%BB%D0%B8%D1%85%D1%82#mw-pages'
def parse(URL):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BS(response.content, 'html.parser')
    mainDiv = soup.find('div', id = 'mw-pages').find_all('li')
    comps = []
    for item in mainDiv:
        try:
            comps.append({
                'title': item.get_text(strip = True)
            })
        except:
            continue
    for comp in comps:
        if topDiary.get(comp['title'][0]) == None:
            topDiary[comp['title'][0]] = 1
        else:
            topDiary[comp['title'][0]] = topDiary.get(comp['title'][0]) + 1
    new_bs_url = soup.find('div', id = 'mw-pages').find('a', text = 'Следующая страница').get('href')
    new_bs_url = 'https://ru.wikipedia.org/' + new_bs_url
    try:
        return parse(new_bs_url)
    except:
        return
parse(my_url)
sorted_dict = {key:topDiary[key] for key in sorted(topDiary)}
#########################
#########################
a = ord('а')
y = ''.join([chr(i) for i in range(a, a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)])
y = str.upper(y)


for x in range(len(y)):
    print(y[x], ': ', sorted_dict.get(y[x]))


a = ord('a')
y = ''.join([chr(i) for i in range(a,a+25)])
y = str.upper(y)
for x in range(len(y)):
    print(y[x], ': ', sorted_dict.get(y[x]))

