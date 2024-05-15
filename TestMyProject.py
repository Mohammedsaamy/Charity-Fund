# from project import main


# print('------------ Test --------------')
# main()


import uuid

# ديكشنري لتخزين معرف UUID لكل صف
row_uuids = {}

def ID():
    # إنشاء معرف UUID جديد لكل صف
    return str(uuid.uuid4())

# عينة من الصفوف
sample_rows = ["row1", "row2", "row3"]

# تعيين معرف UUID لكل صف
for row in sample_rows:
    row_uuids[row] = ID()


