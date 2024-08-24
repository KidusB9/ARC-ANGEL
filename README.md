# ARC-ANGEL AI Web Application

## Overview

ARC-ANGEL is a sophisticated Flask web application designed to harness the power of advanced AI and machine learning technologies. The application integrates with cutting-edge libraries such as OpenAI, Google Cloud Vision, and scikit-learn to offer a wide range of functionalities. These include:

- **Object Detection:** Identify and classify objects within images.
- **Sentiment Analysis:** Analyze and determine the sentiment expressed in text.
- **Text Generation:** Create text based on provided prompts.
- **Anomaly Detection:** Detect unusual patterns or outliers in data.
- **Real-time Analytics:** Analyze data in real-time to gain insights.
- **Real-time Recommendation:** Provide recommendations based on user input.

## Endpoints

### Object Detection

**Endpoint:** `POST /object-detection`  
**Description:** Analyzes a base64 encoded image to detect objects.  
**Request:**  
- `frameData` (base64 encoded image)

**Response:**  
- `result` (list of detected objects)

### Sentiment Analysis

**Endpoint:** `POST /sentiment-analysis`  
**Description:** Evaluates the sentiment of a given text.  
**Request:**  
- `text` (text for sentiment analysis)

**Response:**  
- `result` (sentiment analysis result)

### Text Generation

**Endpoint:** `POST /text-generation`  
**Description:** Generates text based on the provided prompt.  
**Request:**  
- `prompt` (text prompt for generation)

**Response:**  
- `result` (generated text)

### Anomaly Detection

**Endpoint:** `POST /anomaly-detection`  
**Description:** Identifies anomalies in the provided data.  
**Request:**  
- `data` (data for anomaly detection)

**Response:**  
- `result` (anomaly detection result)

### Real-time Analytics

**Endpoint:** `POST /realtime-analytics`  
**Description:** Performs real-time analysis on the provided feature matrix.  
**Request:**  
- `feature_matrix` (feature matrix for analytics)

**Response:**  
- `result` (real-time analytics result)

### Real-time Recommendation

**Endpoint:** `POST /realtime-recommendation`  
**Description:** Recommends items based on user input in real-time.  
**Request:**  
- `user_input` (user input for recommendation)

**Response:**  
- `result` (recommended item)

## Additional Components

### Lambda Function

**File:** `lambda.py`  
**Description:** Contains a Lambda function for sentiment analysis using TextBlob.  
**Event:**  
- `text` (text for sentiment analysis)

**Response:**  
- `sentiment` (sentiment analysis result)

### Dockerfile

**Description:** Includes a Dockerfile configured for running unit tests using Poetry.  
**Purpose:** Automates the environment setup for testing the application in a consistent manner.

### Machine Learning Models

- **`generate.py`**: A script that utilizes an LSTM model for generating text.
- **`IterablDataset.py`**: Defines a custom dataset class for IterablDataset, tailored for specific data requirements.
- **`PromptDataset.py`**: Implements a custom dataset class for PromptDataset, designed to handle prompt-based data efficiently.

### Web Interface

**File:** `index.html`  
**Description:** Provides a basic web interface for users to interact with the API, facilitating ease of access and usability.

## Libraries and Frameworks

- **OpenAI**: Used for generating text based on given prompts.
- **Google Cloud Vision**: Utilized for object detection tasks within images.
- **scikit-learn**: Employed for various machine learning tasks, including anomaly detection.
- **Flask**: The core framework for building and managing the web application.
- **Poetry**: Manages dependencies and project setup.
- **Docker**: Facilitates containerization, ensuring consistent environments across different setups.

## Code

The main application code is written in Python and utilizes Flask for endpoint management. Below is a brief overview of the core implementation:

```python
from flask import Flask, request, jsonify
import os
import cv2
import numpy as np
from google.cloud import vision
from sklearn.ensemble import IsolationForest
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Initialize clients
vision_client = vision.ImageAnnotatorClient()

# Define endpoints and logic

@app.route('/object-detection', methods=['POST'])
def object_detection():
    # Endpoint implementation for object detection
    pass

@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    # Endpoint implementation for sentiment analysis
    pass

@app.route('/text-generation', methods=['POST'])
def text_generation():
    # Endpoint implementation for text generation
    pass

@app.route('/anomaly-detection', methods=['POST'])
def anomaly_detection():
    # Endpoint implementation for anomaly detection
    pass

@app.route('/realtime-analytics', methods=['POST'])
def realtime_analytics():
    # Endpoint implementation for real-time analytics
    pass

@app.route('/realtime-recommendation', methods=['POST'])
def realtime_recommendation():
    # Endpoint implementation for real-time recommendation
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0')

## Installation

To set up and run the ARC-ANGEL AI Web Application locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/KidusB9/ARC-ANGEL.git
   cd ARC-ANGEL
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   Ensure that Poetry is installed. Then run:

   ```bash
   poetry install
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory with necessary configurations.

5. **Run the Application:**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://localhost:5000`.

## Usage

Once the application is running, you can interact with it through the API endpoints listed above. For a web-based interface, navigate to `index.html` in your browser.

## Contributing

Contributions are welcome! If you'd like to contribute to ARC-ANGEL, please follow these guidelines:

1. **Fork the Repository:** Click the "Fork" button at the top right of the repository page on GitHub.
2. **Clone Your Fork:** 

   ```bash
   git clone https://github.com/KidusB9/ARC-ANGEL.git
   ```

3. **Create a Branch:** 

   ```bash
   git checkout -b feature/your-feature
   ```

4. **Make Your Changes:** Implement the desired feature or fix.
5. **Commit Your Changes:** 

   ```bash
   git add .
   git commit -m "Add new feature"
   ```

6. **Push to Your Fork:** 

   ```bash
   git push origin feature/your-feature
   ```

7. **Create a Pull Request:** Open a pull request on the original repository and describe your changes.

## Contact

For any questions, issues, or suggestions, please contact:

- **Email:** Kidus@kidusberhanu.com
- **GitHub:** [KidusB9](https://github.com/KidusB9)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the libraries and frameworks used in this project:

- **OpenAI** for text generation capabilities.
- **Google Cloud Vision** for advanced image analysis.
- **scikit-learn** for robust machine learning solutions.
- **Flask** for creating the web application framework.
- **Poetry** for seamless dependency management.
- **Docker** for consistent development environments.

```
