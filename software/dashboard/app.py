from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# Dummy data (you can later connect real data)
waste_data = {
    "battery": 5,
    "cable": 3,
    "mobile": 2,
    "circuit_board": 4
}

# HTML Template (no need separate file)
html = """
<!DOCTYPE html>
<html>
<head>
    <title>E-Waste Dashboard</title>
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
        .card {
            display: inline-block;
            background: #1e293b;
            padding: 20px;
            margin: 15px;
            border-radius: 10px;
            width: 200px;
        }
        .count {
            font-size: 30px;
            color: #38bdf8;
        }
    </style>
</head>
<body>

    <h1>♻ Smart E-Waste Monitoring Dashboard</h1>
    <p>{{ time }}</p>

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

</body>
</html>
"""

@app.route("/")
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(html, data=waste_data, time=current_time)

if __name__ == "__main__":
    app.run(debug=True)
