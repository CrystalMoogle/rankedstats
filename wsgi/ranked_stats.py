#!/usr/bin/python
from __future__ import division
import os
import traceback
import usage_stats
import urllib

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import jsonify
from collections import OrderedDict
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))


@app.route('/')
def index(url1=None, url2=None, weighting=None):
    try:
        url1 = url1 or request.args.get('url1')
        url2 = url2 or request.args.get('url2')
        weighting = weighting or request.args.get("weighting")
        if not weighting or not url1 or not url2:
            return render_template("index.html")
        processed_text = usage_stats.usage_stats(url2, url1, weighting)
        if isinstance(processed_text, list) and processed_text[0] == "Invalid Request":
            return render_template("index.html", errors=processed_text[1])
        return processed_text
    except:
        return render_template("error.html", traceback=traceback.format_exc())


@app.route('/', methods=['POST'])
def index_post():
    try:
        url1 = request.form.get('url1')
        url2 = request.form.get('url2')
        weighting = request.form.get('weighting')
        if not weighting or not url1 or not url2:
            return render_template("index.html", errors="Please enter text")
        return redirect(request.base_url + "?" + urllib.urlencode(OrderedDict(url1=url1, url2=url2, weighting=weighting)))
    except:
        return render_template("error.html", traceback=traceback.format_exc())


@app.route('/api/v1.0/', methods=['POST', 'GET'])
@app.route('/api/v1.0', methods=['POST', 'GET'])
def app_route():
    try:   
        if request.method == 'GET':
            return index() 
        if request.form.get('response'):
            return usage_stats.usage_stats(request.form.get('url1'), request.form.get('url2'), request.form.get('weighting'), request.form.get('response').lower())
            
        return index(url1=request.form.get('url1'), url2=request.form.get('url2'), weighting=request.form.get('weighting'))
    except:
        print traceback.format_exc()


@app.errorhandler(404)
def page_not_found(e):
    return index(), 404

if __name__ == '__main__':
    app.run()
