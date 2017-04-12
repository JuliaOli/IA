class Node:

    speed = 30

    def __init__(self, parent, cost, action, position):

        self.parent = parent
        self.cost = cost
        self.action = action
        self.position = position

    def final(self, end):
        return self.position == end

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost
