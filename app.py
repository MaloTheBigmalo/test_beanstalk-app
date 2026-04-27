from flask import Flask 
app = Flask('__name__')

@app.route('/')
def hello_world():
    msg = 'Hello, headinthe clouds -this is our demo on Elastic Beanstaklk!'
    return msg

if __name__ == '__name__':
    app.run(host='0.0.0.0', port=3000)

