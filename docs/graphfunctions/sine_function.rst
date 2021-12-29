sine
----
Creates a cosine function with pre set parameters.

Y = round({cos([x + x_offset] * [pi / increments] * frequency) * amplitude} + y_offset, decimal_place)

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

    def print_sine(sine_function):
        string = ""
            for i in range(12):
                string += str(sine_function(i)) + ', '

        print(string)

    print_sine(graph.sine_function())
    # 0.0, 0.26, 0.5, 0.71, 0.87, 0.97, 1.0, 0.97, 0.87, 0.71, 0.5, 0.26,

    print_sine(graph.sine_function(amplitude=2))
    # 0.0, 0.52, 1.0, 1.41, 1.73, 1.93, 2.0, 1.93, 1.73, 1.41, 1.0, 0.52,

    print_sine(ani.sine_function(frequency=2))
    # 0.0, 0.5, 0.87, 1.0, 0.87, 0.5, 0.0, -0.5, -0.87, -1.0, -0.87, -0.5,

    print_sine(graph.sine_function(increments=24))
    # 0.0, 0.13, 0.26, 0.38, 0.5, 0.61, 0.71, 0.79, 0.87, 0.92, 0.97, 0.99,

    print_sine(graph.sine_function(x_offset=1))
    # 0.26, 0.5, 0.71, 0.87, 0.97, 1.0, 0.97, 0.87, 0.71, 0.5, 0.26, 0.0,

    print_sine(graph.sine_function(y_offset=1))
    # 1.0, 1.26, 1.5, 1.71, 1.87, 1.97, 2.0, 1.97, 1.87, 1.71, 1.5, 1.26,

    print_sine(graph.sine_function(decimal_place=1))
    # 0.0, 0.3, 0.5, 0.7, 0.9, 1.0, 1.0, 1.0, 0.9, 0.7, 0.5, 0.3,

