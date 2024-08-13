1\. Content Extraction

Upon inspection of the website, I realized that the article links are dynamically loaded after the initial page load. This meant that I would have to fully render the page to find the articles related to menstrual health or contraception. If I were to build this further, I would have installed a webdriver so that I can execute the Javascript and fully render the HTML. This would have allowed me to scrape the articles directly from the source link. I did not do this because I did not want to install additional software on my computer without needing to. Instead, I manually input the links to the articles and scraped the data from that using the python package beautifulsoup. I examined each article’s HTML structure to find commonalities between each page and also where the important information that was needed was stored. From there, I standardized a way to extract all the data from the five articles. 

2\.  LLM-Powered Content Analysis

I used the Stanza library to perform named entity recognition on the input text to find medical terms, conditions and treatments. Stanza is a comprehensive NLP toolkit that supports various tasks, including tokenization, part-of-speech tagging, dependency parsing, and named entity recognition. Specifically, I utilized the i2b2 NER processor from the "mimic" package, which is tailored for recognizing medical entities like diseases, treatments, and symptoms. This was particularly useful for processing the healthcare-related content from the text. To scale this, I may train my own model on labeled text to better extract the relevant terms. 

For key phrase extraction, I used the YAKE library. YAKE is an unsupervised and language-independent method for extracting key phrases from text. I started by instantiating a KeywordExtractorfrom the YAKE library, specifying parameters such as the language (lan="en" for English), the maximum length of the n-grams (n=4), the deduplication threshold (dedupLim=0.9), and the number of top key phrases to extract (top=10). I then used this extractor to identify the most relevant key phrases from the selected text, printing each key phrase along with its corresponding score, which indicates its significance in the text.

In general for tasks like this, it would probably be best to train our own models if we have the data, but if not, I would use the largest LLM’s like GPT. This would allow us to have some of the most recent data and better context reasoning than the libraries I used. I used the libraries for convenience for this task. 

3\.  
I used the FastAPI framework to create a web API that processes text data. The API accepts a POST request at the /process-text/ endpoint, where it receives a JSON payload containing a text string. The text is then converted to uppercase and returned in the response. To define the structure of the incoming data, I used Pydantic's BaseModel, ensuring that the input text is properly validated. The API is run using uvicorn, a high-performance ASGI server, and it listens on port 8000\. This setup provides a simple yet powerful way to handle text processing tasks via a web interface. I chose the FastAPI framework for its high efficiency and performance. 