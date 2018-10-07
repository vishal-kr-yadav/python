import requests,re
from bs4 import BeautifulSoup
from collections import Counter
pattern = ['[^!.",?]+']

def remove_punctuation(pattern, phrase):
    for pat in pattern:
        return (re.findall(pat, phrase))
        return ('\n')
def extract_aff_content(url):

    website = requests.get(url)
    soup = BeautifulSoup(website.content)
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    l=[]
    import re,unicodedata
    # fileName=url.split('/')[4]
    fileName=str(5)

    f = open(fileName+'.txt', "a")
    for item in text:
        # if "$" in item
        aa="".join(remove_punctuation(pattern, re.sub('\s+',' ',item)))
        print(type(aa))
        f.write(unicodedata.normalize('NFKD', aa).encode('ascii','ignore'))

        # print(re.sub('\s+',' ',item))
        l.append(re.sub('\s+',' ',item))

    f.close
    return l

url_list=['https://www.forbes.com/sites/dominicdudley/2018/09/27/diplomatic-win-over-germany-saudi-arabia-apology-canada/#340e7dd945bf',
          'https://www.thenational.ae/business/aviation/exclusive-saudi-arabia-s-flyadeal-to-finalise-50-jet-order-in-october-as-it-looks-to-hire-female-cabin-crew-1.770815',
          'https://www.khaleejtimes.com/region/saudi-arabia/Dubais-Burj-Khalifa-lights-up-/with-Saudi-flag-colours',
          'https://www.forbes.com/sites/dominicdudley/2018/09/27/diplomatic-win-over-germany-saudi-arabia-apology-canada/#78fbd0b245bf',
          'https://www.si.com/wrestling/2018/09/18/wwe-crown-jewel-saudi-arabia-brock-lesnar-roman-reigns-braun-strowman'
          ]

for each in url_list:
    counter=0
    content = extract_aff_content(each,counter)
    counter+=1

