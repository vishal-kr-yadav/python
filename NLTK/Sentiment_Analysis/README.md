**Installation**:  
- python:
  - make sure you have python version :2.7.x installed(or above version)  
- NLTK: 
  - pip install nltk 
  - if you get any errors while installing nltk, make sure you have downloaded all the extra dataset along with nltk package.
  
 
**File/Script description:**

- SentiWordNet.txt
  - SentiWordNet is a lexical resource for opinion mining. SentiWordNet assigns to each synset of WordNet three sentiment scores: positivity, negativity, objectivity.  
  - Reference: http://sentiwordnet.isti.cnr.it/  
- data_extraction_from_websites.py
  - given list of url,it will extract the text content from the websites and write it into a file   
- sentiment.py  
  - main script for doing the sentiment analysis.
- sentimental_score.py
  - it will read the text file that was created in data_extraction steps and send the text content to sentiment script for detecting a score for the sentence.  
  
**Run:**
- python data_extraction_from_websites  
- python sentiment.py

