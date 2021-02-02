from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
@swagger.model
class studentUpdate(Resource):
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

            database.updateStudent(student_name,student_address,student_gmail,student_phone,student_bdate,student_age,student_course,student_fees)
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
