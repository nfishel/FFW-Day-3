from flask import Flask, render_template, request, session, redirect
from flask_session import Session

app = Flask(__name__)

#Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)

WORKOUTS = []
EXERCISES = [
  'Lunges', 'Pushups','Burpees', 'Crunches', 'Side Planks', 'Squats', 'Planks', 'Mountain Climbers','Reverse Crunches','Knee to Elbow Crunches'
]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/exercise", methods=["GET","POST"])
def exercise():
  if request.method == "POST":
    f_name = request.form.get('first')
    session["name"] = f_name
    
  if not session.get("name"):
    return render_template("error.html", message="You must register before you can log a workout!")
  
  return render_template("exercise.html", exercise_list=EXERCISES)

@app.route("/add", methods=["GET","POST"])
def add():
  if request.method == "POST":
    # get the data from the form.
    exercise_date = request.form.get('date')
    exercise = request.form.get('exercise')
    f_name = request.form.get('f_name')
    if exercise not in EXERCISES:
      return render_template("error.html", message="Please select a valid exercise from the list!")
    reps = request.form.get("reps")
    WORKOUTS.append({'e_date':exercise_date, 'exercise':exercise, 'reps':reps})
    # create a add page that will show each dictionary
  else:
    f_name = 'get it from a sesson later'
  return render_template("add.html", workout_list=WORKOUTS, f_name=f_name)


@app.route("/logout")
def logout():
  #empt the session name variable
  session["name"] = None
  return redirect("/")
  
##################################
if __name__ == "__main__":
  app.run("0.0.0.0")