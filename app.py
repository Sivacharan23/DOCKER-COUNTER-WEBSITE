from pathlib import Path
from flask import Flask

app = Flask(__name__)

DATA_DIR = Path("/app/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
COUNTER_FILE = DATA_DIR / "counter.txt"


@app.route("/")
def home():
    count = 0

    if COUNTER_FILE.exists():
        count = int(COUNTER_FILE.read_text())

    count += 1
    COUNTER_FILE.write_text(str(count))

    return f"""
    <h1>Docker Counter App</h1>
    <p>This page has been visited {count} times.</p>
    <p>Refresh the page to increase the counter.</p>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)