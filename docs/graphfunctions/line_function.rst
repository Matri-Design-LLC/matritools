cosine
------
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

    def print_line(sine_function):
    string = ""
    for i in range(12):
        string += str(sine_function(i)) + ', '

    #print(string)

    print_line(graph.line_function())
    # 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0,

    print_line(graph.line_function(slope=2))
    # 0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0,

    print_line(graph.line_function(x_offset=1))
    # 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0,

    print_line(graph.line_function(x_offset=-1, y_offset=0.5))
    # -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5,

    print_line(graph.line_function(decimal_place=1))
    # 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0,

