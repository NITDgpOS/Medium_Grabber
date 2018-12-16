import cred
from Grab_that_article_on_Medium import grab
from flask import Flask, render_template, request
app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'GET':
        return "Please submit the forms instead."
    else:
        txt_pdf = grab()
    if txt_pdf == "PDF":
        response = render_template("pdf.html")
    else:
        response = render_template("txt.html")
    return response

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

if __name__=='__main__':
    app.run(port=1234)