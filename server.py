from flask import Flask, render_template
app = Flask(__name__)
@app.route('/playground/')
def boxes():
        return render_template('index.html', x = 3, boxColor='blue')
@app.route('/playground/<int:number>/')
def boxes1(number):
    return render_template('index.html', x = number, boxColor='blue')
@app.route('/playground/<int:number>/<string:color>')
def boxes2(number, color):
    return render_template('index.html', x = number, boxColor=color)
if __name__=="__main__":
    app.run(debug=True)