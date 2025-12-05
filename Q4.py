def top_k_cosine(query, docs, k) -> list[int]:
    def cosine(q, d):
        q_norm = math.sqrt(sum(qi**2 for qi in q))
        d_norm = math.sqrt(sum(di**2 for di in d))
        if q_norm == 0 or d_norm == 0:
            return 0
        return sum(qi*di for qi, di in zip(q, d)) / (q_norm * d_norm)
    
    sims = [(cosine(query, doc), idx) for idx, doc in enumerate(docs)]
    # Sort by similarity descending, then index ascending
    sims.sort(key=lambda x: (-x[0], x[1]))
    return [idx for _, idx in sims[:k]]

