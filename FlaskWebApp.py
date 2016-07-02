from flask import Flask, redirect
from flask.helpers import url_for

webapp = Flask(__name__)

@webapp.route("/static", methods=['GET'])
def showStaticFiles():
	return redirect(url_for('static',filename='staticHTMLFile.html'))

if __name__ == '__main__':
	webapp.run(host='0.0.0.0', port=8999,debug=True)
