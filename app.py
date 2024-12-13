from flask import Flask, request, make_response
from pydantic import ValidationError

from models import RecipesRequest
from nlp import recipes_recommendation

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/recipes", methods=["POST"])
def recipe():
    try:
        req = RecipesRequest(**request.json)
        main_ingred = req.main_ingredient
        ingred = req.ingredients

        data = recipes_recommendation(main_ingred, ingred)

        res = {
            "status": "success",
            "data": data
        }
        response = make_response(res)
        response.headers["Content-Type"] = "application/json"
        response.status_code = 200

        return response

    except ValidationError as e:
        errors = {}
        for error in e.errors():
            field = error["loc"][0]
            message = error["msg"]
            errors[field] = message

        res = {
            "status": "failed",
            "data": errors
        }
        response = make_response(res)
        response.headers["Content-Type"] = "application/json"
        response.status_code = 400

        return response
    
    except:
        res = {
            "status": "failed",
            "data": {
                "error": "Invalid JSON format"
            }
        }
        response = make_response(res)
        response.headers["Content-Type"] = "application/json"
        response.status_code = 400

        return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
