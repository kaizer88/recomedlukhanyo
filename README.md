# recomedlukhanyo

This is a rest framework api written in python(Django framework)

Requirement:
This api allows a user to add two dates(start date and end date) and calculate business hours between two date.

Business Rules:
The start date must always be less than end date.
Results business in in hours.

Output:

If start date is greater than end date:
  - Output shows inserted dates and error message
  
If input is valid:
  - It show inserted dates, list of valid date(weekdays excluding south african holidays and weekends) and business hours in seconds

If input is invalid:
  - It shows standard error status.HTTP_400_BAD_REQUEST message
  
  
 Test
 
 
