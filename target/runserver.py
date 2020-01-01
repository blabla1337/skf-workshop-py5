#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
from flask_cors import CORS

app.config.update(dict(
    SECRET_KEY= "woopie",
    SESSION_COOKIE_HTTPONLY = False,
    DEBUG= True
))


if __name__ == '__main__':
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.run(host='0.0.0.0')

