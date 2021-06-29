

class SentencesGenerate:
    def __init__(self, path, min_length):
        self.y = []
        self.X = []
        self.vocab = set()
        self.labels = set()
        self._path = path
        self._min_length = min_length

        self.generate()
    
    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        X = self.X[index]
        y = self.y[index]
        return (X, y, len(X))

    def generate(self):
        sent, tags = [], []
        with open(self._path, 'r') as data:
            for line in data:
                if line != '\n':
                    token, tag = line.replace('\n', '').split(' ')
                    sent.append(token)
                    tags.append(tag)
                    self.labels.add(tag)
                    self.vocab.add(token)
                
                else:
                    assert len(sent) == len(tags)
                    if self._min_length < len(sent):
                        self.X.append(sent)
                        self.y.append(tags)
                    sent, tags = [], []
