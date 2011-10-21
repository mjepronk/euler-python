# vim: sw=4:ts=4:et:ai
"""

Approach:
 Use Edsger Dijkstra's algorithm to find the path with the highest score.

"""

from eulertools.a_star import AStarPyramid

def main(debug=False):
    pyramid = []
    for line in open('resources/triangle.txt', 'r'):
        row = [int(n) for n in line.split(' ')]
        pyramid.append(row)

    start = (0, 0)
    a_star = AStarPyramid(pyramid)
    a_star.a_star(start)
    if debug:
        a_star.display_pyramid()
    return sum(pyramid[row][col] for row, col in a_star.path)


if __name__ == '__main__':
    print("Result: %i" % main(True))

