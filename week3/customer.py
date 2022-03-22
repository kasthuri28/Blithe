import psycopg2
import dblink

class customer():

    __uname = ''
    __passw = ''

    def _init_(self,c_id,c_name,c_city,house_no,phone_no,waste_type,waste_amount):

        self.C_id=c_id
        self.C_name=c_name
        self.C_city=c_city
        self.House_no=house_no
        self.Phone_no=phone_no
        self.Waste_type=waste_type
        self.Waste_amount=waste_amount


    def getCid(self):
        return(self.C_id)

    def getCname(self):
        return(self.C_name)

    def getCcity(self):
        return(self.C_city)

    def getHouseNo(self):
        return(self.House_no)

    def getPhoneNo(self):
        return(self.Phone_no)

    def getWasteType(self):
        return(self.Waste_type)
        
    def getWasteAmount(self):
        return(self.Waste_amount) 
    
    def login(self):
        pass


    def register(self):
        pass

    def viewHistory(self):
        pass

    def TrackStatus(self):
        pass

    def Booking(self):
        pass

    def CheckEwaste(self):
        pass