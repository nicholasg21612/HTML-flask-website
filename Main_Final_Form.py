from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '''
    <h1 style="font-size:20px"><a href="http://127.0.0.1:5000/">Home</a></h1>
    <h1 style="font-size:35px"><center>Welcome to the main page!</center><h1>
    <center>
    <img src= https://fyi.extension.wisc.edu/safefood/files/2020/03/sars-cov-19.jpg>
    </center>

    <h1 style="color:green"><a href="http://127.0.0.1:5000/1"><center>Take Test Here!</center></a></h1>

    '''


@app.route("/1")
def one():
    return '''
        home2.html
        '''


if __name__ == "__Main_Final_Form__":
    app.run(use_reloader=True)
