# vim: sw=4:ts=4:et:ai
"""

Approach:
 Use Edsger Dijkstra's algorithm to find the path with the highest score.

"""
import heapq

pyramid = (
 (75,),
 (95, 64),
 (17, 47, 82),
 (18, 35, 87, 10),
 (20,  4, 82, 47, 65),
 (19,  1, 23, 75,  3, 34),
 (88,  2, 77, 73,  7, 63, 67),
 (99, 65,  4, 28,  6, 16, 70, 92),
 (41, 41, 26, 56, 83, 40, 80, 70, 33),
 (41, 48, 72, 33, 47, 32, 37, 16, 94, 29),
 (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14),
 (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57),
 (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48),
 (63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31),
 ( 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23))


class PriorityDict(dict):
    """Dictionary that can be used as a priority queue.

    Keys of the dictionary are items to be put into the queue, and values
    are their respective priorities. All dictionary methods work as expected.
    The advantage over a standard heapq-based priority queue is
    that priorities of items can be efficiently updated (amortized O(1))
    using code as 'thedict[item] = new_priority.'

    The 'smallest' method can be used to return the object with lowest
    priority, and 'pop_smallest' also removes it.

    The 'sorted_iter' method provides a destructive sorted iterator.
    """
    
    def __init__(self, *args, **kwargs):
        super(PriorityDict, self).__init__(*args, **kwargs)
        self._rebuild_heap()

    def _rebuild_heap(self):
        self._heap = [(v, k) for k, v in self.iteritems()]
        heapq.heapify(self._heap)

    def smallest(self):
        """Return the item with the lowest priority.

        Raises IndexError if the object is empty.
        """
        heap = self._heap
        v, k = heap[0]
        while k not in self or self[k] != v:
            heapq.heappop(heap)
            v, k = heap[0]
        return k

    def pop_smallest(self):
        """Return the item with the lowest priority and remove it.

        Raises IndexError if the object is empty.
        """
        heap = self._heap
        v, k = heapq.heappop(heap)
        while k not in self or self[k] != v:
            v, k = heapq.heappop(heap)
        del self[k]
        return k

    def __setitem__(self, key, val):
        # We are not going to remove the previous value from the heap,
        # since this would have a cost O(n).
        super(PriorityDict, self).__setitem__(key, val)
        if len(self._heap) < 2 * len(self):
            heapq.heappush(self._heap, (val, key))
        else:
            # When the heap grows larger than 2 * len(self), we rebuild it
            # from scratch to avoid wasting too much memory.
            self._rebuild_heap()

    def setdefault(self, key, val):
        if key not in self:
            self[key] = val
            return val
        return self[key]

    def update(self, *args, **kwargs):
        # Reimplementing dict.update is tricky -- see e.g.
        # http://mail.python.org/pipermail/python-ideas/2007-May/000744.html
        # We just rebuild the heap from scratch after passing to super.
        super(PriorityDict, self).update(*args, **kwargs)
        self._rebuild_heap()

    def sorted_iter(self):
        """Sorted iterator of the priority dictionary items.

        Beware: this will destroy elements as they are returned.
        """
        while self:
            yield self.pop_smallest()


class PyramidClass(object):
    """ Class that implements A* methods for the pyramid problem """
    pyramid = None

    @classmethod
    def neighbor_nodes(cls, node):
        """
        Return a generator for the nodes that can be accessed from this node.
        """
        row = node[0] + 1
        left_bound = node[1]
        right_bound = node[1] + 1
        return ((row, col) for col in range(left_bound, right_bound + 1))

    @classmethod
    def heuristic_cost_estimate_to_goal(cls, node):
        """
        Provide an estimation of the distance to the goal node,
        by returning 0, we effectively perform Dijkstra instead of A*.
        """
        return 0 

    @classmethod
    def is_goal_node(cls, node):
        """
        A node is a goal node if the node is on the last row of the pyramid.
        """
        return node[0] == len(cls.pyramid) - 1

    @classmethod
    def dist_between(cls, node, other_node):
        """ distance between two neighbouring nodes """
        row = other_node[0]
        col = other_node[1]
        return (100 - cls.pyramid[row][col])


def a_star(start, cls):
    """
    A* search algorithm, widely used for path finding and graph traversal.

    Sources:
    http://en.wikipedia.org/wiki/A*_search_algorithm
    """
    def reconstruct_path(came_from, current_node):
        if came_from.has_key(current_node):
            p = reconstruct_path(came_from, came_from[current_node])
            p.append(current_node)
            return p
        else:
            return [current_node]

    infinity = 9999999999

    # The set of nodes already evaluated.
    visited = []

    # The set of tentative nodes to be evaluated, initially containing the start node
    openset = PriorityDict()

    # The map of navigated/visited nodes.
    came_from = {} 

    # Maps for scores
    g_score = {}
    h_score = {}
    f_score = {}
 
    # Cost from start along best known path.
    g_score[start] = 0
    # Heuristic cost from start to goal
    h_score[start] = cls.heuristic_cost_estimate_to_goal(start)
    # Estimated total cost from start to goal through y.
    f_score[start] = g_score[start] + h_score[start]    

    openset[start] = f_score[start]

    while len(openset) > 0:
        x = openset.pop_smallest()

        print("Examining %ix%i" % x)
        if cls.is_goal_node(x):
            return (reconstruct_path(came_from, x), visited, openset)

        visited.append(x)

        for y in cls.neighbor_nodes(x):
            if y in visited:
                continue

            tentative_g_score = g_score[x] + cls.dist_between(x, y)

            if y not in openset:
                openset[y] = infinity
                tentative_is_better = True
            elif y in g_score and tentative_g_score < g_score[y]:
                tentative_is_better = True
            else:
                tentative_is_better = False

            if tentative_is_better:
                came_from[y] = x
                g_score[y] = tentative_g_score
                h_score[y] = cls.heuristic_cost_estimate_to_goal(y)
                f_score[y] = g_score[y] + h_score[y]
                if y in openset:
                    openset[y] = f_score[y]

    return False
 

def display_pyramid(pyramid, path, visited, openset):
    """ Graphically display the pyramid, showing the path chosen """
    import sys
    from colorama import init as colorama_init, Style, Fore
    colorama_init()
    isatty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    max_line_width = (len(pyramid[-1]) * 3) - 1
    for row_num, row in enumerate(pyramid):
        line = []
        for col_num, col in enumerate(row):
            value = pyramid[row_num][col_num]
            if (row_num, col_num) in path:
                line.append('%s%s%02i%s' % (Style.BRIGHT, Fore.GREEN, value, Style.RESET_ALL))
            elif (row_num, col_num) in visited:
                line.append('%s%s%02i%s' % (Style.NORMAL, Fore.RED, value, Style.RESET_ALL))
            elif (row_num, col_num) in openset:
                line.append('%s%s%02i%s' % (Style.BRIGHT, Fore.RED, value, Style.RESET_ALL))
            else:
                line.append('%s%02i%s' % (Style.DIM, value, Style.RESET_ALL))
        line_width = (len(line) * 3) - 1
        space_width = (max_line_width - (line_width // 2))
        line.insert(0, ' ' * space_width)
        print(' '.join(line))
    print('')


def main(debug=False):
    global pyramid
    start = (0, 0)
    cls = PyramidClass
    cls.pyramid = pyramid
    path, visited, openset = a_star(start, cls)
    if debug:
        display_pyramid(pyramid, path, visited, openset)
    return sum(pyramid[row][col] for row, col in path)


if __name__ == '__main__':
    print("Result: %i" % main(True))

