import math

def knn_predict(train_X, train_y, test_X, k):

    def dist(a, b):
        return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))

    preds = []

    for x in test_X:
        dlist = []
        for tx, lbl in zip(train_X, train_y):
            dlist.append((dist(x, tx), lbl))

        dlist.sort(key=lambda t: (t[0], t[1]))

        kn = dlist[:k]

        freq = {}
        for _, lbl in kn:
            freq[lbl] = freq.get(lbl, 0) + 1

        best_label = max(freq.keys(), key=lambda lbl: (freq[lbl], -lbl))
        preds.append(best_label)

    return preds
