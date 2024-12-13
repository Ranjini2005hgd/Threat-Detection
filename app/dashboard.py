from flask import Flask, render_template
import logging

app = Flask(__name__)

@app.route('/')
def index():
    # Read the logs for threat detection events
    with open('logs/traffic_logs.log', 'r') as f:
        logs = f.readlines()

    return render_template('dashboard.html', logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
