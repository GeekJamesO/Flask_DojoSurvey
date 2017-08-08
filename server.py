from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    return render_template("DojoSurvey.html")

@app.route("/result", methods=['POST'])
def result():
    print 'before Params'
    resultName = request.form['Name']
    print "name = ", resultName
    resultLocation = request.form['Dojos']
    print "location = ", resultLocation
    resultLanguage = request.form['Language']
    print "language = ", resultLanguage
    resultComment = request.form['Comment']
    print "comment = ", resultComment
    return render_template("result.html",
                           Name=resultName,
                           Location=resultLocation,
                           Language=resultLanguage,
                           Comment=resultComment)
app.run(debug=True)
