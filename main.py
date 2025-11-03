# importing from class file
import taxcalc
# importing math module for round function. 
import math
#Used to validate state options later
available_states = ["AL", "TN"]

#Function to gather all of the necessary inputs and to type check these inputs until valid inputs are received
def gather_inputs(tax_type):
    valid_entries = False
    filing_type = input("Please input your filing type either single or married filing jointly. Be sure to type your selection correctly. \n").lower()
    
    while valid_entries == False:
        #Conditional logic for filing type
        if filing_type == "single" or filing_type == "married filing jointly":
            #Exception handling block for numeric value
            try:
                total_income = float(input("Please provide your income in numeric form: "))
                #Conditional logic to determine which calculator is being used. 
                if tax_type == "state":
                    state = input("Enter the abbreviation for your state: ").upper()
                    valid_selection = False
                    while valid_selection == False:
                        #Ensuring that the data for the selected state is in the current data structure
                        if state in available_states:
                            #exits the while loop
                            valid_selection = True
                        else:
                            print("You did not enter state abbreviation that is in our system.")
                            #Keeps asking for the same input value until a valid selection is made
                            state = input("Please enter a different state abbreviation: ")
                    #exits the while loop determined by valid_entries for state tax calculator
                    valid_entries = True
                elif tax_type == "federal":
                    #exits the while loop for the federal tax calculator
                    valid_entries = True
            #Catches all scenarios where the user did not enter a number        
            except ValueError:
                print("You did not enter a number. ")
        #catches all scenarios where the user does not select single or married filing jointly
        else: 
            print("Invalid filing type. Try again!")
            filing_type = input("Please input your filing type either single or married filing jointly. Be sure to type your selection correctly. \n").lower()
    #The conditional varies the outputs depending on the calculator selected. 
    if tax_type == "federal":
        return filing_type, total_income
    elif tax_type == "state":
        return filing_type, total_income, state

#Menu options to be printed later
options = ["FEDTAX: Calculate federal tax amount and marginal tax rate", 
            "STATETAX: Calculate state tax amount", 
            "TOTALTAX: Calculate your total tax amount both federal and state",
            "QUIT: To quit the application"]

# General intro to application
print("Welcome to the tax calculation app \n----------------------------------- ")
#While loop for the whole program. Lets the user continue to enter values
game_over = True
while game_over:
    #Printing options
    print("Please select from one of the following options.\n------------------------------------------------")
    for option in options:
        print(option)
    print("Input the portion of each option in all caps.")
    #Menu selector
    selection = input("Enter your selection below: \n").upper()
    
    #Different scenarios based on the option selected. 
    if selection == "FEDTAX":
        #Calling function to gather required parameters for fedtaxcalc
        filing_type, total_income = gather_inputs(tax_type="federal")
        #Instantiation
        fedtaxcalc = taxcalc.FederalTaxCalculator(filing_type=filing_type, total_income=total_income)
        #calling method to receive federal tax amount
        tax_amount = fedtaxcalc.getFedTaxAndRate()
        
        print(f"Your total federal tax owed is ${tax_amount}.")
        #Nested Logic for Average Tax Rate
        selection_two = input("Would you like to know your average tax rate? Enter Y for yes or N for no: ").upper()
        #Used to break the while loop later
        valid_selection = False
        #While loop to valid response
        while valid_selection == False: 
            if selection_two == "Y":
                average_rate = fedtaxcalc.getAverageRate()
                print(f"Your average tax rate is {average_rate}%")
                valid_selection = True
            elif selection_two == "N":
                valid_selection = True
            #Catches all values aside from Y or N
            else:
                print("You entered an invalid input")
    #Logic if you just want to know the amount owed in state taxes
    elif selection == "STATETAX":
        #Calling method to gather necessary parameters for statetaxcalc
        filing_type, total_income, state = gather_inputs(tax_type="state")
        #Instantiation
        statetaxcalc = taxcalc.StateTaxCalculator(filing_type=filing_type, total_income=total_income, state=state)
        #object method to get the state tax amount
        state_tax_amount = statetaxcalc.getStateTaxAmount()
        format_state_amount = round(state_tax_amount, 3)
        print(f"Your total state tax owed is ${format_state_amount}")
    #Logic for the total value owed in state taxes
    elif selection == "TOTALTAX":
        #Using the state logic within gather_inputs() because the state tax needs to be gathered
        filing_type, total_income, state = gather_inputs(tax_type="state")
        #I only needed to instantiate the statetaxcalculator because it inherits from the federal tax calculator
        #Because it inherits from the federal tax calculator I can use its method to gather the fed tax. 
        statetaxcalc = taxcalc.StateTaxCalculator(filing_type=filing_type, total_income=total_income, state=state)
        total_taxes = statetaxcalc.getStateAndFedTaxes()
        formatted_taxes = round(total_taxes, 2)
        print(f'Your total tax amount including federal and state taxes is ${formatted_taxes}.')
    #Quit option allows the user to exit the while loop
    elif selection == "QUIT":
        game_over = False
    #Catches any entry that doesn't match the available options. 
    else:
        print("You did not pick an option from the selection list. \n------------------------------------------------------------------------------------------------")    
               

