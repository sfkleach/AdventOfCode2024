from pathlib import Path


class RuleSet:

    def __init__(self):
        self.rules = set()
    
    def addRule(self, a, b):
        self.rules.add((a, b))

    def is_allowed(self, a, b):
        # print(f"Check: {a} < {b}")
        return (b, a) not in self.rules

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