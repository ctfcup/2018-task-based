from flask import Flask, request, render_template_string
import urllib

application = Flask(__name__)

@application.errorhandler(404)
def error(e):
    template = '''
    <div class="center-content error">
        <h1> Page not found :( </h1>
    </div>
'''
    return render_template_string(template), 404

@application.route('/', methods=["POST", "GET"])
def index():
    template = '''<html>
          <head>
            <title>Try to hack v.1</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" media="screen">
          </head>
          <body>
            <div class="container">
                <h1> Hi, %s! </h1>
                <form action="" method="post">
                  <h3> Enter you name! </h3>
                  <input type="text" placeholder="Name" name="EnterYouName" value="{{request.form.EnterYouName}}">
                  <input class="btn btn-default" type="submit" value="View">
                </form>
            </div>
          </body>
        </html>
        ''' % "quest"
    if request.method == "POST":
        name = request.form['EnterYouName']
        blacklist = ["__class__", "__subclasses__", "__mro__", 'flag']
        for bad in blacklist:
            if bad in name:
                return (render_template_string("ARE YOU HACKER?!!"))
        template = '''<html>
                  <head>
                    <title>Try to hack v.1</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" media="screen">
                  </head>
                  <body>
                    <div class="container">
                        <h1> Hi, %s! </h1>
                        <form action="" method="post">
                          <h3> Enter you name! </h3>
                          <input type="text" placeholder="Name" name="EnterYouName" value="{{request.form.EnterYouName}}">
                          <input class="btn btn-default" type="submit" value="View">
                        </form>
                    </div>
                  </body>
                </html>
                ''' % name
        return render_template_string(template)
    return render_template_string(template)

if __name__== '__main__':
    application.run(port=8080, host='0.0.0.0', debug=False)
