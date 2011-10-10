# vim: sw=4:ts=4:et:ai

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
 (04, 62, 98, 27, 23, 09, 70, 98, 73, 93, 38, 53, 60, 04, 23))


def neighbor_nodes(x):
    pass

def a_star(start, goal):
    # The set of nodes already evaluated.
    closedset = set()
    # The set of tentative nodes to be evaluated, initially containing the start node
    openset = set(start)
    # The map of navigated nodes.
    came_from = {}
 
    # Cost from start along best known path.
    g_score[start] := 0
    h_score[start] := heuristic_cost_estimate(start, goal)
    # Estimated total cost from start to goal through y.
    f_score[start] := g_score[start] + h_score[start]    

    while openset is not empty
        x := the node in openset having the lowest f_score[] value
        if x = goal
            return reconstruct_path(came_from, came_from[goal])

        remove x from openset
        add x to closedset
        foreach y in neighbor_nodes(x)
            if y in closedset
                continue
            tentative_g_score := g_score[x] + dist_between(x,y)

            if y not in openset
                add y to openset
                tentative_is_better := true
            elif tentative_g_score < g_score[y]
                tentative_is_better := true
            else
                tentative_is_better := false

            if tentative_is_better = true
                came_from[y] := x
                g_score[y] := tentative_g_score
                h_score[y] := heuristic_cost_estimate(y, goal)
                f_score[y] := g_score[y] + h_score[y]

    return failure
 
 function reconstruct_path(came_from, current_node)
     if came_from[current_node] is set
         p = reconstruct_path(came_from, came_from[current_node])
         return (p + current_node)
     else
         return current_node

