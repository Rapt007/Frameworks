from flask import Flask, render_template,url_for,request,redirect

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def show_index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        return redirect('homepage')

@app.route('/homepage')
def homepage_user():
    return render_template('userhomepage.html')
if __name__=="__main__":
    app.run()