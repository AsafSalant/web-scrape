from flask import Flask, request, jsonify
import newspaper
from newspaper import Article
app = Flask(__name__)

@app.route('/get-text-from-links', methods=['POST'])
def hello_world():
    if request.is_json:
        urls = request.get_json()
        texts = []
        for url in urls:
            article = Article(url)
            article.download()
            article.parse()
            texts.append(article.text)
    
        return jsonify(texts), 200
    else:
        return jsonify({'error': 'Invalid JSON data'}), 400
