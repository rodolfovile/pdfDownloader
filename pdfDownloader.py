import requests
import os
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen




url = 'http://stock.ethop.org/pdf/python/'
#cria uma pasta para fazer o download
os.makedirs('PAST_DOWNLOAD', exist_ok=True)
html = urlopen("http://stock.ethop.org/pdf/python/")
soup = BeautifulSoup(html)


for tag in soup.findAll('a', href=True):
    for link in tag:
        if '.pdf' in link:
            #concatena os href achados nos links
            postUrl = 'http://stock.ethop.org/pdf/python/' + link
            print('Fazendo download do livro %s...' % (postUrl))
            res = requests.get(postUrl)
            res.raise_for_status()

            pdfFile = open(os.path.join('PAST_DOWNLOAD', os.path.basename(postUrl)), 'wb')
            for chunck in res.iter_content(1000000):
                pdfFile.write(chunck)
            pdfFile.close()


print("MAL FEITO, FEITO!!")









   
