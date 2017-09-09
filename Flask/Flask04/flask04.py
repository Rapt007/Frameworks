from flask import Flask,redirect,render_template,url_for,request

app=Flask(__name__)
username=''

@app.route('/',methods=['GET','POST'])
def show_index():
    global username
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=='POST':
        username= request.form.get('user',none)
        return redirect(url_for('aboutme'))

@app.route('/resume')
def aboutme():
    return render_template("resume.html",user=username)


if __name__=="__main__":
    app.run()