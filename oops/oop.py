# creating a obj

class Book:
    name:str="Andy Macnab"
    price:int="250"
    
book = Book()
print(book.name, book.price)


from datetime import datetime
class TimeTeller:
    def __init__(self, time:str, day:str, year:str ):
        """
        if not isinstance(time,str):
            raise TypeError(f"time must be in str")
        if not isinstance(day,str):
            raise TypeError(f"day must be in str")
        if not isinstance(year,str):
            raise TypeError(f"year must be in str")
            """
        checks = {
            "time": (time, str),
            "day": (day, str),
            "year": (year, str)}
        for field, (value, type) in checks.items():
            if not isinstance(value, type):
                raise TypeError(f"{field} must be type {type} ")
        
        self.time= time
        self.day= day
        self.year=year
    
time = TimeTeller(datetime.now().day, datetime.now().year, False)
print(time.time, time.day, time.year) #  raise TypeError(f"time must be in str")




    