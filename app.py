from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world from CI/CD from jenkins webhook'

@app.route('/health')
def hello_world():
    return 'Status: Healthy :-D'
    
@app.route('/route-sync')
def hello_world():
    return 'Status: Healthy route sync done :-D'

@app.route('/route-sync-two')
def hello_world():
    return 'Status: Healthy route sync done two :-D'

@app.route('/reverser',methods = ['POST'])
def reverser():
    num = request.get_json().get("num")
    num = int(num[len(num)::-1])
    return jsonify({"num":num})


@app.route('/summation',methods = ['POST'])
def summation():
    num = request.get_json().get("num")
    sum = 0
    for i in num:
        sum += int(i)

    return jsonify({"sum":sum})

if __name__ == "__main__":
     app.run()
