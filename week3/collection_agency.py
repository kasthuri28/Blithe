import psycopg2

class collection_agency():
    def _init_(self,ca_id,ca_name,ca_city,caphone_no,cawaste_type):
        self.Ca_id=ca_id
        self.Ca_name=ca_name
        self.Ca_city=ca_city
        self.CaPhone_no=caphone_no
        self.CaWaste_type=cawaste_type

    def getCaid(self):
        return(self.Ca_id)
    
    def getCaname(self):
        return(self.Ca_name)
    
    def getCacity(self):
        return(self.Ca_city)
    
    def getCaPhoneNo(self):
        return(self.CaPhone_no)
    
    def getCaWastetype(self):
        return(self.CaWaste_type)

    def Login(self):
        pass

    def register(self):
        pass

    def TrackCus(self):
        pass

    def MakeBill(self):
        pass

    def AmountCalc(self):
        pass

    def ARReq(self):
        pass