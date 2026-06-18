class EmbeddingServer:
    def __init__(self, model="BAAI/bge-large-en-v1.5"): self.model, self.cache = model, {}
    def embed(self, texts):
        for t in texts:
            if t not in self.cache: self.cache[t] = [0.0]*768
        return [self.cache[t] for t in texts]
