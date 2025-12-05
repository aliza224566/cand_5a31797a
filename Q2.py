def softmax_classify(W, b, X) -> list[int]:
    predictions = []
    for x in X:
        logits = [sum(w * xi for w, xi in zip(Wc, x)) + bc for Wc, bc in zip(W, b)]
        max_val = max(logits)
        # break ties by smallest index
        max_idx = min(i for i, val in enumerate(logits) if val == max_val)
        predictions.append(max_idx)
    return predictions


