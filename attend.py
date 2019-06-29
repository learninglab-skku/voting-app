from xlutils.copy import copy
from xlrd import open_workbook
import calendar
from datetime import date
# https://www.stavros.io/posts/standalone-django-scripts-definitive-guide/
import os, sys

proj_path = "/home/jun/learninglab/"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learninglab.settings.production")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from votes.models import Response


# User input for class information
YEAR = 2019
spring = range(3,7)
fall = range(9,13)
classes = ['TUESDAY', 'THURSDAY']
filename = "44.xls"
section_number = 44
semester = spring

# prepare Excel file for reading
xl_workbook = open_workbook(filename)
xl_sheet = xl_workbook.sheet_by_index(0)
# prepare Excel file for writing
book = copy(xl_workbook)
sheet1 = book.get_sheet(0)

# All response data
r = Response.objects.all()

# Calculate lecture date
lecture_date = []
for month in semester:
    mycal = calendar.monthcalendar(YEAR, month)
    for week in mycal:
        for each in classes:
            if week[getattr(calendar, each)]:
                # print(date(2019, month, week[getattr(calendar, each)]))
                lecture_date.append(date(YEAR, month, week[getattr(calendar, each)]))
# Now, can find the lecture number by
# print(lecture_date.index(date(2019, 3, 7))) # which gives 1

for month in semester:
    mycal = calendar.monthcalendar(YEAR, month)
    for week in mycal:
        for each in classes:
#            print(each)
            if week[getattr(calendar, each)]:
#                print(week[getattr(calendar, each)])
                class_date = date(YEAR, month, week[getattr(calendar, each)])
                # print(class_date)
                try:
                    student_in_each_class = r.filter(timestamp__contains=class_date,
                                                     student__section__section_no=section_number)
                    ################ Modify this later.
                    # print(student_in_each_class.count())
                    for st in student_in_each_class:
                        sid = st.student.student_no
                        for i in range(xl_sheet.nrows):
                            row_value = xl_sheet.row_values(i)
                            try:
                                if row_value[4] == sid:
                                    # print(i, sid)
                                    # calculate column number using class_date
                                    # order of the class
                                    order = lecture_date.index(class_date) # 0, 1,
                                    # print(order)
                                    # Excel file column index no: 12 + 3k + l
                                    cols = 12 + 3 * (order // 2) + (order % 2)
                                    # print(cols)
                                    sheet1.write(i, cols, 'x')
                            except:
                                pass
                            #    print("sid {0} not found. student was absent".format(sid))
                except:
                    print("attendace was not checked on {0}.".format(class_date))
# sheet1.write(0,0,'x')
book.save(filename)
