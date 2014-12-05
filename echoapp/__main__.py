from __future__ import unicode_literals
import os
import pprint
import StringIO

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def echo():
    stream = StringIO.StringIO()
    indent = int(os.environ.get('PRINT_INDENT', 1))
    pprint.pprint(request.environ, indent=indent, stream=stream)
    return stream.getvalue()


def main():
    app.run(
        host=os.environ.get('HTTP_HOST', '0.0.0.0'),
        port=int(os.environ.get('HTTP_PORT', 80)),
        debug=int(os.environ.get('DEBUG', 0)),
    )

if __name__ == "__main__":
    main()
