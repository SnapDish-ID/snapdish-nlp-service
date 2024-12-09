from flask import Flask, request, make_response
import nlp

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

    main_ingred = req.get("main_ingredient")
    ingred = req.get("ingredients")

    data = nlp.recipes_recommendation(main_ingred, ingred)

    res = {
        "status": "success",
        "data": data
    }
    response = make_response(res)
    response.headers["Content-Type"] = "application/json"

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
