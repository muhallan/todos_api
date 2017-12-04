from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort, make_response
from flask_cors import CORS

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from app.models import Todo

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # add support for CORS for all end points
    CORS(app, resources={r"/*": {"origins": "*"}})

    # for removing trailing slashes enforcement
    app.url_map.strict_slashes = False

    db.init_app(app)

    @app.route('/todos/', methods=['POST', 'GET'])
    def todos():
        if request.method == "POST":
            title = str(request.data.get('title', ''))
            description = str(request.data.get('description', ''))
            if title and description:
                todo = Todo(title=title, description=description)
                todo.save()
                response = jsonify({
                    'id': todo.id,
                    'title': todo.title,
                    'description': todo.description,
                    'date_created': todo.date_created,
                    'date_updated': todo.date_updated,
                    'done_status': todo.done_status
                })
                response.status_code = 201
                return response
        else:
            # GET
            todos = Todo.get_all()
            results = []

            for todo in todos:
                obj = {
                    'id': todo.id,
                    'title': todo.title,
                    'description': todo.description,
                    'done_status': todo.done_status,
                    'date_created': todo.date_created,
                    'date_updated': todo.date_updated
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def todo_manipulation(id, **kwargs):
        # retrieve todos using it's ID
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            todo.delete()
            return {
                       "message": "todo {} deleted successfully".format(todo.id)
                   }, 200

        elif request.method == 'PUT':
            title = str(request.data.get('title', ''))
            description = str(request.data.get('description', ''))
            done_status = str(request.data.get('done_status', '')).lower()
            if title:
                todo.title = title
            if description:
                todo.description = description
            if done_status:
                if done_status == 'false':
                    todo.done_status = False
                elif done_status == 'true':
                    todo.done_status = True
                else:
                    # Return a message to the user telling them that they need to submit a valid done string
                    response = {
                        'message': 'done status should be either true or false.'
                    }
                    return make_response(jsonify(response)), 400
            todo.save()
            response = jsonify({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'date_created': todo.date_created,
                'date_updated': todo.date_updated,
                'done_status': todo.done_status
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'done_status': todo.done_status,
                'date_created': todo.date_created,
                'date_updated': todo.date_updated
            })
            response.status_code = 200
            return response

    return app
