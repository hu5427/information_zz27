a = 1
b = 2
c = 3 
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def index():
    return 'hello world'

if __name__ == "__main__":
    app.run()
