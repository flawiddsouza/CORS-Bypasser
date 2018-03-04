from flask import Flask, request
from flask_cors import CORS
import requests
import requests_cache
import os

app = Flask(__name__)
CORS(app)

requests_cache.install_cache(os.path.join(os.path.dirname(__file__), 'the_cache'))

@app.route('/<path:url>')
def catch_all(url):
    try:
        if request.query_string:
           url  = url + '?' + request.query_string.decode('utf-8')
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers).text
        return response
    except ValueError:
        return "Invalid URL"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9877, threaded=True)