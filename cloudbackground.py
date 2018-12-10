from flask import Flask
from flask import request,make_response,render_template
import json
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
    #resp.response = render_template("shoppingpage.html")

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
        #resp.response = render_template("shoppingpage.html")

        return resp
    else:
        return -1

@app.route('/shoppingpage/getinfo')
def shop():
    customerid = request.cookies.get('customerid')
    finallist = []
    finaldic = {}
    # getinfo function
    #返回一个list，有很多子list组成，每个子list代表一个商品，包括一个商品id，一个商品图片url，一个商品数量
    #list = function()
    #for sublist in list:
    #   id = sublist[0]
    #   num = sublist[2]
    #   pictureurl = sublist[1]
    #   name = sublist[3]
    #   finallist.append(json.dump({"id":id,"num":num,"pictureurl":pictureurl,"name":name}))
    for i in range(len(finallist)):
        finaldic["i"] = finallist[i]
    return json.dump(finaldic)

@app.route('/shoppingpage/purchase')
def purchase():
    customerid = request.cookies.get('customerid')
    num = request.cookies.get('num')
    id = request.cookies.get('id')#商品id
    #purchase function
    if(True):
        resp = make_response()
        #resp.response = render_template("orderpage.html")
        return resp
    else:
        return -1

@app.route('/orderpage/orderinfo')
def orderinfo():
    customerid = request.cookies.get('customerid')
    finallist = []
    finaldic = {}
    #order
    # list = function()
    # for sublist in list:
    #   orderid = sublist[0]
    #   num = sublist[2]
    #   name = sublist[1]
    #   finallist.append(json.dump({"orderid":orderid,"num":num,,"name":name}))
    for i in range(len(finallist)):
        finaldic["i"] = finallist[i]
    return json.dump(finaldic)


if __name__ == '__main__':
    app.run()
