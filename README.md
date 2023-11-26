# Article Recommendation Using Word2vec (From the course MSDS692 - Data Acquisiton @USF)

- Summary: Developed an article recommendation model using word2vec from Stanford's GloVe project, trained on Wikipedia, and a corpus of BBC text articles.
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
Processes the each file line-by-line to build a dictionary of word vectors.
Each article represented by a centroid in the vector space.
Similar articles identified based on the closeness of these centroids.

# Web Server and User Interface

<img width="226" alt="Screenshot 2023-11-23 at 1 19 50 PM" src="https://github.com/eren-bardak/BBCArticleRecommendation/assets/138029233/6ced7d16-13d1-4180-af43-40b63c9f341a">

- Flask Web Server:
    Built to respond to requests for a list of articles and individual articles.
    Hosted locally for testing purposes.

- User Interface:
    Users can view a list of articles and select one to read the full text.
    Each article page displays the content along with five recommended articles.
  
<img width="1438" alt="Screenshot 2023-11-23 at 1 20 36 PM" src="https://github.com/eren-bardak/BBCArticleRecommendation/assets/138029233/c3aa261a-3bd6-429b-b131-0af11454c434">

- Testing and Validation
    Validated the functionality of doc2vec.py using PyTest (test_doc2vec.py).
    Tested the web server with pytest test_server.py, ensuring it runs correctly and responds as expected.

# Conclusion
- The code succesfully combines NLP techniques with web development to create an article recommendation engine. It demonstrates practical application in processing and recommending content based on text similarity, serving as an effective tool for content discovery.
