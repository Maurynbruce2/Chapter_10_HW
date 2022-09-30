# Write a program that will creat the following employees (Table 1) as well as the payroll deductions (Table 2)
# The program should also create a report that shows net pay for Jimmy after his deductions have been subtracted


# Import name of the files

import EmployeeClass as e 
import PayrollDeductionClass as pd 

# The main function 
def main():

# Create Table 1 with information about Jimmy

    Jimmy = e.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

    Deduction1 = pd.Payroll_Deduction('Food Court','8/14/2022', 22.50, 39119)
    Deduction2 = pd.Payroll_Deduction('Gift Contribution', '8/12/2022', 25.00, 58475)
    Deduction3 = pd.Payroll_Deduction('Food Court', '8/17/2022', 15.25, 21547)
    Deduction4 = pd.Payroll_Deduction('Vending Machine', '8/22/2022', 3.00, 58475)
    Deduction5 = pd.Payroll_Deduction('Vending Machine', '8/5/2022', 2.75, 58475)

    Deduction_List = [Deduction1, Deduction2, Deduction3, Deduction4, Deduction5]

    net_pay = Jimmy.get_monthlysalary()

    for Deduction in Deduction_List: 
        if pd.Payroll_Deduction.get_employeeid(Deduction) == Jimmy.get_idnumber():
            net_pay -= pd.Payroll_Deduction.get_chargeamount(Deduction)



    #print report that shows net pay for Jimmy after his deductions have been subtracted

    print('*** Employee Pay ***')
    print('Name:' , e.Employee.get_name(Jimmy))
    print('ID Number:' , e.Employee.get_idnumber(Jimmy))
    print('Department:' , e.Employee.get_department(Jimmy))
    print('Gross Pay:' , e.Employee.get_monthlysalary(Jimmy))    
    print('Net Pay: $', net_pay , sep='')
    

main()