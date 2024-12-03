# Common code will go here.

class Report:

    def __init__(self, *data):
        self.data = list(*data)

    def is_monotonic(self, dirn):
        for i, j in zip(self.data, self.data[1:]):
            if not 1 <= (dirn * (j - i)) <= 3:
                return False
        return True
    
    def is_increasing(self):
        return self.is_monotonic(1)
    
    def is_decreasing(self):
        return self.is_monotonic(-1)
    
    def is_safe(self):
        return self.is_increasing() or self.is_decreasing()
    
    def child_reports(self):
        for i in range(len(self.data)):
            yield Report(self.data[:i] + self.data[i+1:])

    def has_safe_child(self):
        return any(r.is_safe() for r in self.child_reports())


def read_input(file_path):
    with open(file_path, 'r') as f:
        return [Report(int(w) for w in line.split()) for line in f ]
