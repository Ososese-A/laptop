from flask import Flask
from views import views

#To initialize 
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")



if __name__ == '__main__':
    #the default port is 5000
    app.run(debug=True, port=800)