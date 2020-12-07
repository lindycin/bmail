from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') #how to write the path..??
def password():
	return render_template('pw.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3000, threaded = True, debug = True)
