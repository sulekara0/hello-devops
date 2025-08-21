from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok", service="hello-devops"), 200

@app.get("/")
def root():
    return "Hello DevOps ", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
