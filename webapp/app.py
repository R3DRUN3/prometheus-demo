from flask import Flask  
from flask import render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by='endpoint')

@app.route("/")
def coding_notes_app():  
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8887, host="0.0.0.0")
