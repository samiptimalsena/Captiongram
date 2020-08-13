from flask import Flask
from model import evaluate

app=Flask(__name__)

@app.route("/")
def home():
    result=evaluate("./1.jpg")
    sentence=" ".join(result)
    return(f"<h1>The picture shows: {sentence}</h1>")

if __name__ == "__main__":
    app.run(debug=True)