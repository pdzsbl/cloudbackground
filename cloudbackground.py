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

@app.route('/firstpage/login')
def login():
    customerid = request.args.get("customerid")
    password = request.args.get("password")
    # login函数
    if(True):
        resp = make_response()
        # resp.set_cookie('customerid', customerid)
        # resp.set_cookie('password', password)
        resp.response = render_template("index.html")

        return resp
    else:
        return -1

@app.route('/shoppingpage/getinfo')
def shop():
    customerid = request.cookies.get('customerid')
    # getinfo function
    


if __name__ == '__main__':
    app.run()
