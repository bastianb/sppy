from flask import json, abort, request, render_template
from sppy.app import app

"""
request.args   : GET If you want the parameters in the URL
request.form   : POST If you want the info in the body (as send by a html POST form)
request.values : If you want both
"""


@app.route('/ping/')
def ping():
    return json.dumps('pong')


@app.route('/send/')
def send():
    return render_template('send.html')


@app.route('/vads-payment')
def no_redirect():
    raise abort(404)


@app.route('/vads-payment/', methods=['POST'])
def vads_payment():
    vads = {}
    for key, val in request.form.iteritems():
        if key.startswith('vads_'):
            vads[key] = val
    return json.dumps(vads)
