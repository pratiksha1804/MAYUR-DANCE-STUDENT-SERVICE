import os
from config import app
from api import api
from api.student import Student


api.add_resource(Student,"/api/student")


if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5001, debug=True)
