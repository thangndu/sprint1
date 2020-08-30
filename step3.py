#!/usr/bin/env python3
import os
from flask import Flask

app = Flask(__name__)

GREEN = "#99CC99"

COLOR = GREEN

@app.route('/')
def mainmenu():

    response = """
    <html>
        <body bgcolor="{color}">
            <h1>Hello Cloud Native World</h1>
            <br>
            <a href="piper.html">Click Me!!!</a>
        </body>
    </html>
    """.format(color=COLOR)

    return response

@app.route('/piper.html')
def piper():

    return """
    <html>
        <body>
            <img src="static/piper.png">
    
        </body>
    </html>
    """


if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
