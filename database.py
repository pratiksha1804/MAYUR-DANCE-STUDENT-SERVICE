from config import app
from config import mongo

def addStudent(student_name,student_address,student_gmail,student_phone,student_bdate,student_age,student_course,student_fees):
    student_info={
        "name":student_name,
        "address":student_address,
        "gmail":student_gmail,
        "phone_no":student_phone,
        "birth_date":student_bdate,
        "age":student_age,
        "course":student_course,
        "fees":student_fees
    }
    return mongo.db.STUDENT_INVENTORY.insert_one(student_info)

def deleteStudent(student_gmail):
    student_info={
        "gmail":student_gmail
    }
    return mongo.db.STUDENT_INVENTORY.delete_one(student_info)

def getStudents():
    students = mongo.db.STUDENT_INVENTORY.find({}, {'_id': False})
    student_list = []
    if students:
        for student in students:
            student_list.append(student)
        return student_list
    return None

def getParticularStudent(student_gmail):
    students = mongo.db.STUDENT_INVENTORY.find_one({"gmail":student_gmail}, {'_id': False})
    if students:
        return students
    return None

def updateStudent(student_name,student_address,student_gmail,student_phone,student_bdate,student_age,student_course,student_fees):
        my_query = {"student_gmail": student_gmail}
        new_values = {"$set": {"gmail":student_gmail,"phone_no":student_phone,"birth_date":student_bdate
                               ,"age":student_age,"course":student_course,"fees":student_fees}}
        return mongo.db.STUDENT_INVENTORY.update(my_query, new_values)