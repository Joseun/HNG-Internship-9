from flask import Flask, jsonify, make_response, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"slackUsername": "Joseun",
                    "backend": True,
                    "age": 27,
                    "bio": "Hi, Joseph Ologunja here, I am a Full Stack developer, proficient in Python"
                   })

@app.route('/', methods=['POST'])
def post_world():
#     if not request.get_json():
#         abort(400, description="Not a JSON")

#     if 'operation_type' not in request.get_json():
#         abort(400, description="Missing operation_type")
#     if 'x' not in request.get_json():
#         abort(400, description="Missing value")
#     if 'y' not in request.get_json():
#         abort(400, description="Missing value")
#     if not type(request.get_json()['x']) is int:
#         abort(400, description="Value not an integer")
#     if not type(request.get_json()['y']) is int:
#         abort(400, description="Value not an integer")
#     ops = {'addition': x + y, 
#            'substraction': x - y,
#            'multiplication': x * y}
    data = request.get_json()
#     x = data['x']
#     y = data['y']
#     for k, v in ops.items():
#         if k == data['operation_type']:
#             result = v
   
    r = {"slackUsername": "Joseun",
                     "operation_type": data['operation_type'],
                     "result": result
         "data": data
                    }
    headers={'mimetype':'application/json'}

    response = make_response(jsonify(r), 200)

    response.headers = headers

    return response
