# vim: sw=4:ts=4:et:ai

import heapq

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
        self._heap = [(v, k) for k, v in self.items()]
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


class AStarAlgorithm(object):
    def __init__(self):
        # The set of tentative nodes to be evaluated, initially containing the start node
        self.openset = PriorityDict()
        # The set of nodes already evaluated.
        self.visited = []

    def a_star(self, start):
        """
        A* search algorithm, widely used for path finding and graph traversal.

        Sources:
        http://en.wikipedia.org/wiki/A*_search_algorithm
        """
        # The map of navigated/visited nodes.
        came_from = {} 

        # Maps for scores
        g_score = {}
        h_score = {}
        f_score = {}
     
        # Cost from start along best known path.
        g_score[start] = 0
        # Heuristic cost from start to goal
        h_score[start] = self.heuristic_cost_estimate_to_goal(start)
        # Estimated total cost from start to goal through y.
        f_score[start] = g_score[start] + h_score[start]    

        self.openset[start] = f_score[start]

        while len(self.openset) > 0:
            x = self.openset.pop_smallest()

            if self.is_goal_node(x):
                self.path = self.reconstruct_path(came_from, x)
                return True

            self.visited.append(x)

            for y in self.neighbor_nodes(x):
                if y in self.visited:
                    continue

                tentative_g_score = g_score[x] + self.dist_between(x, y)

                if y not in self.openset:
                    tentative_is_better = True
                elif y in g_score and tentative_g_score < g_score[y]:
                    tentative_is_better = True
                else:
                    tentative_is_better = False

                if tentative_is_better:
                    came_from[y] = x
                    g_score[y] = tentative_g_score
                    h_score[y] = self.heuristic_cost_estimate_to_goal(y)
                    f_score[y] = g_score[y] + h_score[y]
                    self.openset[y] = f_score[y]

        return False

    def reconstruct_path(self, came_from, current_node):
        if current_node in came_from:
            p = self.reconstruct_path(came_from, came_from[current_node])
            p.append(current_node)
            return p
        else:
            return [current_node]

    def neighbor_nodes(self, node):
        """
        Return a generator for the nodes that can be accessed from this node.
        """
        raise NotImplementedError

    def heuristic_cost_estimate_to_goal(self, node):
        """
        Provide an estimation of the distance to the goal node,
        by returning 0, we effectively perform Dijkstra instead of A*.
        """
        return 0 

    def is_goal_node(self, node):
        """
        A node is a goal node if the node is on the last row of the pyramid.
        """
        raise NotImplementedError

    def dist_between(self, node, other_node):
        """ distance between two neighbouring nodes """
        raise NotImplementedError


class AStarPyramid(AStarAlgorithm):
    """ Class that implements A* methods for the pyramid problem """

    def __init__(self, pyramid):
        self.pyramid = pyramid
        super(AStarPyramid, self).__init__()

    def neighbor_nodes(self, node):
        """
        Return a generator for the nodes that can be accessed from this node.
        """
        row = node[0] + 1
        left_bound = node[1]
        right_bound = node[1] + 1
        return ((row, col) for col in range(left_bound, right_bound + 1))

    def is_goal_node(self, node):
        """
        A node is a goal node if the node is on the last row of the pyramid.
        """
        return node[0] == len(self.pyramid) - 1

    def dist_between(self, node, other_node):
        """
        Distance between two neighbouring nodes.
        """
        row = other_node[0]
        col = other_node[1]
        return (100 - self.pyramid[row][col])

    def display_pyramid(self):
        """
        Graphically display the pyramid, showing the path chosen.
        """
        import sys
        from colorama import init as colorama_init, Style, Fore
        colorama_init()
        #isatty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        max_line_width = (len(self.pyramid[-1]) * 3) - 1
        for row in range(len(self.pyramid)):
            line = []
            for col in range(len(self.pyramid[row])):
                value = self.pyramid[row][col]
                if (row, col) in self.path:
                    line.append('%s%s%02i%s' % (Style.BRIGHT, Fore.GREEN, value, Style.RESET_ALL))
                elif (row, col) in self.visited:
                    line.append('%s%s%02i%s' % (Style.NORMAL, Fore.RED, value, Style.RESET_ALL))
                elif (row, col) in self.openset:
                    line.append('%s%s%02i%s' % (Style.BRIGHT, Fore.RED, value, Style.RESET_ALL))
                else:
                    line.append('%s%02i%s' % (Style.DIM, value, Style.RESET_ALL))
            line_width = (len(line) * 3) - 1
            space_width = (max_line_width // 2) - (line_width // 2)
            line.insert(0, ' ' * space_width)
            print(' '.join(line))
        print('')

