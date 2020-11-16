from flask import Flask, send_from_directory

app = Flask(__name__)

DOWNLOAD_DIRECTORY = "./"

@app.route('/get-files/bmail:pw.html',methods = ['GET','POST']) #how to write the path..??
def get_files(path):

    """Download a file."""
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3000, threaded = True, debug = True)
