from flask import *
# create/ initialize flask app
app=Flask(__name__)

# define route/endpoints
@app.route("/api/home")
def home():
    return jsonify({"message": "welcome to HOME API"})

@app.route("/api/products")
def products():
    return jsonify({"message": "Welcome to products API"})

@app.route("/api/about")
def about():
    return jsonify({"message": "Welcome to about API"})

@app.route("/api/calc",methods=["POST"])
def calc():
    number1=request.form["number1"]
    number2=request.form["number2"]
    # print(type(number1))
    sum=int(number1)+int(number2)
    return jsonify({"Answer": sum})


if __name__ == '__main__':
    app.run(debug=True)

