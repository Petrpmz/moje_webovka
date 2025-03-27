import os
import importlib.util
from flask import Flask, render_template

app = Flask(__name__)

SCRIPTS_DIR = "scripts"

def load_and_run_scripts():
    results = []
    for filename in os.listdir(SCRIPTS_DIR):
        if filename.endswith(".py"):
            filepath = os.path.join(SCRIPTS_DIR, filename)
            spec = importlib.util.spec_from_file_location("module.name", filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            results.append(f"Spuštěn: {filename}")
    return results

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run-scripts")
def run_scripts():
    result = load_and_run_scripts()
    return "<br>".join(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Port 10000 pro Render
