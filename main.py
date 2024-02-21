from flask import Flask
import random
app = Flask('__main__')


@app.route('/')
def index():
    r = random.randint(1,1000)
    output = f"{r}"
    return output


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")