from flask import Flask
import DB as db
import json
app = Flask(__name__)

@app.route('/HelloWorld')
def hello_world():
    strategyInstanceList = db.getStrategyInstanceList()
    htmlStr = "<button>Save</button>"
    result = {"list":strategyInstanceList}
    htmlStr = json.dumps(result)
    print("test")
    print("test")
    return htmlStr

@app.route('/')
def startStrategy():
    strategyInstanceList = db.getStrategyInstanceList()
    htmlStr = "<button>Save</button>"
    result = {"list":strategyInstanceList}
    htmlStr = json.dumps(result)
    return htmlStr
if __name__ == "__main__":
    app.run(debug=True)
