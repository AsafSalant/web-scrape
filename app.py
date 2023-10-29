from flask import Flask
import newspaper
from newspaper import Article
app = Flask(__name__)





@app.route('/')
def hello_world():
    urls = ['https://www.theiwsr.com/key-trends-for-wine-in-2023-and-beyond/','https://8wines.com/blog/wine-trends-everything-you-need-to-know','https://www.wineandmore.com/stories/global-wine-trends/']
    texts = []
    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        texts.append(article.text)
    
    return texts
