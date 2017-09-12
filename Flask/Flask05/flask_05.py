from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/user')
def show_user():
    return render_template('user.html')

if __name__=="__main__":
    app.run()