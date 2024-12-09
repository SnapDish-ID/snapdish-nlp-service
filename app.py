from flask import Flask, request, make_response

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/", methods=["GET"])
def home():
    res = {
        "status": "success",
        "message": "this is homepage"
    }
    response = make_response(res)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route("/recipes", methods=["POST"])
def recipe():
    req = request.json

    # TODO: handle request validation here
    # ...

    # TODO: get ingredients from request body here
    num = req.get("num")

    # TODO: retrieve recipe recommendation here
    data = [
        {
            "title": "TITLE_1",
            "ingredients": "INGRED_1",
            "steps": "STEPS_1" 
        },
        {
            "title": "TITLE_2",
            "ingredients": "INGRED_2",
            "steps": "STEPS_2" 
        }
    ]

    res = {
        "status": "success",
        "data": data[0:num] # dummy
    }
    response = make_response(res)
    response.headers["Content-Type"] = "application/json"

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
