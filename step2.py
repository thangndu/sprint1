#!/usr/bin/env python3
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainmenu():

    response = """
    <html>
        <body>
            <h1>Hello Cloud Native World</h1>
            <br>
            <img src="static/piper.png">
        </body>
    </html>
    """

    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
