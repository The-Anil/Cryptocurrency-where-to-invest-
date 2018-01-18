import urllib.request
from re import findall

with urllib.request.urlopen('https://coinmarketcap.com/') as response:
    html = response.read()
    strHTML = html.decode()       #Convert to a string
#print(html)



value = float(strHTML.split('<a href="/currencies/bitcoin/#markets" class="price" data-usd="11401.2" data-btc="1.0" >$')[1].split('</a>')[0])
print(value)

#ndata = findall('<a href="/currencies/[A-Za-z]+/#markets" class="price" data-usd="[0-9]+.[0-9]+" data-[A-Za-z]+="1.0" >$',strHTML)

ndata = findall('<a href="/currencies/bitcoin/#markets" class="price" data-usd="11401.2" data-btc="1.0" >$',strHTML)
print(ndata)

for item in ndata:
    print(item)