# vim: sw=4:ts=4:et:ai
"""

Approach:
 Use Edsger Dijkstra's algorithm to find the path with the highest score.

"""

from eulertools.a_star import AStarMatrix

def main(debug=False):
    matrix = []
    for line in open('resources/matrix.txt', 'r'):
        row = [int(n) for n in line.split(',')]
        matrix.append(row)

    start = (0, 0)
    a_star = AStarMatrix(matrix)
    a_star.a_star(start)
    return sum(matrix[row][col] for row, col in a_star.path)

if __name__ == '__main__':
    print("Result: %i" % main(True))

