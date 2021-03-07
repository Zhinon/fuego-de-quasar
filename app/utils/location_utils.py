from sympy import (
    Circle,
    Point,
)

def get_message_origin(list_of_positions_and_distance):
    """
    This method receive a list with all postions and the distance to the emisor.
    To to get the origin this method create three circles and get the intersection
    point between this circles

    >>> get_message_origin([(-1, 0, 1), (0, -2, 2), (3, 0, 3)])
    (0, 0)
    """

    circle_one = Circle(
        Point(list_of_positions_and_distance[0][0],list_of_positions_and_distance[0][1]),
        list_of_positions_and_distance[0][2]
    )
    circle_two = Circle(
        Point(list_of_positions_and_distance[1][0],list_of_positions_and_distance[1][1]),
        list_of_positions_and_distance[1][2]
    )
    circle_three = Circle(
        Point(list_of_positions_and_distance[2][0],list_of_positions_and_distance[2][1]),
        list_of_positions_and_distance[2][2]
    )

    intersection_point_set = (
        set(circle_one.intersection(circle_two)) &
        set(circle_one.intersection(circle_three)) &
        set(circle_two.intersection(circle_three))
    )

    if len(intersection_point_set) != 1:
        # None or more than 1 point where found
        raise Exception

    intersection_point = intersection_point_set.pop()

    return intersection_point.x, intersection_point.y
