from flask import Blueprint,jsonify,request,session
from happytransformer import HappyTextToText,TTSettings
import sqlite3
from sqlite3 import Error
from datetime import datetime


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

@api.route('/update-score',methods=['POST','GET'])
def update_score():
    
    data = request.json
    marks = int(data['marks'])
    std_id = session.get("std_id")
    meeting_id = "M001"

    message = 'message'

    if(request.method == 'POST'):
        with sqlite3.connect("./instance/learnly.db") as con:

            cursor = con.cursor()

            try:
                cursor.execute("INSERT INTO Marks (std_id,meeting_id,date,time,marks) VALUES (?,?,CURRENT_DATE,CURRENT_TIME,?)",(std_id,meeting_id,marks))
                con.commit()

                message = 'score has been added'
                    
            except Error as e:
                print(e)
    
    return message

@api.route("/get-scores",methods=['GET'])
def get_scores():
    if(request.method == "GET"):
        with sqlite3.connect("./instance/learnly.db") as con:

            cursor = con.cursor()

            try:
                cursor.execute("SELECT marks.std_id,student.std_fname,student.std_lname,SUM(marks) as total_marks FROM Marks marks JOIN Student student ON marks.std_id = student.std_id WHERE date = CURRENT_DATE GROUP BY marks.std_id;")
                rows = cursor.fetchall();

                result = []

                for row in rows:
                    result.append({
                        'std_id': row[0],
                        'std_fname': row[1],
                        'std_lname': row[2],
                        'total_marks': row[3]
                    })
                    
            except Error as e:
                print(e)

        cursor.close()
        con.close()
    
    return jsonify(result)