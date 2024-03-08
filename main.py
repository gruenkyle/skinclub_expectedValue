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

links_array = np.genfromtxt('./URL_DATA/freeCaseData.txt', dtype=str, delimiter='\n')

caseRepository = pd.DataFrame(columns=['Name', 'Price', 'Expected'])

for link in links_array:
    currDict = ca.createDictionary(link)
    caseRepository = caseRepository._append({'Name': currDict['CaseName'], 
                                             'Expected': currDict['Expectation']}, 
                                             ignore_index=True)

for index in caseRepository.index:
    print("Case Name : " + caseRepository.loc[index, 'Name'])
    print("Expected Value : " + str(caseRepository.loc[index, 'Expected']) + "\n")
