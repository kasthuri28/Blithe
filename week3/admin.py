class Admin:
    def _init_(self,admin_id,admin_name):
        self.Admin_id=admin_id
        self.Admin_name=admin_name

    def getAdminId(self):
        return(self.Admin_id)

    def getAdminName(self):
        return(self.Admin_name)

    def RemoveCA(self):
        pass