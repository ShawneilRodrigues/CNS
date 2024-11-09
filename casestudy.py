import random
import numpy as np

class CLARANS:
    def __init__(self, data, k, num_local_min, max_neighbors):
        self.data = data
        self.k = k
        self.num_local_min = num_local_min
        self.max_neighbors = max_neighbors
        self.medoids = []
        self.clusters = []

    def fit(self):
        for _ in range(self.num_local_min):
            current_medoids = random.sample(range(len(self.data)), self.k)
            current_cost = self.calculate_cost(current_medoids)
            neighbor_count = 0
            
            while neighbor_count < self.max_neighbors:
                new_medoids = self.get_neighbor(current_medoids)
                new_cost = self.calculate_cost(new_medoids)
                
                if new_cost < current_cost:
                    current_medoids = new_medoids
                    current_cost = new_cost
                    neighbor_count = 0
                else:
                    neighbor_count += 1
            
            if not self.medoids or current_cost < self.calculate_cost(self.medoids):
                self.medoids = current_medoids
        
        self.assign_clusters(self.medoids)

    def calculate_cost(self, medoids):
        cost = 0
        for idx, point in enumerate(self.data):
            closest_medoid_distance = min(np.linalg.norm(point - self.data[medoid]) for medoid in medoids)
            cost += closest_medoid_distance ** 2
        return cost

    def get_neighbor(self, medoids):
        new_medoids = medoids[:]
        non_medoids = list(set(range(len(self.data))) - set(medoids))
        swap_out_index = random.choice(range(len(medoids)))
        swap_in_index = random.choice(non_medoids)
        
        new_medoids[swap_out_index] = swap_in_index
        return new_medoids

    def assign_clusters(self, medoids):
        self.clusters = [[] for _ in range(self.k)]
        for idx, point in enumerate(self.data):
            closest_medoid_index = np.argmin([np.linalg.norm(point - self.data[medoid]) for medoid in medoids])
            self.clusters[closest_medoid_index].append(point)

if __name__ == "__main__":
    data_points = np.array([[1, 2], [1, 4], [1, 0],
                            [10, 2], [10, 4], [10, 0]])

    k_clusters = 2          
    num_local_minima = 5   
    max_neighbors = 10      

    clarans_model = CLARANS(data_points, k_clusters, num_local_minima, max_neighbors)
    clarans_model.fit()

    print("Final Medoids:", clarans_model.medoids)
    print("Clusters:")
    for i, cluster in enumerate(clarans_model.clusters):
        print(f"Cluster {i}: {cluster}")
