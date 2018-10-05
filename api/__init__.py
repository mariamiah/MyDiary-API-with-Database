from flask import Flask, redirect
from api.entry_views import entry
from api.user_views import user
from api.diary_views import diary
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
app.register_blueprint(entry)
app.register_blueprint(user)
app.register_blueprint(diary)

# Create swagger template
template = {
    "swagger": "2.0",
    "info": {
        "title":
        "MyDiary-API",
        "description":
        "This application allows the user to pen down their feelings",
        "version":
        "1.0.0"
    },
    "schemes": ["http", "https"]
}

# Instantiate swagger docs
swagger = Swagger(app, template=template)


@app.route('/')
def index():
    return redirect('/apidocs/')
