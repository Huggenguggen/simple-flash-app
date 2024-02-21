from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
  image_url = requests.get('https://thispersondoesnotexist.com/').url 
  return render_template('index.html', image_url=image_url)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)