from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import constant
import json
@swagger.model
class studentList(Resource):
    @swagger.operation(
        description="student list",
        nickname="student list",
        parameters=[
            {
                "name": "student_gmail",
                "dataType": "String",
                "description": "student details",
                "required": False,
                "allowMultiple": False,
                "paramType": "query"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Students fetched successfully"},
            {"code": 400, "message": "Bad Request: Error on fetching student list"}
        ],
    )
    def get(self):
        try:
            student_gmail = request.args.get(constant.STUDENT_GMAIL)
            if student_gmail:
                students=database.getParticularStudent(student_gmail)
            else:
                students=database.getStudents()
            return make_response(jsonify(
                {
                    "title": "Users Details Fetched Successfully",
                    "status": HTTPStatus.OK,
                    "data": students,
                }
            ),
                HTTPStatus.OK
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from fetching students",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )