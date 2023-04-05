from flask import Blueprint,jsonify,request
from happytransformer import HappyTextToText,TTSettings

api = Blueprint('api',__name__)

# def validate_token_middleware(func):
#     def wrapper(*args, **kwargs):
#         token = request.headers.get('Authorization')

#         # Perform token validation here
#         if not token:
#             return jsonify({'error': 'Missing authorization token'}), 401

#         # If token is valid, call the view function
#         return func(*args, **kwargs)
#     return wrapper

# @api.before_request
# @validate_token_middleware
# @api.route("/update-marks",methods=['GET'])
# def update_marks():
#     return 'add marks'

@api.route('/verify-message',methods = ['GET','POST'])
def verify_message():
    happy_tt = HappyTextToText("T5","vennify/t5-base-grammar-correction")
    data = request.json
    message = str(data['message'])

    beam_settings =  TTSettings(num_beams=5, min_length=1, max_length=20)
    prefix = "grammar: "
    input = prefix+message

    result = happy_tt.generate_text(input, args=beam_settings)

    response = 'response'

    if(message == result.text):
        print(message)
        response = jsonify({
            'msg' : "correct"
        })
    else:
        response =  jsonify({
            'msg': "incorrect"
        })
    return response