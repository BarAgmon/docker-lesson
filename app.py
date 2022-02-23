from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    try:
        return render_template("index.html")
    except:
        print("run `docker exec` and enter your continer. Then run `mv index.html templates/index.html` and try to refresh your browser.")
        return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')