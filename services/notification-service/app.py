from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "service": "notification-service",
        "message": "Notification service works"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)