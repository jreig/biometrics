# Contents

This project contains information and examples about biometrics. It's goal is to
learn and test different algorithms and how they behave.

- [Biometrics](#biometrics)
    - [Evaluation Metrics](#evaluation-metrics)
    - [Face Detection](#face-detection)
    - [Face Recognition](#face-recognition)

# Biometrics

Identification: Use biometric features extracted from a person to look them up in a BD. Classification problem

Verification: Identify a person with the objective of verifying a second ID method (passwarod, physical card, etc)

## Evaluation metrics

### Identification

**Identification error**: failed identifications / total identifications

**Ranking rate**: probability that the correct id appears in the first *k* most confident identifications

### Validation

**Confusion matrix** (given a verification threshold):
 - Fake positives: Person A verificating as person B and identified as Person B (impostor)
 - Fake negatives: Person A verificating as person A and NOT identified as Person A
 - ROC curve to visualize it

**Detection Error Trade-Off**: Display False Rejection Rate vs False Acceptance Rate. Highlight areas of interest and the critical operating level.


## Face Detection

Can be seen as binary classification. For training require images with faces and images with no faces.

Popular Methods:
 - Multiple methos using deep neural networks. Diferent methods allow for rotations or ilumination changes
 - Schneiderman and Kanade: Bayesian probabilities using face sub-regions (naive Bayes)
 - Viola and Jones: Haar filters. Fast ans simple. Good for scale changes but not rotation.

 Preprocessing of ilumination to make models robust to changes in light

## Face Recognition

Popular methods:
 - Structural representation: Graph representation, nodes are interest points of the face. Uses gabor filters to locate points.
 - Feature based: vector representation. Use PCA (EigenFaces) or LDA (FisherFaces) to reduce dimensionality. PCA+LDA.
 - Local features: Divide face in substructures, local structures are very similar when face rotate, scale, etc. Trained to choose best subestructures and combine them using a probabilistic model.
