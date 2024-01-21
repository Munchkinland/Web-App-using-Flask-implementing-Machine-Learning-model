#ML Deployment with Flask
This project demonstrates the deployment of a machine learning model using Flask. The model is trained to predict the class of an Iris flower based on its sepal and petal dimensions.

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Make sure you have the following installed:

Python (3.7 or higher)
Flask
scikit-learn
Pandas
Numpy
Install the required libraries using:


pip install -r requirements.txt
Running the Application
Run the Flask app:

python app.py
Open your web browser and go to http://127.0.0.1:5000/

Enter the sepal and petal dimensions for prediction.

Click the "Predict" button.

app.py: This is the main file of the Flask application. It contains the configuration and routes for handling HTTP requests. Here, routes (/ and /predict) are associated with specific functions that render HTML templates and handle model predictions.

templates: This directory contains HTML templates used to render the web pages of the application. In this case, there's only one template called index.html, which displays the input form and prediction results.

static/css/style.css: This CSS file defines styles for the appearance of the user interface. It contains style rules for buttons, the layout of elements, and the overall look of the page. It's important to have this file in a folder named static so that Flask can find and serve it as a static asset.

model.pkl: This is the pre-trained machine learning model. In the train_model.py script, the Iris dataset is used to train a logistic regression model, and the resulting model is saved to this file. In app.py, this model is loaded and used to make predictions based on user-provided data through the web form.

train_model.py: This script is responsible for loading the Iris dataset, training a logistic regression model, and saving the trained model to the model.pkl file. This file is run once to train and save the model.

requirements.txt: This file contains a list of Python libraries and their specific versions required to run the application. You can generate this file using the pip freeze > requirements.txt command after installing the necessary dependencies.

The application follows a basic flow:

The user enters data into the form on the main page (/).
Data is sent to the server when the "Predict" button is clicked.
The server uses the loaded model (model.pkl) to make a prediction based on the provided data.
The prediction is displayed to the user on the same page.
In summary, app.py acts as the main controller, HTML templates in the templates directory define the user interface, the CSS file (style.css) controls the visual style, and model.pkl contains the trained model for making predictions.

#Project structure.

📁 project-root
|
|-- 📄 app.py                 # Main Flask application file
|
|-- 📁 templates              # HTML templates for rendering web pages
|   |-- 📄 index.html         # Main page template with input form and results
|
|-- 📁 static                 # Static assets (e.g., CSS, JS)
|   |-- 📁 css                # Stylesheets
|       |-- 📄 style.css      # Styles for the user interface
|
|-- 📄 model.pkl              # Pre-trained machine learning model
|
|-- 📄 train_model.py         # Script for training and saving the machine learning model
|
|-- 📄 requirements.txt       # List of required Python libraries and versions