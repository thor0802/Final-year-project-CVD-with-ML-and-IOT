# Final-year-project-CVD-with-ML-and-IOT
Cardiovascular Disease Diagnosis Using Machine Learning and IoT

Overview

This project aims to predict cardiovascular diseases using Machine Learning (ML) techniques and IoT data. By leveraging ML models and advanced feature selection, the system enhances prediction accuracy and provides insights for early detection and intervention.

Features

Data preprocessing to clean and standardize input data

Feature selection and dimensionality reduction

Machine learning classification models for prediction

Integration with IoT-enabled health monitoring devices

Performance evaluation with accuracy metrics

Technologies Used

Programming Language: Python 3.6+

Machine Learning Libraries: Scikit-learn, TensorFlow, Keras

Data Processing: Pandas, NumPy

Visualization: Matplotlib, Seaborn

Hardware Requirements: Intel i5 processor, 4GB RAM, 120GB HDD

Software Requirements: Windows 11, Python IDLE

Installation

Clone the repository:

git clone <repository-url>

Navigate to the project directory:

cd project-directory

Install required dependencies:

pip install -r requirements.txt

Usage

Prepare and preprocess the dataset:

python preprocess.py

Train the ML model:

python train.py

Test and evaluate the model:

python evaluate.py

Deploy the model for real-time predictions:

python app.py

System Workflow

Data Collection: Acquires patient physiological data (heart rate, BP, ECG, etc.) from IoT devices.

Preprocessing: Cleans and normalizes data for consistency.

Feature Selection: Identifies significant features for prediction.

Model Training: Trains ML models using classification techniques like Random Forest and Neural Networks.

Prediction & Evaluation: Classifies the risk level of cardiovascular disease.

Deployment: Provides real-time predictions through an integrated system.

Results & Performance

Achieved 90.7% accuracy using a hybrid Random Forest model.

Compared multiple classification techniques for optimal performance.

Future Enhancements

Expand dataset to improve generalization.

Implement real-time health monitoring via IoT integration.

Enhance deep learning techniques for higher accuracy.

Contributors

Imran Hussain (1ME20CS026)

Nishant Sinha (1ME20CS028)

Shadikul Islam (1ME20CS037)

Shivam Yadav (1ME20CS039)

License

This project is licensed under the MIT License.
