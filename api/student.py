from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
import constant

# {
# "student_name":"pratiksha",
# "student_address":"old sangvi",
# "student_gmail":"pratiksha@gmail.com",
# "student_phone":"7765796336",
# "student_bdate":"18/04/1997",
# "student_age":"23",
# "student_course":"Dance",
# "student_fees":"1000"
#
# }


@swagger.model
class Student(Resource):
    @swagger.operation(
        description="student registration",
        nickname="student registration",
        parameters=[
            {
                "name": "body",
                "dataType": "string",

                "required": True,
                "allowMultiple": False,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Student Registered succesfully"},
            {"code": 400, "message": "Bad Request: Error on resgistering student"}
        ],
    )
    def post(self):
        try:
            payload = json.loads(request.data.decode())
            student_name=payload["student_name"]
            student_address=payload["student_address"]
            student_gmail=payload["student_gmail"]
            student_phone=payload["student_phone"]
            student_bdate=payload["student_bdate"]
            student_age=payload["student_age"]
            student_course=payload["student_course"]
            student_fees=payload["student_fees"]

            database.addStudent(student_name,student_address,student_gmail,student_phone,student_bdate,student_age,student_course,student_fees)
            return make_response(jsonify(
                {
                    'title': "Student Registered Successfully",
                    "status": HTTPStatus.CREATED
                }
            ),
                HTTPStatus.CREATED,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from student registration",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )

    @swagger.operation(
    description="student deletion",
    nickname="student deletion",
    parameters=[
        {
            "name": "body",
            "dataType": "string",

            "required": True,
            "allowMultiple": False,
            "paramType": "body"
        }
    ],
    responseMessages=[
        {"code": 200, "message": "Student deleted succesfully"},
        {"code": 400, "message": "Bad Request: Error on deleting student"}
    ],
    )
    def delete(self):
            try:
                payload = json.loads(request.data.decode())
                student_gmail = payload["student_gmail"]

                database.deleteStudent(student_gmail)
                return make_response(jsonify(
                    {
                        'title': "Student Deleted Successfully",
                        "status": HTTPStatus.OK
                    }
                ),
                    HTTPStatus.OK,
                )


            except Exception as e:
                return make_response(jsonify(
                    {
                        'title': "Unsuccessful from user deletion",
                        "status": HTTPStatus.BAD_REQUEST,
                        "error": {
                            "message": str(e)
                        }
                    }
                ),
                    HTTPStatus.BAD_REQUEST,
                )

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
                students = database.getParticularStudent(student_gmail)
            else:
                students = database.getStudents()
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

    @swagger.operation(
        description="student update",
        nickname="student update",
        parameters=[
            {
                "name": "body",
                "dataType": "string",

                "required": True,
                "allowMultiple": False,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Student updated succesfully"},
            {"code": 400, "message": "Bad Request: Error on updating student"}
        ],
    )
    def put(self):
        try:
            payload = json.loads(request.data.decode())
            student_name = payload["student_name"]
            student_address = payload["student_address"]
            student_gmail = payload["student_gmail"]
            student_phone = payload["student_phone"]
            student_bdate = payload["student_bdate"]
            student_age = payload["student_age"]
            student_course = payload["student_course"]
            student_fees = payload["student_fees"]

            database.updateStudent(student_name, student_address, student_gmail, student_phone, student_bdate,
                                   student_age, student_course, student_fees)
            return make_response(jsonify(
                {
                    'title': "Student updated Successfully",
                    "status": HTTPStatus.OK
                }
            ),
                HTTPStatus.OK,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from student updation",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )