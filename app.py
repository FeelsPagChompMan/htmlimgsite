from flask import Flask
from views import *
from main import *

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")
app.register_blueprint(main, url_prefix="/home")

if __name__ == '__main__':

    app.run(debug=True, port=8000)
