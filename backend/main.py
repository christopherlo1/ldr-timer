print("Hello world")

# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/api/status')
def get_status():
    # This is an example API endpoint.
    # In a real app, you might fetch user data or saved timers here.
    return {'status': 'Server is running'}

if __name__ == '__main__':
    app.run(debug=True)