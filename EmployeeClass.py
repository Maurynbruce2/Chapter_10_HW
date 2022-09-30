# Write a class named Employee that holds attributes. Each attribute should be hidden 

class Employee: 

# Class should hold data about employess with the following attributes: 

    # Initialize each attribute with __init__ method & accept an argument for each attribute 

    def __init__(self,name,id_number,department,job_title,monthly_salary): 
        self.__name = name
        self.__idnumber = id_number
        self.__department = department 
        self.__jobtitle = job_title
        self.__monthlysalary = monthly_salary
        

    # Define employee name 

    def set_name(self,name):
        self.__name = name

    # Define employee ID number

    def set_idnumber(self,id_number):
        self.__idnumber = id_number

    # Define employee department 

    def set_department(self,department):
        self.__department = department 

    # Define employee job title 

    def set_jobtitle(self,job_title):
        self.__jobtitle = job_title

    # Define employee monthly salary

    def set_monthlysalary(self,monthly_salary):
        self.__monthlysalary = monthly_salary

    

# The employee class should have accessor methods for each attribute 

    # Return employee name 

    def get_name(self):
        return self.__name

    # Return employee ID number 

    def get_idnumber(self):
        return self.__idnumber

    # Return employee department 

    def get_department(self):
        return self.__department

    # Return employee job title 

    def get_jobtitle(self):
        return self.__jobtitle

    #Return employee monthly salary

    def get_monthlysalary(self):
        return self.__monthlysalary

    