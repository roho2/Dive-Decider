from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Dive Decider is running ✅"

if __name__ == "__main__":
    app.run(debug=True)