# Article Recommendation Using Word2vec (From the course MSDS692 - Data Acquisiton @USF)

- Summary: Developed an article recommendation system using by calculating the Euclidean distances between a corpus of articles using the word2vec from Stanford's GloVe project, trained on Wikipedia, and a corpus of BBC text articles.
  
- Technologies Used: Python, Flask for web server, and PyTest for testing.

# Web Server and User Interface

<p align="center"> <kbd><img width="224" alt="Screenshot 2023-11-23 at 1 19 13 PM" src="https://github.com/eren-bardak/Word2vec-BBCArticleRecommendation/assets/138029233/e6dd2b2e-e0fe-4ede-ada0-095d8118434c"></img></kbd> </p>

- Flask Web Server:
    Built to respond to requests for a list of articles and individual articles.
    Hosted locally for testing purposes.

- User Interface:
    Users can view a list of articles and select one to read the full text.
    Each article page displays the content along with five recommended articles.
  
  <p align="center"> <kbd><img width="1500" alt="Screenshot 2023-11-23 at 1 18 12 PM" src="https://github.com/eren-bardak/Word2vec-BBCArticleRecommendation/assets/138029233/4c649cab-20ba-4812-8530-e3eae7d88f5f"></img></kbd> </p>

- Testing and Validation:
    Validated the functionality of doc2vec.py using PyTest (test_doc2vec.py).
    Tested the web server with pytest test_server.py, ensuring it runs correctly and responds as expected.
