# vim: sw=4:ts=4:et:ai
"""

Approach:
 Use Edsger Dijkstra's algorithm to find the path with the lowest score.

"""

from eulertools.a_star import AStarMatrix

class AStarMinimalMatrix(AStarMatrix):
    """ Slightly modified version of class used in problem 81 """

    def neighbor_nodes(self, node):
        """
        Generator for the nodes that can be accessed from this node.
        """
        row = node[0]
        col = node[1]
        if row < (self.num_rows - 1):
            # We can still go down
            yield (row + 1, col)
        if row > 0:
            # We can still go up
            yield (row - 1, col)
        if col < (self.num_cols - 1):
            # We can still go to the right
            yield (row, col + 1)
        if col > 0:
            # We can still go to the left
            yield (row, col - 1)

    def is_goal_node(self, node):
        """
        A node is the goal node if it's the bottom right node.
        """
        return node[0] == self.num_rows - 1 and node[1] == self.num_cols - 1

def astar_minimal_matrix(matrix):
    """
    >>> astar_minimal_matrix(((131, 673, 234, 103,  18), (201, 96,  342, 965, 150), (630, 803, 746, 422, 111), (537, 699, 497, 121, 956), (805, 732, 524,  37, 331)))
    2297
    """
    # The start node is the top left node
    start = (0, 0)
    a_star = AStarMinimalMatrix(matrix)
    a_star.a_star(start)
    return sum(matrix[row][col] for row, col in a_star.path if row >= 0 and col >= 0)
    
def main(debug=False):
    matrix = []
    for line in open('resources/matrix.txt', 'r'):
        row = [int(n) for n in line.split(',')]
        matrix.append(row)
    return astar_minimal_matrix(matrix)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Result: %i" % main(True))

