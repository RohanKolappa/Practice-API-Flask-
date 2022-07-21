import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Practice Flask Application That Will Be Used As A Prototype</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run()

#to run this code in terminal, create a file with the code above followed by "python [filename]"
#Then, copy the http link presented in the terminal into a web browser to see the output
