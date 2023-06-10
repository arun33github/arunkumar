from flask import Flask,render_template,request,redirect
import json_utils
import registration
import update
import delete


app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def register():
    if request.method=="POST":
     registration.register_business(request.form["cname"],request.form["phoneno"],request.form["location"])
    data=json_utils.Business("data/business.json")
    return render_template("home.html",business=data["Business"])

@app.route("/update/<int:sno>",methods=["POST","GET"])
def update_2(sno):
    if request.method=="POST":
        update.update(request.form ["sno"],request.form["cname"],request.form["phoneno"],request.form["location"])
        return redirect("/")
    data=json_utils.Business("data/business.json")
    for company in data["Business"]:
        if sno==company["sno"]:
         temp=company  
    return render_template("update.html",company=temp)

@app.route("/delete/<int:sno>",methods=["POST","GET"])
def delete_2(sno):
    if request.method=="post":
        delete.delete(request.form["cname"],request.form["phoneno"],request.form["location"])


if __name__=="__main__":
    app.run(debug=True)

