from flask import Flask
from flask import request,make_response,render_template

app = Flask(__name__,static_folder='', static_url_path='',template_folder='')

"""
@app.route('/firstpage')
def firstpage():
    resp = make_response()
    resp.response = render_template("index.html")

    return resp
"""
@app.route('/firstpage/registry')
def registry():
    customerid = request.args.get("customerid")
    password = request.args.get("password")
    #注册函数
    resp = make_response()
    #resp.set_cookie('customerid', customerid)
    #resp.set_cookie('password', password)
    resp.response = render_template("index.html")

    return resp



if __name__ == '__main__':
    app.run()
