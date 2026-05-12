from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "service": "analytics-service",
        "message": "Analytics service works"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)