# Grokking Algorithms
# Chapter 10 - K-Nearest Neighbors

# K-Nearest Neighbors (KNN) is a simple algorithm that stores all available cases and classifies new cases based on a similarity measure. It is mostly used for classification and regression problems.

# KNN works as follows:
# 1. Calculate the distance between the new case and all the available cases.
# 2. Sort the cases by distance.
# 3. Select the top K cases.
# 4. Find the most frequent class among these cases.
# 5. Return the most frequent class as the prediction for the new case.

# KNN is a lazy learner because it doesn't learn a discriminative function from the training data but memorizes the training dataset instead.
# A lazy learner delays the induction or generalization process until a new instance must be classified.

# Exercise
# 10.1 
# 1. Normalize the data (each users rating) using z-score normalization/min-max scaling.
# Z-score normalization: (x - mean) / standard deviation (measures standard de from the mean)
# Min-max scaling: (x - min) / (max - min) (scales the data between 0 and 1)
# 2. Weighted KNN: Instead of taking the majority vote, take the weighted vote of the neighbors, where the weight is the inverse of the distance.
# Formula 'rating_normalized = (rating - min_rating) / (max_rating - min_rating)' -- ensures users who are generious or stingy with ratings are adjusted to common scale.

# 10.2
# 1. Weighted rankings --> give influencers a higher weight, or change aggregate scores of influencers to a different scale.
# 2. Modify Influence Dynamically --> change the influence of a user based on the user's behavior.

# Example of weighted ratings using Euclidean distance and weights
# Euclidean distance is a measure of the true straight line distance between two points in Euclidean space. It's the most common use of distance in many machine learning algorithms, especially in clustering and classification processes.
# Euclidean distance: sqrt((x1 - x2)^2 + (y1 - y2)^2)
# Weighted Euclidean distance: sqrt(w1 * (x1 - x2)^2 + w2 * (y1 - y2)^2)
# Example: Yogi and Pinky are two users who have rated movies. Quentin Tarantino and Wes Anderson are influencers who have a higher weight in the ratings.

from cmath import sqrt
ratings_yogi = {'Quentin Tarantino': 5, 'Wes Anderson': 4, 'regular_user': 3}
ratings_pinky = {'Quentin Tarantino': 4, 'Wes Anderson': 5, 'regular_user': 2}

def weighted_euclidean_distance(user1, user2, weights):
    sum_squared_distance = 0
    for key in user1:
        if key in user2:
            # Applying a weight if the user is an influencer
            weight = weights.get(key, 1)
            sum_squared_distance += weight * (user1[key] - user2[key]) ** 2
    return sqrt(sum_squared_distance)

# Example weights dictionary where influencers have higher weights
weights = {'Quentin Tarantino': 3, 'Wes Anderson': 3, 'regular_user': 1}

# Using the function in a KNN-like algorithm
distance = weighted_euclidean_distance(ratings_yogi, ratings_pinky, weights)

# cosine similarity
# Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. It is a judgment of orientation and not magnitude.

# When working with KNN, picking the right distance metric is important. Euclidean distance is the most common choice, but other metrics like cosine similarity can be used as well.
# Features need to directly correlate, and can't have bias. Cosine similarity is used when the magnitude of the vectors doesn't matter, only the direction.

# Excercise
# 10.3 Netflix has millions of users. Is Five closest neighbors enough? What are the trade-offs of increasing the number of neighbors?
# 1. More neighbors can lead to a more accurate prediction, but it also increases the computational complexity.
# 2. The choice of K depends on the dataset and the problem at hand. A small K can lead to overfitting, while a large K can lead to underfitting.
# 3. The curse of dimensionality can also affect the choice of K. As the number of dimensions increases, the distance between points becomes less meaningful.
# 4. The choice of K can be determined using cross-validation or other model selection techniques.

# Recap 
# KNN is used for classification and regression problems and involves looking at the K closest neighbors to make a prediction.
# Classification = categorization into a group. 
# Regression = predicting a response (like a number). 
# Feature extraction means converting an item into a list of numbers that can be compared.
# Picking good features is important for KNN.

