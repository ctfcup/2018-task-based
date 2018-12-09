from flask import Flask, render_template, request, Session, render_template_string

application = Flask(__name__)

@application.errorhandler(404)
def error(e):
    template = '''{%% extends "index.html" %%}
{%% block content %%}
    <div class="center-content error">
        <h1> Hmm! Looks like this page doesn't exist.</h1>
        <h3>%s</h3>
    </div>
{%% endblock %%}
''' % (request.url)
    return render_template_string(template), 404

@application.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        s = request.form['FileName']
        try:
            tmp = open('/app/Anecdotes/{}'.format(s)).read()
            print(tmp)
            if tmp is not None:
                if s.find('flag') >= 0:
                    template = """Nononono >:("""
                else:
                    template = """You file: %s""" % tmp
                    print(template)
        except:
            template = """Hmmm! Looks like file %s doesn't exist.""" % s
        return render_template("index.html", template=template)
    return render_template("index.html", template=None)

#it's very secure, to be store something
def read():
	with open("flag.py") as f:
		return f.readlines()

application.jinja_env.globals['read'] = read

if __name__== '__main__':
    application.run(port=8080, host='0.0.0.0', debug=False)
