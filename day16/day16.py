from typing import Dict, Tuple
from pathlib import Path
import heapq
from collections import defaultdict

def read_input(file_path: Path) -> Tuple[str]:
    with open(file_path, 'r') as file:
        return tuple(file.read().splitlines())

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Trail:

    def __init__(self, position, trail):
        self.position = position
        self.trail = trail
        self.score = (trail.score if trail else 0) + self.delta_score()

    def dirn(self):
        if self.trail:
            x0, y0 = self.position
            x1, y1 = self.trail.position
            return (x0 - x1, y0 - y1)
        else:
            return None

    def __lt__(self, other): 
        return self.score < other.score

    def delta_score(self):
        if self.trail and self.trail.trail:
            x0, y0 = self.position
            x2, y2 = self.trail.trail.position
            d1 = abs(x0 - x2) == 0
            d2 = abs(y0 - y2) == 0
            if d1 and not d2 or d2 and not d1:
                return 1
            else:
                return 1001
        else:
            return 1
        
    def print(self):
        t = self
        while t:
            # print(f'POSITION {t.position}, Score {t.score}')
            t = t.trail

    def positions(self):
        t = self
        while t:
            yield t.position
            t = t.trail

    def posdirns(self):
        t = self
        while t:
            yield (t.position, t.dirn())
            t = t.trail

    def does_not_include(self, position):
        t = self
        while t:
            if t.position == position:
                return False
            t = t.trail
        return True

class Maze:

    def __init__(self, data):
        self.data = tuple(data)
        self.start = None
        self.end = None
        for x, row in enumerate(self.data):
            for y, cell in enumerate(row):
                if cell == 'S':
                    self.start = (x, y)
                elif cell == 'E':
                    self.end = (x, y)
        self.trails = {}
        self.alternatives = defaultdict(list)

    def get(self, x, y):
        return self.data[x][y] != '#'
    
    def __str__(self):
        return '\n'.join(self.data)
    
    def solve(self):
        prestart = Trail((self.start[0], self.start[1]-1), None)
        queue = []
        heapq.heappush(queue, Trail(self.start, prestart))
        while queue:
            t = heapq.heappop(queue)
            # print('Position', t.position, 'Score', t.score)
            tpos = t.position
            tx, ty = tpos
            tdirn = t.dirn()
            tposdirn = (tpos, tdirn)
            if tposdirn in self.trails and t.score >= self.trails[tposdirn].score:
                if t.score == self.trails[tposdirn].score:
                    self.alternatives[tposdirn].append(t)
                continue
            self.trails[tposdirn] = t
            self.alternatives[tposdirn] = []
            if tpos == self.end:
                # print('Found solution')
                continue
            for d in DIRECTIONS:
                x, y = tx + d[0], ty + d[1]
                if self.get(x, y) and t.does_not_include((x,y)):
                    u = Trail((x,y), t)
                    heapq.heappush(queue, u)
        return self.find_one_best()
    
    def reached_end(self):
        for d in DIRECTIONS:
            posdirn = (self.end, d)
            if posdirn in self.trails:
                yield self.trails[posdirn]
    
    def find_best_score(self):
        best_score = None
        for t in self.reached_end():
            candidate_score = t.score
            if best_score is None or candidate_score < best_score:
                best_score = candidate_score
        return best_score

    def find_best(self):
        best_score = self.find_best_score()
        for t in self.reached_end():
            if t.score == best_score:
                yield t

    def find_one_best(self):
        for t in self.find_best():
            return t

    def show_best_seats(self):
        seen = set()
        queue = list(self.find_best())
        data = list(map(list, self.data))
        while queue:
            t = queue.pop()
            if t not in seen:
                seen.add(t)
                for posdirn in t.posdirns():
                    queue.extend(self.alternatives[posdirn])
        positions = set()
        for t in seen:
            for pos in t.positions():
                positions.add(pos)
        for x, y in positions:
            data[x][y] = 'O'
        print(f'Best seats: {len(positions)-1}')
        # print('\n'.join(''.join(row) for row in data))
        
            

    def show(self, trail: Trail):
        data = list(map(list, self.data))
        while trail:
            x, y = trail.position
            data[x][y] = '*'
            trail = trail.trail
        print('\n'.join(''.join(row) for row in data))

