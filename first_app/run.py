from app import app

import sys

d = sys.path

app.run(host="0.0.0.0", port=8080, debug=True)
