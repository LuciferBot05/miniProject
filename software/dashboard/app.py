from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# Dummy data
waste_data = {
    "battery": 5,
    "cable": 3,
    "mobile": 2,
    "circuit_board": 4
}

html = """
<!DOCTYPE html>
<html>
<head>
    <title>E-Waste Dashboard</title>

    <!-- Auto refresh every 5 seconds -->
    <meta http-equiv="refresh" content="5">

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
            margin-top: 20px;
        }

        .card {
            display: inline-block;
            background: #1e293b;
            padding: 20px;
            margin: 15px;
            border-radius: 10px;
            width: 200px;
            transition: 0.3s;
        }

        .card:hover {
            transform: scale(1.05);
            background: #334155;
        }

        .count {
            font-size: 30px;
            color: #38bdf8;
        }

        .total {
            margin-top: 20px;
            font-size: 24px;
            color: #facc15;
        }
    </style>
</head>
<body>

    <h1>♻ Smart E-Waste Monitoring Dashboard</h1>
    <p>{{ time }}</p>

    <div class="container">

        <div class="card">
            <h2>🔋 Battery</h2>
            <p class="count">{{ data["battery"] }}</p>
        </div>

        <div class="card">
            <h2>🔌 Cable</h2>
            <p class="count">{{ data["cable"] }}</p>
        </div>

        <div class="card">
            <h2>📱 Mobile</h2>
            <p class="count">{{ data["mobile"] }}</p>
        </div>

        <div class="card">
            <h2>💻 Circuit Board</h2>
            <p class="count">{{ data["circuit_board"] }}</p>
        </div>

    </div>

    <div class="total">
        Total Waste Items: {{ total }}
    </div>

</body>
</html>
"""

@app.route("/")
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_items = sum(waste_data.values())
    return render_template_string(html, data=waste_data, time=current_time, total=total_items)

if __name__ == "__main__":
    app.run(debug=True)
