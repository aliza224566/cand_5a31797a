import math

def top_k_cosine(query, docs, k):
    def cosine(q, d):
        dot = sum(q[i] * d[i] for i in range(len(q)))
        nq = math.sqrt(sum(val * val for val in q))
        nd = math.sqrt(sum(val * val for val in d))
        if nq == 0 or nd == 0:
            return 0
        return dot / (nq * nd)

    sims = []
    for i, d in enumerate(docs):
        sims.append((cosine(query, d), i))

    sims.sort(key=lambda x: (-x[0], x[1]))
    return [idx for _, idx in sims[:k]]
