from flask import Flask,render_template,request, url_for,redirect

app=Flask(__name__)
@app.route('/')
def show_index():
    return render_template('index.html')


@app.route('/myresume')
def resume():
    return render_template('resume.html')

if __name__=="__main__":
    app.run()
