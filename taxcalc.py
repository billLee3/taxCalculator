
class FederalTaxCalculator:
    #sets up attributes based on parameters input into object instantiation
    def __init__(self, filing_type, total_income):
        #user inputted arguments
        self.filing_type = filing_type
        self.income = total_income
        #Used within several class methods
        self.taxbrackets_des = {
            "single": {.37: 578125, .34: 231250, .32: 182100, .24: 95375, .22: 44725, .12: 11000, .10: 0},
            "married filing jointly": {.37: 693750, .34: 462500, .32: 364200, .24: 190750, .22: 89540, .12: 22000, .10: 0}
        }
        #Used to store the users tax_amount
        self.tax_amount = 0
        
    #Function to return the amount owed in federal taxes taking a standard deduction into effect using the users filing type and income to filter.
    def getFedTaxAndRate(self):
        #filtering down dictionary based on filing type
        applicable_fed_tax_brackets = self.taxbrackets_des[self.filing_type]
        previous_key_value = 0
        tax_amount = 0
        temp_income = 0
        #standard deduction logic - standard deduction rates for 2023 gathered from irs.gov
        if (self.filing_type == "single"):
            temp_income = self.income - 13850
        elif (self.filing_type == "married filing jointly"):
            temp_income = self.income - 27700

        #Dictionary traversal logic
        for key in applicable_fed_tax_brackets:
            #Handles negative values after standard deduction logic
            if(temp_income < 0):
                print("Your standard deduction eliminated your need to pay taxes. ")
                break
            #finds the highest tax bracket the user would have to pay for and the amount to pay for in this bracket.
            elif(temp_income > applicable_fed_tax_brackets[key]):
                #value after standard deduction - the threshold value for the tax bracket
                remainder = temp_income - applicable_fed_tax_brackets[key]
                #the remainder is the taxable amount within the tax bracket multiplied by the brackets rate
                tax_amount += remainder * key
                #temp_incme and previous_key_value are used to set up the following traversals
                temp_income -= remainder
                previous_key_value = applicable_fed_tax_brackets[key]
            #Based on the logic in the previous step the temp_income should always meet the previous key value. This allows us to use the previous value and the current value
            elif(temp_income == previous_key_value):
                #follows a similar flow from the previous logic
                remainder = previous_key_value - applicable_fed_tax_brackets[key]
                tax_amount += remainder * key
                temp_income -= remainder
                previous_key_value = applicable_fed_tax_brackets[key]
        self.tax_amount = tax_amount
        return tax_amount

    #Outputs the average tax rate after applying the different rates to the different brackets of income for the user
    def getAverageRate(self):
        rate = (self.tax_amount/self.income) * 100 
        return rate

#Children class of FedTaxCalculator. Adding in the State to find the state income tax the user falls intos
class StateTaxCalculator(FederalTaxCalculator):
    def __init__(self, filing_type, total_income, state):
        super().__init__(filing_type, total_income)
        self.state = state
        self.statetaxbrackets_des = {
            "AL": {"single": {.05: 3000, .04: 500, .02: 0},
                   "married filing jointly": {.05: 6000.01, .04: 1000.01, .02:0}},
            "TN": {"single": {1: 0}, "married filingjointly": {1:0}}
        }
    #Method returns the amount owed in state taxes.
    def getStateTaxAmount(self): 
        applicable_state_tax_brackets = self.statetaxbrackets_des[self.state][self.filing_type]   
        state_tax_amount = 0
        state_temp_income = self.income * 1
        for key in applicable_state_tax_brackets:
            #Base case if below last threshold
            if((self.income <= 500 and self.filing_type == "single") or (self.income <= 1000 and self.filing_type == "married filing jointly")):
                state_tax_amount = self.income * .02
            #same logic as the federal tax calculator from here on out
            elif(state_temp_income > applicable_state_tax_brackets[key]):
                remainder = state_temp_income - applicable_state_tax_brackets[key]
                state_tax_amount += remainder * key
                state_temp_income -= remainder
                previous_key_value = applicable_state_tax_brackets[key]
            elif(state_temp_income == previous_key_value):
                remainder = previous_key_value - applicable_state_tax_brackets[key]
                state_tax_amount += remainder * key
                state_temp_income -= remainder
                previous_key_value = applicable_state_tax_brackets[key]
        return state_tax_amount

    #Method returns the total amount owed in state and federal taxes 
    def getStateAndFedTaxes(self):
        #gets fed tax amount from the parent class
        fed_taxes = self.getFedTaxAndRate()
        #gets the state tax amount from the current class
        state_taxes = self.getStateTaxAmount()
        total_taxes = fed_taxes + state_taxes
        return total_taxes