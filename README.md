# Chatbot Project

Developed an AI-powered chatbot capable of handling a variety of user queries with high accuracy. The chatbot integrates natural language processing (NLP) techniques and machine learning models to understand and respond to user inputs effectively.

## Files Included

1. **chatbot.py**
2. **training.py**

### 1. chatbot.py

This script handles the core functionalities of the chatbot, including preprocessing user inputs, predicting user intents, and generating appropriate responses.

**Key Features:**
- **Natural Language Processing (NLP):**
  - **Tokenization** and **lemmatization** using `nltk` library.
  - **Bag of Words** model to convert sentences into numerical data.
- **Deep Learning:**
  - Utilizes a pre-trained model loaded using `TensorFlow`'s Keras API (`chatbot_model.h5`).
- **Intent Recognition:**
  - Predicts the intent of the user's query with a defined error threshold.
- **Weather Integration:**
  - Fetches weather data using the OpenWeatherMap API.
- **Billboard Integration:**
  - Accesses Billboard charts data using the `billboard` library.

**Technologies Used:**
- **Python Libraries:**
  - `json`, `random`, `pickle`, `numpy`, `requests`, `billboard`
  - `nltk` for natural language processing.
  - `tensorflow.keras` for loading the pre-trained model.
- **APIs:**
  - OpenWeatherMap API for fetching weather information.

### 2. training.py

This script is responsible for training the chatbot's model. It processes the training data, builds the neural network, and saves the trained model.

**Key Features:**
- **Data Preparation:**
  - Tokenizes and lemmatizes training data.
  - Creates training data arrays for model input and output.
- **Model Training:**
  - Defines a Sequential neural network model using `TensorFlow`'s Keras API.
  - Uses **Stochastic Gradient Descent (SGD)** for optimization.
  - Trains the model with the prepared training data.
  - Saves the trained model as `chatbot_model.h5`.

**Technologies Used:**
- **Python Libraries:**
  - `json`, `pickle`, `numpy`
  - `nltk` for preprocessing text data.
  - `tensorflow.keras` for building and training the neural network.
- **Machine Learning Techniques:**
  - Neural Networks with multiple layers and dropout for regularization.
  - Categorical Crossentropy loss function and SGD optimizer.

---




