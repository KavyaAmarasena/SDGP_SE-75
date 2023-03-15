from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/room.html')
def room():
    return render_template("room.html")

@app.route('/',methods =["GET", "POST"])
def lobby():
    if request.method == "POST":
       room_id = request.form('room')
       return redirect (url_for('room',room_id = room_id))
       # getting input with name = fname in HTML form
    #    first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
    #    last_name = request.form.get("lname")
    #    return "Your name is "+first_name + last_name
    else:
        return render_template("lobby.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)