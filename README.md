
# Web Scraping Gambling Odds DataBase

This is a web-scraping script that utilizes Selinium, BeautifulSoup, Pandas, and NumPy to determine what cases will output the highest expected value on the gambling site https://skin.club/en : 

The main.py will take in a text file of URL links to each case being analyzed and run through the dictionary creation method in analysis.py in order to output the expected values from each case. 


## Roadmap

[x] Create Selenium Web Scraping Algorithm

[x] Dictionary Storage Method Development

[X] Output Expected Values From All Cases in Text File

[X] Free Cases File Analysis 
 
[ ] Multi Case Analysis

[ ] Ranking System Based on Cost of Case and Expected Value

[ ] Dashboard of All Cases By Type and Value 

## Run Locally

Clone the project

```bash
  git clone https://github.com/gruenkyle/skinclub_expectedValue.git
```

Download Updated Chrome Driver for Web Search with Selenium

- https://googlechromelabs.github.io/chrome-for-testing/

Go to the project directory

```bash
  cd skinclub_expectedValue
```

Import Libraries

```bash
  pip install pandas
  pip install Selenium
  pip install BeautifulSoup4
```

Set Path on Main.py Line20 to URL Data File
``` bash 
links_array = np.genfromtxt('freeCaseData.txt', dtype=str, delimiter='\n')
```

Run Script Through Terminal
``` bash 
python main.py
```
## Usage/Examples

### analysis.py
```python

def createDictionary(url) {
  #Create Driver#

  #Find All Text Values#

  #Compute Expected Value#

  #Return Dictionary#

   caseDictionary = {
    'CaseName': caseName,
    'Odds': odds,
    'Prices': prices,
    'Expectation': expectation
   }
}
```

### main.py

```python
#Read In Link File#

#Create Pandas Data Frame# 
caseRepository = pd.DataFrame(columns=['Name', 'Price', 'Expected'])

#Iterate Over Links and Append Data#

#Print Values Found#
...

Case Name : lvl-20
Expected Value : 0.046113999999999995

...

```

## Expected Output
```python 
Case Name : lvl-3
Expected Value : 0.038869

Case Name : lvl-10
Expected Value : 0.045092999999999994

Case Name : lvl-20
Expected Value : 0.046113999999999995

Case Name : lvl-30
Expected Value : 0.09907460000000001

Case Name : lvl-40
Expected Value : 0.24282329999999994

Case Name : lvl-50
Expected Value : 0.5219931

Case Name : lvl-60
Expected Value : 1.4671465999999997
```
