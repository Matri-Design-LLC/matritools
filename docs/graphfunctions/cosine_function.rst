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

    def print_cosine(cosine_function):
        string = ""
            for i in range(12):
                string += str(cosine_function(i)) + ', '

        print(string)

    print_cosine(graph.cosine_function())
    # 1.0, 0.97, 0.87, 0.71, 0.5, 0.26, 0.0, -0.26, -0.5, -0.71, -0.87, -0.97,

    print_cosine(graph.cosine_function(amplitude=2))
    # 2.0, 1.93, 1.73, 1.41, 1.0, 0.52, 0.0, -0.52, -1.0, -1.41, -1.73, -1.93,

    print_cosine(graph.cosine_function(frequency=2))
    # 1.0, 0.87, 0.5, 0.0, -0.5, -0.87, -1.0, -0.87, -0.5, 0.0, 0.5, 0.87,

    print_cosine(graph.cosine_function(increments=24))
    # 1.0, 0.99, 0.97, 0.92, 0.87, 0.79, 0.71, 0.61, 0.5, 0.38, 0.26, 0.13,

    print_cosine(graph.cosine_function(x_offset=1))
    # 0.97, 0.87, 0.71, 0.5, 0.26, 0.0, -0.26, -0.5, -0.71, -0.87, -0.97, -1.0,

    print_cosine(graph.cosine_function(y_offset=1))
    # 2.0, 1.97, 1.87, 1.71, 1.5, 1.26, 1.0, 0.74, 0.5, 0.29000000000000004, 0.13, 0.030000000000000027,

    print_cosine(graph.cosine_function(decimal_place=1))
    # 1.0, 1.0, 0.9, 0.7, 0.5, 0.3, 0.0, -0.3, -0.5, -0.7, -0.9, -1.0,

