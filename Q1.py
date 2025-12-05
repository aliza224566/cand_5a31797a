import math

def kmeans_assign(points, centroids) -> list[int]:
    assignments = []
    for p in points:
        min_dist = float('inf')
        assigned_idx = 0
        for i, c in enumerate(centroids):
            # Euclidean distance
            dist = math.sqrt(sum((px - cx) ** 2 for px, cx in zip(p, c)))
            if dist < min_dist or (dist == min_dist and i < assigned_idx):
                min_dist = dist
                assigned_idx = i
        assignments.append(assigned_idx)
    return assignments


