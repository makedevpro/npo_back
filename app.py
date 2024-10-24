# server.py
import json
import random
import time

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Для разрешения запросов с другого домена (Vue)


@app.route('/api/data', methods=['GET'])
def get_data():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    value = random.randrange(0, 100)
    data = {
        'time': current_time,
        'value': value
    }
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
