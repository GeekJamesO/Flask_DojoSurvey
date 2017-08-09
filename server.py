from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="SmokeandFire"

@app.route('/', methods=['GET'])
def root():
    return render_template("DojoSurvey.html")

@app.route("/result", methods=['POST'])
def result():
    resultName = request.form['Name']
    resultLocation = request.form['Dojos']
    resultLanguage = request.form['Language']
    resultComment = request.form['Comment']

    # validate
    validInput = True
    if (len(resultName) < 1):
        validInput = False;
        flash("Name field cannot be blank.")



    if (len(resultComment) < 1):
        validInput = False;
        flash("Comment field cannot be blank.")
    if (len(resultComment) > 120):
        validInput = False;
        flash("Comment field cannot be larger than 120 characters.")


    if (validInput):
        return render_template('result.html',
                               Name=resultName,
                               Location=resultLocation,
                               Language=resultLanguage,
                               Comment=resultComment)
    else:
        return redirect('/')
app.run(debug=True)
