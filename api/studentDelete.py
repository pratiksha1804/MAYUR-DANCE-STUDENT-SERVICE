from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
@swagger.model
class studentDeletion(Resource):
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
            student_gmail=payload["student_gmail"]

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