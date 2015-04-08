from flask import Flask,jsonify,abort,request,make_response
from flask.ext.httpauth import HTTPBasicAuth



auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'john':
        return 'mary'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error':'Unauthorized Access'}),403)

app = Flask(__name__)


tasks = [
    {
        'id':1,
        'title':u'Cleaning',
        'desc':u'Clean the house',
        'done':True
    },
    {
        'id':2,
        'title':u'Cooking',
        'desc':u'Prepare dinner',
        'done':False
    }
]

@app.route('/todo/api/v1.0/tasks',methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks':tasks})



@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

@app.route('/todo/api/v1.0/tasks',methods=['POST'])
def create_task():

    if not request.json or not 'title' in request.json:
        abort(400)

    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'desc':request.json.get('desc',""),
        'done':False
        }
    tasks.append(task)
    return jsonify({'task':task}),201 ## 201 is the status code for created

@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(400)
    if not request.json:
        abort(400)
    if type(request.json['title']) != unicode:
        abort(400)
    if type(request.json['description']) != unicode:
        abort(400)
    if type(request.json['done']) is not bool:
        abort(400)

    task[0]['title'] = request.json.get('title',task[0]['title'])
    task[0]['description'] = request.json.get('desc',task[0]['description'])
    task[0]['done'] = request.json.get('done',task[0]['done'])

    return jsonify({'task':task})

@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])

    return jsonify({'result':True})
    


  
        

if __name__=="__main__":
    app.run(debug=True)
    
