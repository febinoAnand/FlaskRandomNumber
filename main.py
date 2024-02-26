from flask import Flask,request
import random
app = Flask('__main__')

@app.route('/')
def index():
    r = random.randint(1,1000)
    output = f"{r}"
    return output

@app.route('/iopin',methods=["POST","GET"])
def ioPin():
    if request.method == "POST":
        r = request.form["inputs"]
        output = int(r)
        if output < 0 or output > 255:
            r = "input data error"
        else:
            print (r)
            randomNo = random.randint(0,255)
            r = f"{randomNo}"
    else:
        r = "GET error"
    return r

@app.route('/output')
def output():
    r = random.randint(0,255)
    output = f"{r}"
    return output

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")