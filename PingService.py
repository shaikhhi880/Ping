from flask import Flask, jsonify,url_for
from flask_httpauth import HTTPDigestAuth
from requests.auth import HTTPDigestAuth as Dauth
import requests
import json
import time 

app = Flask(__name__)
auth = HTTPDigestAuth()
app.config['SECRET_KEY'] = 'secret key here'

credentials = {
    'vcu': 'rams'
}

url = 'http://127.0.0.1:7000/'

@auth.get_password
def get_pw(username):
    if(username in credentials):
        return credentials.get(username)
    return None

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'page not here from ping'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Something is Broken from ping'}), 500

@app.route('/ping', methods=['GET'])
@auth.login_required
def index():
    r = requests.get(url+"pong",auth = Dauth("vcu","rams"))
    s = time.perf_counter()
    pingpong_t = (time.perf_counter()-start) * 1000
    return jsonify({"time": pingpong_t})
   
    

if __name__ == '__main__':
    app.run()