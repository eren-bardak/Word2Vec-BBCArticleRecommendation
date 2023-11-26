# Article Recommendation Using Word2vec (From the course MSDS692 - Data Acquisiton @USF)

- Summary: Developed an article recommendation engine using word2vec from Stanford's GloVe project, trained on Wikipedia, and a corpus of BBC text articles.
- Technologies Used: Python, Flask for web server, and PyTest for testing.

# Implementation Details
    - Data Acquisition and Preparation:
    - Downloaded GloVe word vectors and BBC articles.
    - Organized data into a usable format for processing.

    Building the Recommendation System (Part 1):
    - Implemented functions in doc2vec.py to create a database of word vectors and article recommendations.
    - Created articles.pkl and recommended.pkl for storing processed data.

    Web Application Development (Part 2):
    - Developed a Flask web server (server.py) with two main routes:
    - The root route (/) displaying a list of BBC articles.
    - An article route (/article/<topic>/<filename>) for individual articles.

# Functionalities
Processes the each file line-by-line to build a dictionary of word vectors, including all of the unqiue words in the corpus.
Each article represented by a centroid in the vector space and similar articles identified based on the Euclidean distances between these centroids.

# Web Server and User Interface

<img width="234" alt="Screenshot 2023-11-23 at 1 19 13 PM" src="https://github.com/eren-bardak/Word2vec-BBCArticleRecommendation/assets/138029233/e6dd2b2e-e0fe-4ede-ada0-095d8118434c">

- Flask Web Server:
    Built to respond to requests for a list of articles and individual articles.
    Hosted locally for testing purposes.

- User Interface:
    Users can view a list of articles and select one to read the full text.
    Each article page displays the content along with five recommended articles.
  
  <img width="1446" alt="Screenshot 2023-11-23 at 1 18 12 PM" src="https://github.com/eren-bardak/Word2vec-BBCArticleRecommendation/assets/138029233/4c649cab-20ba-4812-8530-e3eae7d88f5f">

- Testing and Validation
    Validated the functionality of doc2vec.py using PyTest (test_doc2vec.py).
    Tested the web server with pytest test_server.py, ensuring it runs correctly and responds as expected.

# Conclusion
- The code succesfully combines NLP techniques with web development to create an article recommendation engine. It demonstrates practical application in processing and recommending content based on text similarity, serving as an effective tool for content discovery.
