# imports

import os
from datetime import *
from dateutil.relativedelta import *
import calendar
import time

# variables

TODAY = date.today()

# Grab today's date
today_date = datetime.now()
# Grab total days in month
days_in_month = calendar.monthrange(today_date.year, today_date.month)[1]
# Grab last Thursday in month
ltom = TODAY+relativedelta(day=days_in_month, weekday=TH(-1))
# Convert ltom to strftime
time_format = ltom.strftime("%B %d %Y")
# Grab days until meetup
delta = ltom - TODAY
print(delta)[1]





