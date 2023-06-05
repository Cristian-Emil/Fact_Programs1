"""
Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/
"""
#-----------------------------------------------------------------------------------------------------------------------
# Import date class from datetime module
from datetime import date

# Returns the current local date
today = date.today()
print("Today date is: ", today)
#
#
# #-----------------------------------------------------------------------------------------------------------------------
# # Import datetime class from datetime module
# from datetime import datetime
#
# # returns current date and time
# now = datetime.now()
# print("now = ", now)
#
#
# #-----------------------------------------------------------------------------------------------------------------------
# # importing datetime module for now()
# import datetime
#
# # using now() to get current time
# current_time = datetime.datetime.now()
#
# # Printing attributes of now().
# print("The attributes of now() are : ")
#
# print("Year: ", end="")
# print(current_time.year)
#
# print("Month: ", end="")
# print(current_time.month)
#
# print("Day: ", end="")
# print(current_time.day)