# http://www.pythonchallenge.com/pc/return/cat.html
# and its name is uzi, you'll hear from him later
# should we change this pic to a wav file?
# NO. Notice that this page didn't contains number 15.
# we try http://www.pythonchallenge.com/pc/return/uzi.html
# a canlender
# title whom?
# 1xx6-01-26 Monday
# OK, let's find the year
# find which musican born or die in this time
# in the source code there is two hints: <!-- he ain't the youngest, he is the second --> <!-- todo: buy flowers for tomorrow -->


import datetime

for x in range (99):
    year = 1000+10*x+6
    d = datetime.date(year,1,26)
    if (d.weekday()==0 and year%4==0):
        print(d.isoformat())


#1176-01-26
#1356-01-26
#1576-01-26
#1756-01-26
#1976-01-26

# But we look for tomorrow 
# so it's 1756-1-27
# it's Wolfgang Amadeus Mozart's birthday