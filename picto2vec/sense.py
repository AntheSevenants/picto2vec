class Sense:
    def __init__(self, name, data):
        self.name = name
        # Filter all where key = None
        self.data = { key: value for (key, value) in data.items() if not value is None }
        
    def total_representation_count(self):
        return len(self.data.keys())
    
    def get_representations(self, layer_index):       
        representations = []
        for key in list(self.data.keys())[:30]:
            representations.append(self.data[key][layer_index])
            
        return np.array(representations)
    
    def get_distances(self, representations):
        return pairwise_distances(representations, metric="cosine")

    def get_medoid_indices(self, representations, medoid_clusters):
        distance_matrix = self.get_distances(representations)
        medoids = KMedoids(medoid_clusters, metric="precomputed", method="pam").fit(distance_matrix)
        
        return list(medoids.medoid_indices_)