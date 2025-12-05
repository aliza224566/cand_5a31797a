def softmax_classify(W, b, X):
    C = len(W)
    preds = []

    for x in X:
        logits = []
        for c in range(C):
            logit = sum(W[c][j] * x[j] for j in range(len(x))) + b[c]
            logits.append(logit)

        best = max(range(C), key=lambda c: (logits[c], -c))
        preds.append(best)

    return preds
