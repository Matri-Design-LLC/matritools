import matritools.nodefile as nf


print("Testing AntzGlyph")
tests = []

#region constructor

try:
    test_glyph = nf.AntzGlyph()
    tests.append("Fail: empty construtor")
except RuntimeError:
    tests.append("Pass: empty constructor")

try:
    test_glyph0 = nf.AntzGlyph("no file ext")
    tests.append("Fail: no csv file extion")
except RuntimeError:
    tests.append("Pass: no csv file extension")

try:
    test_glyph1 = nf.AntzGlyph("Test1.csv")
    tests.append("Pass: proper formated csv input to constructor")
except:
    tests.append("Fail: proper formated csv input to constructor")

try:
    test_glyph2 = nf.AntzGlyph("Test2.csv")
    tests.append("Fail: improper formated csv input to constructor")
except:
    tests.append("Pass: improper formated csv input to constructor")

try:
    test_glyph3 = nf.AntzGlyph("Test3.csv")
    tests.append("Fail: csv rows with reserved ids input to constructor")
except:
    tests.append("Pass: csv rows with reserved ids input to constructor")

#endregion

correct_results = [45, 46, 47, 48, 49, 50, 51]
test_glyph4 = nf.AntzGlyph("Test4.csv")
test_glyph4.increment_node_file_rows()

i = 0
success = True
for row in test_glyph4.node_file_rows:
    if row.id != correct_results[i]:
        tests.append("Fail: id properly incremented")
        success = False
        break
    i += 1
    print(i)

if success:
    tests.append("Pass: id properly incremented")


############ test other parent id and child id


print("\n******************Results***************")
for test in tests:
    print(test)