#!/usr/bin/env python3

from flask import request
from config import app, db 
# from models import MODELS GO HERE


# write your routes here!


if __name__ == '__main__':
    app.run(port=5555, debug=True)
