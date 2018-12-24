from flask import Flask
from flask import request,make_response,render_template
import json
import Connection as con
app = Flask(__name__,static_folder='', static_url_path='',template_folder='')

"""
@app.route('/firstpage')
def firstpage():
    resp = make_response()
    resp.response = render_template("index.html")

    return resp
"""


@app.route('/firstpage/registry')
def cregistry():
    print("res")
    customerid = request.args.get("customerid")
    password = request.args.get("password")
    #注册函数
    t = con.registry(customerid,password)
    print(t)
    resp = make_response()
    if(t == True):
        print(t)
        resp = make_response()
        resp.set_cookie('customerid', customerid)
        resp.set_cookie('password', password)
        return resp
    else:
        return "F"
    #resp.response = render_template("shoppingpage.html")


@app.route('/firstpage/login')
def clogin():
    customerid = request.args.get("customerid")
    password = request.args.get("password")
    t = con.login(customerid,password)
    if(t == True):
        resp = make_response()
        resp.set_cookie('customerid', customerid)
        resp.set_cookie('password', password)
        #resp.response = render_template("shoppingpage.html")

        return resp
    else:
        return "F"


@app.route('/shoppingpage/getinfo')
def shop():
    customerid = request.cookies.get('customerid')
    finallist = []
    finaldic = {}
    # getinfo function
    #返回一个list，有很多子list组成，每个子list代表一个商品，包括一个商品id，一个商品图片url，一个商品数量
    list = con.getinfo()
    for sublist in list:
       id = sublist[0]
       num = sublist[3]
       pictureurl = sublist[4]
       name = sublist[2]
       price = sublist[1]
       finallist.append(json.dumps({"id":id,"num":num,"pictureurl":pictureurl,"name":name,"price":price}))
    #finallist.append(json.dumps({"id":"123","num":12,"pictureurl":"./img/3.jpg","name":"tname"}))
    finaldic["len"]=len(finallist)
    for i in range(len(finallist)):
        finaldic[str(i)] = finallist[i]
    return json.dumps(finaldic)

@app.route('/shoppingpage/search')
def search():
    minprice = request.args.get("minprice")
    maxprice = request.args.get("maxprice")
    keyword = request.args.get("keyword")
    finallist = []
    finaldic = {}

    list = con.search(minprice,maxprice,keyword)
    #list =  refreshfunction
    for sublist in list:
       id = sublist[0]
       num = sublist[3]
       pictureurl = sublist[4]
       name = sublist[2]
       price = sublist[1]
       finallist.append(json.dumps({"id":id,"num":num,"pictureurl":pictureurl,"name":name,"price":price}))
    #finallist.append(json.dumps({"id":"123","num":12,"pictureurl":"./img/3.jpg","name":"tname"}))
    finaldic["len"]=len(finallist)
    for i in range(len(finallist)):
        finaldic[str(i)] = finallist[i]
    return json.dumps(finaldic)


@app.route('/shoppingpage/purchase')
def purchase():
    customerid = request.cookies.get('customerid')
    num = request.args.get('num')
    id = request.args.get('id')#商品id
    #purchase function
    s = con.buy(customerid,id,1)
    if(s == True):
        resp = make_response()
        #resp.response = render_template("orderpage.html")
        return resp
    else:
        return "F"



@app.route('/orderpage/orderinfo')
def orderinfo():
    customerid = request.cookies.get('customerid')
    finallist = []
    finaldic = {}
    #order
    list = con.orderinfo(customerid)
    for sublist in list:
       orderid = sublist[0]
       num = sublist[3]
       name = sublist[2]
       cus = sublist[1]

       finallist.append(json.dumps({"orderid":orderid,"num":num,"name":name}))

    finaldic["len"]=len(finallist)
    for i in range(len(finallist)):
        finaldic[str(i)] = finallist[i]
    print(finaldic)
    return json.dumps(finaldic)




if __name__ == '__main__':
    app.run()
