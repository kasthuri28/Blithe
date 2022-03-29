import datetime
class Booking:
    def _init_(self,b_id):
        self.B_id=b_id
        self.B_date=datetime.date.today()
        self.B_time=datetime.time.strftime()
    
    def getBid(self):
        return(self.B_id)

    def Book(self):
        pass