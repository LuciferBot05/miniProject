from flask import Flask, render_template_string
import datetime

app = Flask(name)

waste_data = {
    "battery": 0,
    "cable": 0,
    "mobile": 0,
    "circuit_board": 0
}

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart E-Waste Dashboard</title>
    <meta http-equiv="refresh" content="2">
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
        }
        h1 {
            color: #22c55e;
        }
        .container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        .card {
            background: #1e293b;
            padding: 20px;
            margin: 15px;
            border-radius: 15px;
            width: 200px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
        }
        .count {
            font-size: 35px;
            color: #38bdf8;
        }
    </style>
</head>
<body>

<h1>♻️ Smart E-Waste Dashboard</h1>
<p>{{ time }}</p>

<div class="container">

    <div class="card">
        <h2>Battery</h2>
        <p class="count">{{ data["battery"] }}</p>
    </div>

    <div class="card">
        <h2>Cable</h2>
        <p class="count">{{ data["cable"] }}</p>
    </div>

    <div class="card">
        <h2>Mobile</h2>
        <p class="count">{{ data["mobile"] }}</p>
    </div>

    <div class="card">
        <h2>Circuit Board</h2>
        <p class="count">{{ data["circuit_board"] }}</p>
    </div>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(html, data=waste_data, time=current_time)

@app.route("/update/<label>")
def update(label):
    if label in waste_data:
        waste_data[label] += 1
    return "OK"

app.run(debug=True)
