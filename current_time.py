from datetime import datetime , timedelta
def current_time(offset):
    time = datetime.now()
    calculated_time = time + timedelta(hours = offset)
    return calculated_time

offset = eval(input("Enter the time zone offset to GMT: "))
print(current_time(offset))