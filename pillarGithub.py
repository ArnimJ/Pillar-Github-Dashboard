from flask import Flask
import handler
from flask import render_template


app = Flask(__name__)


@app.route('/organizations/<section>')
def organizations(section):
    res = handler.handle(section)
    return render_template("index.html", org = section, result = res[0], result2 = res[1])


if __name__ == '__main__':
    app.run()
