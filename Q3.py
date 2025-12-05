from collections import Counter

def knn_predict(train_X, train_y, test_X, k) -> list[int]:
    predictions = []
    for test_point in test_X:
        # Compute distances
        dists = [(math.sqrt(sum((tx - trx) ** 2 for tx, trx in zip(test_point, train_point))), label)
                 for train_point, label in zip(train_X, train_y)]
        # Sort by distance, then label
        dists.sort(key=lambda x: (x[0], x[1]))
        # Take k nearest
        nearest_labels = [label for _, label in dists[:k]]
        # Majority vote
        count = Counter(nearest_labels)
        max_votes = max(count.values())
        # Break tie by smallest label
        pred_label = min(label for label, votes in count.items() if votes == max_votes)
        predictions.append(pred_label)
    return predictions

