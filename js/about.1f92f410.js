(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["about"],{"13cd":function(t,e,n){},1542:function(t,e,n){"use strict";var o=n("13cd"),i=n.n(o);i.a},"2b3c":function(t,e,n){},6123:function(t,e,n){},"759b":function(t,e,n){"use strict";n.r(e);var o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"new"},[n("el-menu",{staticClass:"el-menu-demo",attrs:{"default-active":t.activeIndex,mode:"horizontal"},on:{select:t.handleSelect}},[n("el-menu-item",{attrs:{index:"1"}},[t._v("Shopping")]),n("el-menu-item",{attrs:{index:"4"}},[t._v("Order")])],1),n("div",{attrs:{id:"items"}},t._l(t.items,function(t){return n(t.component,{tag:"div",attrs:{title:t.title,bgc:t.bgc}})}),1)],1)},i=[],c=(n("7f7f"),n("a481"),n("cadf"),n("551c"),n("097d"),function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"ordercp",style:t.bgc},[n("h6",[t._v(t._s(t.title)+"，"+t._s(t.id))])])}),r=[],a={name:"ordercp",props:{title:String,id:String,bgc:String},methods:{}},s=a,l=(n("1542"),n("2877")),u=Object(l["a"])(s,c,r,!1,null,null,null);u.options.__file="Ordercp.vue";var d=u.exports,p={name:"new",data:function(){return{userid:"",pw:"",h:"20%",activeIndex:"4",items:[{component:d,id:"1",title:"订单1",shopurl:"./img/1.jpg",bgc:"background-color:#909399"},{component:d,id:"2",title:"订单2",shopurl:"./img/2.img",bgc:"background-color:#E4E7ED"}]}},components:{ordercp:d},methods:{handleSelect:function(t,e){console.log(t,e),"1"==t&&this.$router.replace({name:"about"})}},mounted:function(){var t=this,e=n("bc3a");e.get("/orderpage/orderinfo",{params:{}}).then(function(e){if(-1==e);else for(var n=["#00ffff","#00ff00"],o=e["len"],i=0;i<o;i++){var c=e[String(i)];t.items.push({component:shopcomponent,id:c["orderid"],title:c["name"],bgc:n[i%2]})}}).catch(function(t){console.log(t)}).then(function(){})}},f=p,m=(n("a1cd"),Object(l["a"])(f,o,i,!1,null,null,null));m.options.__file="new.vue";e["default"]=m.exports},"7f7f":function(t,e,n){var o=n("86cc").f,i=Function.prototype,c=/^\s*function ([^ (]*)/,r="name";r in i||n("9e1e")&&o(i,r,{configurable:!0,get:function(){try{return(""+this).match(c)[1]}catch(t){return""}}})},a1cd:function(t,e,n){"use strict";var o=n("6123"),i=n.n(o);i.a},e76e:function(t,e,n){"use strict";var o=n("2b3c"),i=n.n(o);i.a},f820:function(t,e,n){"use strict";n.r(e);var o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"about",attrs:{id:"about"}},[n("el-menu",{staticClass:"el-menu-demo",attrs:{"default-active":t.activeIndex,mode:"horizontal"},on:{select:t.handleSelect}},[n("el-menu-item",{attrs:{index:"1"}},[t._v("Shopping")]),n("el-menu-item",{attrs:{index:"4"}},[t._v("Order")])],1),n("div",{attrs:{id:"shop"}},t._l(t.items,function(t){return n(t.component,{tag:"div",attrs:{title:t.title,id:t.id,shopurl:t.shopurl,bgc:t.bgc}})}),1)],1)},i=[],c=(n("7f7f"),n("a481"),n("cadf"),n("551c"),n("097d"),n("fdab")),r={name:"about",data:function(){return{userid:"",pw:"",h:"20%",activeIndex:"1",lists:[{id:"1",title:"商品1",shopurl:"./img/1.jpg"},{id:"2",title:"商品2",shopurl:"./img/2.img"}],items:[{component:c["a"],id:"1",title:"商品1",shopurl:"./img/1.jpg",bgc:"background-color:#909399"},{component:c["a"],id:"2",title:"商品2",shopurl:"./img/2.img",bgc:"background-color:#E4E7ED"}]}},components:{shopcomponent:c["a"]},methods:{handleSelect:function(t,e){console.log(t,e),"4"==t&&this.$router.replace({name:"new"})}},mounted:function(){var t=this,e=n("bc3a");e.get("/shoppingpage/getinfo",{params:{}}).then(function(e){response1=e.data;var n=["#00ffff","#00ff00"],o=response1["len"];console.log("response1",response1),console.log("length",o);for(var i=0;i<o;i++){var r=response1[String(i)];console.log(r),t.items.push({component:c["a"],id:r["id"],title:r["name"],shopurl:r["pictureurl"],bgc:n[i%2]}),console.log(t.items)}}).catch(function(t){console.log(t)}).then(function(){})}},a=r,s=(n("e76e"),n("2877")),l=Object(s["a"])(a,o,i,!1,null,null,null);l.options.__file="About.vue";e["default"]=l.exports}}]);
//# sourceMappingURL=about.1f92f410.js.map