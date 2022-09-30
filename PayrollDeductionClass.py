# Write a class that represents a payroll deduction transaction. 

class Payroll_Deduction: 
 
 # The class's __init__ method should accept an argument for each attribute 
 # Initialize the attributes using the __init__ method 

    def __init__(self,description,date,charge_amount,employee_id):
        self.__description = description
        self.__date = date
        self.__chargeamount = charge_amount
        self.__employeeid = employee_id

# Each instance should have the description, date, charge amount, and employee ID as attributes. All attributes should be hidden 

    # Define description

    def set_description(self,description):
        self.__description = description

    # Define date

    def set_date(self,date):
        self.__date = date

    # Define charge amount 

    def set_chargeamount(self,charge_amount):
        self.__chargeamount = charge_amount

    # Define employee id 

    def set_employeeid(self,employee_id):
        self.__employeeid = employee_id 

# The class should have accessor methods for each attribute

    # Return description 

    def get_description(self):
        return self.__description

    # Return date 

    def get_date(self):
        return self.__date

    # Return charge amount 

    def get_chargeamount(self):
        return self.__chargeamount

    # Return employee id

    def get_employeeid(self):
        return self.__employeeid