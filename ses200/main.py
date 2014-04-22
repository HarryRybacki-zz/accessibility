import os

from flask import Flask

# Setup app
app = Flask(__name__)


# Import views
from views import *
if __name__ == '__main__':
    app.run(debug=True)
