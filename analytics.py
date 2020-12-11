##################################
# Get responses for each activity
##################################
# - given: question pk no
#          section

from django_pandas.io import read_frame
import pandas as pd

import matplotlib, os
import matplotlib.pyplot as plt
import numpy as np

from votes import models
from accounts.models import Student
from votes.models import Question

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


students = Student.objects.all()
section = [41, 42, 43, 44]
no_groups = [13, 10, 9, 14]
#group = range(1,13)
choice = range(1,5)

pk_no = 25
section_no = 41
criteria = 2  # criteria for group visit
# no of groups for each section
no_groups_section = no_groups[section.index(section_no)]
group = range(1, no_groups_section)
idx = pk_no - 1

r = models.Response.objects.filter(question__pk = pk_no)
# answer_key = r[0].question.correct_number
answer_key = Question.objects.get(pk=pk_no).correct_number


# first & second response
v1 = []
v2 = []

for each_group in group:
    v1.append([r.filter(student__section__section_no=section_no, student__group__group_no=each_group, vote1=c).count() for c in choice])
    v2.append([r.filter(student__section__section_no=section_no, student__group__group_no=each_group, vote2=c).count() for c in choice])

v = [v1, v2]

# plot
cols = ['{}'.format(col) for col in group]
rows = ['{}'.format(row) for row in ['1st','2nd']]

fig, axes = plt.subplots(2, no_groups_section - 1, sharex=True, sharey=True, figsize=(16,2))

for ax, col in zip(axes[0], cols):
    ax.set_title(col)

for ax, row in zip(axes[:,0], rows):
    ax.set_ylabel(row, rotation=90, size='large')

for k in range(2):
    for l in range(len(group)):
        axes[k][l].barh(choice, v[k][l], align='center')
        axes[k][l].set_yticks(choice)
        axes[k][l].set_yticklabels(choice)
        axes[k][l].invert_yaxis()
        if v[k][l][answer_key - 1] < criteria:
            axes[k][l].set_facecolor('xkcd:salmon')
plt.show()
