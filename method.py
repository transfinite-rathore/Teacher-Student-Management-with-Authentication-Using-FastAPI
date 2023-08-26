# from faker import Faker
# from Databases.models import Student,Teacher
# from Databases.session import SessionLocal
# from Databases.schema import StudentModel,TeacherModel
# import random
#
# #
# db=SessionLocal()
# li=[
#     {'name': 'Christopher Pollard', 'Math_marks': 83, 'Science_marks': 83, 'Hindi_marks': 64, 'English_marks': 75, 'Total_marks': 305, 'Rank': 12, 'Teacher_id': 1, 'roll_no': 4},
#     {'name': 'Shelley Newton', 'Math_marks': 69, 'Science_marks': 83, 'Hindi_marks': 65, 'English_marks': 89, 'Total_marks': 306, 'Rank': 7, 'Teacher_id': 5, 'roll_no': 19},
#     {'name': 'Andrew Suarez', 'Math_marks': 72, 'Science_marks': 85, 'Hindi_marks': 74, 'English_marks': 75, 'Total_marks': 306, 'Rank': 7, 'Teacher_id': 1, 'roll_no': 1},
#     {'name': 'Bryan Parker', 'Math_marks': 72, 'Science_marks': 69, 'Hindi_marks': 71, 'English_marks': 85, 'Total_marks': 297, 'Rank': 17, 'Teacher_id': 2, 'roll_no': 3},
#     {'name': 'Donna Clarke', 'Math_marks': 79, 'Science_marks': 88, 'Hindi_marks': 89, 'English_marks': 90, 'Total_marks': 346, 'Rank': 18, 'Teacher_id': 5, 'roll_no': 7},
#     {'name': 'Michelle Mack', 'Math_marks': 64, 'Science_marks': 85, 'Hindi_marks': 64, 'English_marks': 64, 'Total_marks': 277, 'Rank': 2, 'Teacher_id': 1, 'roll_no': 12},
#     {'name': 'Stacy Allen', 'Math_marks': 85, 'Science_marks': 81, 'Hindi_marks': 81, 'English_marks': 76, 'Total_marks': 323, 'Rank': 19, 'Teacher_id': 4, 'roll_no': 20},
#     {'name': 'Danielle Lewis', 'Math_marks': 86, 'Science_marks': 70, 'Hindi_marks': 93, 'English_marks': 66, 'Total_marks': 315, 'Rank': 8, 'Teacher_id': 2, 'roll_no': 5},
#     {'name': 'Robert Montoya', 'Math_marks': 69, 'Science_marks': 78, 'Hindi_marks': 64, 'English_marks': 63, 'Total_marks': 274, 'Rank': 15, 'Teacher_id': 2, 'roll_no': 17},
#     {'name': 'David Hoover', 'Math_marks': 61, 'Science_marks': 60, 'Hindi_marks': 89, 'English_marks': 61, 'Total_marks': 271, 'Rank': 15, 'Teacher_id': 5, 'roll_no': 6},
#     {'name': 'Julie Mendoza', 'Math_marks': 80, 'Science_marks': 74, 'Hindi_marks': 78, 'English_marks': 95, 'Total_marks': 327, 'Rank': 20, 'Teacher_id': 4, 'roll_no': 10},
#     {'name': 'Paul Erickson', 'Math_marks': 81, 'Science_marks': 78, 'Hindi_marks': 94, 'English_marks': 66, 'Total_marks': 319, 'Rank': 20, 'Teacher_id': 4, 'roll_no': 15},
#     {'name': 'Austin Cook', 'Math_marks': 76, 'Science_marks': 84, 'Hindi_marks': 85, 'English_marks': 76, 'Total_marks': 321, 'Rank': 10, 'Teacher_id': 3, 'roll_no': 2},
#     {'name': 'Katherine Brandt', 'Math_marks': 74, 'Science_marks': 65, 'Hindi_marks': 62, 'English_marks': 88, 'Total_marks': 289, 'Rank': 16, 'Teacher_id': 4, 'roll_no': 11},
#     {'name': 'Pamela Johnson', 'Math_marks': 80, 'Science_marks': 79, 'Hindi_marks': 76, 'English_marks': 75, 'Total_marks': 310, 'Rank': 1, 'Teacher_id': 4, 'roll_no': 14},
#     {'name': 'Shannon Reed', 'Math_marks': 68, 'Science_marks': 71, 'Hindi_marks': 83, 'English_marks': 72, 'Total_marks': 294, 'Rank': 21, 'Teacher_id': 3, 'roll_no': 18},
#     {'name': 'Nancy Grant', 'Math_marks': 62, 'Science_marks': 74, 'Hindi_marks': 88, 'English_marks': 74, 'Total_marks': 298, 'Rank': 19, 'Teacher_id': 3, 'roll_no': 13},
#     {'name': 'Jeremy George', 'Math_marks': 73, 'Science_marks': 78, 'Hindi_marks': 87, 'English_marks': 65, 'Total_marks': 303, 'Rank': 4, 'Teacher_id': 2, 'roll_no': 9},
#     {'name': 'Howard Harris DVM', 'Math_marks': 92, 'Science_marks': 63, 'Hindi_marks': 73, 'English_marks': 62, 'Total_marks': 290, 'Rank': 18, 'Teacher_id': 3, 'roll_no': 8},
#     {'name': 'Robert Bell MD', 'Math_marks': 70, 'Science_marks': 62, 'Hindi_marks': 62, 'English_marks': 87, 'Total_marks': 281, 'Rank': 2, 'Teacher_id': 3, 'roll_no': 16}
#
#     ]
#
# fake=Faker()
#
# # def create_student():
# #     li=[]
# #     for i in range(20):
# #         stu = {}
# #         stu["name"]= fake.name()
# #         stu["Math_marks"]=random.randint(60,95)
# #         stu["Science_marks"] = random.randint(60, 95)
# #         stu["Hindi_marks"] = random.randint(60, 95)
# #         stu["English_marks"] = random.randint(60, 95)
# #         stu["Total_marks"]=stu["Math_marks"]+stu["Science_marks"]+stu["Hindi_marks"]+stu["English_marks"]
# #         stu["Rank"]=random.randint(1,21)
# #
# #         stu["Teacher_id"]=random.randint(1,5)
# #         li.append(stu)
# #     sorted_data=sorted(li,key=lambda s:s["name"])
# #     final_list=[]
# #     for i in range(len(sorted_data)):
# #         sorted_data[i]["roll_no"]=i+1
# #     #print(sorted_data)
# #     return li
# # # def sorting(li:[]):
# # #     pass
# # students=create_student()
# # # print(li)
# # print(students)
# # def teacher_entry()
#
# '''
# to generate fake teacher data
# teacher_name = Column(String)
# mobile_no = Column(String)
# email = Column(String, unique=True)
# password = Column(String)
# '''
#
# # def create_tech():
# #     teachers=[]
# #     for i in range(5):
# #         di={}
# #         di["teacher_name"]=fake.name()
# #         di["mobile_no"]=fake.phone_number()
# #         di["email"]=fake.email()
# #         di["password"]=di["teacher_name"].split()[-1]+"@123"
# #         teachers.append(di)
# #     return teachers
# #
# #
# # teachers=create_tech()
# teachers_ty =[
#     {'teacher_name': 'Tammie Ingram', 'mobile_no': '3842635373', 'email': 'williamsheather@example.org', 'password': 'Ingram@123'},
#            {'teacher_name': 'Tiffany Howard', 'mobile_no': '7163491081', 'email': 'mcruz@example.org', 'password': 'Howard@123'},
#            {'teacher_name': 'Robert Lang', 'mobile_no': '7916434578', 'email': 'richard14@example.com', 'password': 'Lang@123'},
#            {'teacher_name': 'Kimberly Snyder', 'mobile_no': '9733013285', 'email': 'aaronjohnson@example.org', 'password': 'Snyder@123'},
#            {'teacher_name': 'Andrew Mills', 'mobile_no': '9854763214', 'email': 'ortegakrista@example.org', 'password': 'Mills@123'}
#           ]
#
#
#
#
#
#
#
#
#
#
# # teachers=db.query(Teacher).all()
# #
# # for teacher in teachers:
# #     teacher_dict = {
# #         "id": teacher.id,
# #         "teacher_name": teacher.teacher_name,
# #         "mobile_no": teacher.mobile_no,
# #         "email": teacher.email,
# #         "password": teacher.password
# #     }
# #     print(teacher_dict)
# #
