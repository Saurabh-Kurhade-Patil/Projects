📩 SMS Spam Classifier

This project is a Machine Learning based SMS Spam Detection system that classifies messages as Spam or Not Spam (Ham). The model was trained after performing Exploratory Data Analysis (EDA) and Feature Engineering on the dataset.

🚀 Project Workflow

1️⃣ Exploratory Data Analysis (EDA)

Analyzed message distribution

Checked class imbalance

Visualized message length and word patterns

2️⃣ Feature Engineering

Text preprocessing (tokenization, stopword removal, stemming)

TF-IDF vectorization

Created additional features like word count

3️⃣ Model Building

Trained multiple ML models for spam detection

Achieved ~97% accuracy

⚠️ Since the dataset is imbalanced, the focus was on Precision Score to reduce false spam predictions rather than relying only on accuracy.

🌐 Live Demo

Try the deployed application here:

🔗 https://ds-projects-d7awsheyjaf9sfg33hsie2.streamlit.app/

The web app is built using Streamlit.

📊 Dataset

The dataset used for this project is the SMS Spam Collection Dataset from Kaggle.

🔗 https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset/data

🛠 Tech Stack

Python 🐍

Pandas & NumPy

scikit-learn

NLTK

Streamlit

🎯 Goal

To build a practical end-to-end Machine Learning application that demonstrates:

Data analysis

Feature engineering

Model training

Web deployment

⭐ If you found this project helpful, feel free to star the repository.
