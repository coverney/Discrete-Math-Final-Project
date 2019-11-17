class Reporter(object):
    def __init__(self, name):
        self.name = name
        self.cnt = 0
        self.cliques = []

    def inc_count(self):
        self.cnt += 1

    def record(self, clique):
        self.cliques.append(clique)

    def sort_cliques(self):
        self.cliques.sort(key=len, reverse=True)

    def print_max(self, n):
        # print the n largest cliques
        self.sort_cliques()
        print(self.name)
        print('%d recursive calls' % self.cnt)
        for i in range(n):
            clique = self.cliques[i]
            print('%d: %s' % (i, clique))
        print()

    def print_report(self):
        print(self.name)
        print('%d recursive calls' % self.cnt)
        for i, clique in enumerate(self.cliques):
            print('%d: %s' % (i, clique))
        print()
