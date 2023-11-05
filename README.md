# Problem-Statement-3
Problem Statement:
Predict whether an object is a star or not, and if it is a star, classify its type, using a CSV file obtained from Sloan Digital Sky Survey (SDSS) photometric data,

Objective:
To develop a machine learning model that can accurately predict whether an object is a star or not, and if it is a star, classify its type, using only its photometric data

Input:
A CSV file containing the spectra of objects, along with their labels (star or not).

Output:
A prediction for each object in the 80:20 split input file, indicating whether it is a star or not, and if it is a star, its type. (Split the given dataset and use 80% of it for training and 20% of it for testing)

Constraints:
The model must be able to generalize to new data, meaning that it should be able to predict the type of a star accurately even if it has not seen the spectrum of that star before

Potential Applications:
This model could be used to help astronomers identify stars in large datasets of astronomical images.
It could also be used to study the evolution of stars by tracking their type over time.
Link to the dataset: https://github.com/DespCAP/APV_2023/raw/main/star_classification.csv 
