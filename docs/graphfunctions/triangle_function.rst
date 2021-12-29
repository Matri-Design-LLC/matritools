triangle_function
-----------------
Creates a sine function with pre set parameters.

Y = round({sin([x + x_offset] * [pi / increments] * frequency) * amplitude} + y_offset, decimal_place)

Parameters:

+---------------+------------------------------------------------------------------+-------+---------+
| Name          | Description                                                      | Type  | Default |
+===============+==================================================================+=======+=========+
| amplitude     | Effects the min and max output of the function.                  | float | 1       |
+---------------+------------------------------------------------------------------+-------+---------+
| frequency     | Effect how frequently the value rises and falls over time.       | float | 1       |
+---------------+------------------------------------------------------------------+-------+---------+
| increments    | Effects how many increments a wave is measured at.               | float | 12      |
+---------------+------------------------------------------------------------------+-------+---------+
| x_offset      | The amount x is offset before being transformed by the function. | float | 0       |
+---------------+------------------------------------------------------------------+-------+---------+
| y_offset      | The amount the final result is offset by.                        | float | 0       |
+---------------+------------------------------------------------------------------+-------+---------+
| decimal_place | The number of decimal places the function is rounded by.         | int   | 2       |
+---------------+------------------------------------------------------------------+-------+---------+

Returns:
    cosine function
        Parameters:
            x (float)
        Returns:
            Float

Raises:
    TypeError

Example::

    from matritools import graphfunctions as graph

    def print_triangle(triangle_function):
    string = ""
    for i in range(12):
        string += str(triangle_function(i)) + ', '

    print(string)

    print_triangle(graph.triangle_function())
    # 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0,
    print_triangle(graph.triangle_function(slope=2))
    # 0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 8.0, 6.0, 4.0, 2.0, 0.0, 2.0,
    print_triangle(graph.triangle_function(period=2))
    # 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0,
    print_triangle(graph.triangle_function(x_offset=1))
    # 1.0, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0,
    print_triangle(graph.triangle_function(y_offset=1))
    # 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 2.0,
    print_triangle(graph.triangle_function(decimal_place=1))
    # 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0,


