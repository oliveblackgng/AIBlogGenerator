MONTH={ "JAN":"JANUARY",
        "FEB":"FEBRUARY",
        "MAR":"MARCH", # here a string value is assigned to another "code" string
        "APR":"APRIL",
        "MAY":"MAY",
        "JUN":"JUNE",
        "JUL":"JULY",
        "AUG":"AUGUST",
        "SEP":"SEPTEMBER",
        "OCT":"OCTOBER",
        "NOV":"NOVEMBER",
        "DEC":"DECEMBER"} # a grid or a matrix type thing
print(MONTH.get("DEC")) # it 'gets' the string related to the "code"
print(MONTH["JAN"])
print(MONTH.get("DAY","INVALID")) # gets the "code" string but if non-existent, it prints the second part
print(MONTH.get("JUL","INVALID"))