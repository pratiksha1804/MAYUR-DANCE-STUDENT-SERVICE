import os
from config import app
from api import api
from api.studentCreate import studentCreation
from api.studentDelete import studentDeletion
from api.studentList import studentList
from api.updateStudent import studentUpdate

api.add_resource(studentCreation,"/api/studentCreate")
api.add_resource(studentDeletion,"/api/studentDelete")
api.add_resource(studentList,"/api/get_all_students")
api.add_resource(studentUpdate,"/api/update_student")

if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5001, debug=True)