def DayFormat(dayNumber, formatt):
    format_lut = {
        'day':['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'shortday':['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'char':['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
    }
    return format_lut[formatt][dayNumber-1]

print(DayFormat(2, "day"))