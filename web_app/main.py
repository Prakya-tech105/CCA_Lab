from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html',titke="Home Page")

if __name__=='__main__':
    #Local Development server
    app.run(host='127.0.0.1',port=8080,debug=True)