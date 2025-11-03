## PyTax

### Description
---
The purpose of this application was to better understand how the US tax brackets work.
I learned a lot about how the more money you make, the more you traverse through different tax brackets.
My initial, naive understanding was that a 22% tax rate would be on every dollar made. This is not the case. 

### Motivation
---
Like a lot of the projects I build. I wanted a better understanding of how something in the real world worked.
Because I had been using a tax calculator app frequently, I figured I should probably just learn how taxes are calculated for my own self-awareness.
This approach ended up being a great thing for me because it helped me understand how federal and state taxes work together and the algorithm that gets someone to their effective tax rate.

### Quick Start
---
Clone the repo to your machine. Make sure that you have python3 installed on your machine. 
Run the `python3 main.py` if you are using linux you may have to run the sudo command beforehand. 
The app is all through the console. The only 2 state options available are "AL" or "TN".

### Usage
---
The application will allow the user to start over using a while loop to continue inputting information. 

The application will give you four options to choose from. 
- FEDTAX - this will ask the user several questions (Q1, Q2, and Q4 below) and return the federal tax amount and marginal tax rate.
- STATETAX - this will ask the user several questions (Q1, Q2, and Q3 below) and return the state tax amount owed.
- TOTALTAX - this command will ask the user several questions (Q1, Q2, and Q3 below) and return the total tax amount summation of federal and state taxes.

Questions:
1.) Filing Type: Married filing jointly or single
2.) Income Amount (Yearly)
Gather the user's total family income. If married filing jointly, this will include their spouse's income. If it is a non-numeric value, the program will throw an error.
3.) Please enter your state abbreviation. (Only working options are AL or TN)
4.) Would you like to know your average tax rate?

#### Lessons Learned
---
How to slide through the tax brackets and identify when you breached into the next one. While carrying the remainder of the funds to the next tax bracket
How to use different data structures and algorithms to effectively solve this issue for various pay ranges and states of residence. 
