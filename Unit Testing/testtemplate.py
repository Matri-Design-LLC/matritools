def template(name, number):

    return "# region set " + name + "\n\n" + \
    'print("'+ str(number) + '. set ' + name + ' correct input ints")\n' + \
    'test_nfr.set_' + name + '(100, 200, 300)\n' + \
    'if test_nfr.' + name + '_x == 100 and test_nfr.' + name + '_y == 200 and test_nfr.' + name + '_z == 300:\n' + \
        '\ttests.append("Pass: set ' + name + ' correct input ints")\n' + \
    'else:\n' + \
        '\ttests.append("Fail: set '+ name + ' correct input ints")\n\n' + \
    'print("'+ str(number + 1) + '. set '+ name + ' correct input castable strings")\n' + \
    'test_nfr.set_'+ name + '("400", "500", "600")\n' + \
    'if test_nfr.'+ name + '_x == 400 and test_nfr.'+ name + '_y == 500 and test_nfr.'+ name + '_z == 600:\n' + \
        '\ttests.append("Pass: set '+ name + ' correct input castable strings")\n' + \
    'else:\n' + \
        '\ttests.append("Fail: set '+ name + ' correct input castable strings")\n\n' + \
    'print("'+ str(number + 2) + '. set '+ name + ' correct input castable floats")\n' + \
    'test_nfr.set_'+ name + '(700.0, 800.0, 900.0)\n' + \
    'if test_nfr.'+ name + '_x == 700 and test_nfr.'+ name + '_y == 800 and test_nfr.'+ name + '_z == 900:\n' + \
        '\ttests.append("Pass: set '+ name + ' correct input castable floats")\n' + \
    'else:\n' + \
        '\ttests.append("Fail: set '+ name + ' correct input castable floats")\n\n' + \
    '# endregion'

print(template("segments", 71))