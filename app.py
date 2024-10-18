from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *
import pdb

app =Flask("__survey__")
app.debug=True
app.config['SECRET_KEY'] = 'my_key'
toolbar = DebugToolbarExtension(app)



@app.route('/')
def main_page():
    
    return render_template("main.html", instructions = satisfaction_survey.instructions,questions= satisfaction_survey.questions,title= satisfaction_survey.title)

@app.route('/questions/<id>')
def questions_page(id):

    if int(id)< len(satisfaction_survey.questions):
        question = satisfaction_survey.questions[int(id)].question
        choices = satisfaction_survey.questions[int(id)].choices


    if(int(id) == len(session['responses'])):
        
        return render_template("questions.html", question = question, choices = choices, id = id)
    
    elif (len(satisfaction_survey.questions) == len(session['responses'])):
        return render_template("thanks.html")
    else:
        flash("You are trying to access a question out of order!!!")
        return render_template("OOO.html")


@app.route('/answer', methods =['POST'])
def answer_page():
    responses = session['responses']
    responses.append(request.form)
    session['responses'] = responses
    #ask about this
   
    current_id = len(responses)

    if len(satisfaction_survey.questions) > len(responses):
        return redirect(f"/questions/{current_id}")
    else: 
        return render_template("thanks.html")
    
@app.route('/newroute', methods = ['POST'])
def new_route():
     session["responses"] = []
     return redirect ('/questions/0')