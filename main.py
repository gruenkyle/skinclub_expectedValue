#######################################
#
#      Utilizes the Text File Containing 
#   Each URL String and Stores all Dictionary Information
#   Then Prints Name and Expected Value
#
#          Author : Kyle Gruen
#          Date : 02/27/2024
#
#######################################

# Import Statements #
import numpy as np
import pandas as pd

import analysis as ca

# Main Script #

links_array = np.genfromtxt('urlDataBase.txt', dtype=str, delimiter='\n')

caseRepository = pd.DataFrame(columns=['Name', 'Price', 'Expected Value'])

for link in links_array:
    currDict = ca.createDictionary(link)
    caseRepository = caseRepository._append({'Name': currDict['CaseName']}, ignore_index=True)
    caseRepository = caseRepository._append({'Expected Value': currDict['Expectation']})


for case in caseRepository:
    print("Case Name : " + case['Name'] + "\n")
    print("Expected Value : " + case['Expected Value'] + "\n\n")
