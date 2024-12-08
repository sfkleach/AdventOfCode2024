from functools import cmp_to_key
from pathlib import Path
from collections import defaultdict


class RuleSet:

    def __init__(self):
        self.rules = set()
        self.dict = None
    
    def addRule(self, a, b):
        self.rules.add((a, b))

    def is_allowed(self, a, b):
        # print(f"Check: {a} < {b}")
        return (b, a) not in self.rules

    def compile_dict(self):
        self.dict = defaultdict(list)
        for rule in self.rules:
            (a, b) = rule
            self.dict[a].append(b)

    def next(self, a):
        if self.dict is None:
            self.compile_dict()
        return self.dict[a]

    def is_path(self, a, b):
        if a == b:
            return True
        else:
            for x in self.next(a):
                # print(f"Checking: {x} -> {b}")
                if self.is_path(x, b):
                    return True
            return False
    
    def cmp(self, a, b):
        if self.is_path(a, b):
            return -1
        elif self.is_path(b, a):
            return 1
        else:
            return 0
        
    def filter(self, pages):
        new_rules = RuleSet()
        p = set(pages)
        for a, b in self.rules:
            if a in p and b in p:
                new_rules.addRule(a, b)
        return new_rules

class PageList:

    def __init__(self, pages):
        self.pages = tuple(pages)

    def is_ordered(self, rules):
        for i in range(0, len(self.pages)):
            for j in range(i+1, len(self.pages)):
                if not rules.is_allowed(self.pages[i], self.pages[j]):
                    print(f"Violates rule: {self.pages[i]} < {self.pages[j]}")
                    return False
        return True
    
    def middle(self):
        return self.pages[len(self.pages)//2]
    
    def sorted(self, rules: RuleSet):
        return sorted(self.pages, key=cmp_to_key(rules.cmp))
    
def parseInput(inputPath: Path):
    with inputPath.open('r') as file:
        rules = RuleSet()
        for line in file:
            if '\n' == line:
                break
            rules.addRule(*map(int, line.strip().split('|')))
        pagelist_collection = []
        for line in file:
            pagelist = PageList(map(int, line.split(',')))
            pagelist_collection.append(pagelist)
        return rules, pagelist_collection 