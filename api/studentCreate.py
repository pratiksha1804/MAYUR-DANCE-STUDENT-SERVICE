from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json

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
class studentCreation(Resource):
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