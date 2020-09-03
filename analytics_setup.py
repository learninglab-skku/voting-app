from django_pandas.io import read_frame
import pandas as pd

import matplotlib, os
import matplotlib.pyplot as plt
import numpy as np

from votes import models
from accounts.models import Student

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
