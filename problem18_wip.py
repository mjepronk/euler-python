# vim: sw=4:ts=4:et:ai

import heapq

pyramid =
((75),
 (95, 64),
 (17, 47, 82),
 (18, 35, 87, 10),
 (20, 04, 82, 47, 65),
 (19, 01, 23, 75, 03, 34),
 (88, 02, 77, 73, 07, 63, 67),
 (99, 65, 04, 28, 06, 16, 70, 92),
 (41, 41, 26, 56, 83, 40, 80, 70, 33),
 (41, 48, 72, 33, 47, 32, 37, 16, 94, 29),
 (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14),
 (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57),
 (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48),
 (63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31),
 (04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 04, 23))


class Node(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __cmp__(self, other):
        pass

    def neighbor_nodes(self):
        pass

    def heuristic_cost_estimate(self, to_node):
        pass

    def dist_between(self, other):
        pass

class PyramidNone(Node):
    pass



def a_star(start, goal):
    """
    A* search algorithm, widely used for path finding and graph traversal.

    Sources:
    http://en.wikipedia.org/wiki/A*_search_algorithm
    """
    def reconstruct_path(came_from, current_node):
        if came_from.has_key(current_node):
            p = reconstruct_path(came_from, came_from[current_node])
            return (p + current_node)
        else
            return current_node

    # The set of nodes already evaluated.
    closedset = []

    # The set of tentative nodes to be evaluated, initially containing the start node
    openset = [start]
    heapq.heapify(openset)

    # The map of navigated/visited nodes.
    came_from = {} 

    # Maps for scores
    g_score = h_score = f_score = {}
 
    # Cost from start along best known path.
    g_score[start] := 0
    # Heuristic cost from start to goal
    h_score[start] := start.heuristic_cost_estimate(goal)
    # Estimated total cost from start to goal through y.
    f_score[start] := g_score[start] + h_score[start]    

    while len(openset) > 0:
        # Pop the node in openset having the lowest f_score[] value
        x = heapq.heappop(openset)

        if x == goal:
            return reconstruct_path(came_from, came_from[goal])

        closedset.append(x)

        for y in x.neighbor_nodes():
            if y in closedset:
                continue

            tentative_g_score := g_score[x] + x.dist_between(y)

            if y not in openset:
                heapq.heappush(openset, y)
                tentative_is_better = True
            elif tentative_g_score < g_score[y]
                tentative_is_better = True
            else
                tentative_is_better = False

            if tentative_is_better:
                came_from[y] = x
                g_score[y] = tentative_g_score
                h_score[y] = y.heuristic_cost_estimate(goal)
                f_score[y] = g_score[y] + h_score[y]

    return False
 
