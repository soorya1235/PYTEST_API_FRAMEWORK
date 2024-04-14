class Testsuper:

    def test_method1(self):
        print("method1")

    def test_method2(self):
        print("method2")

    def test_method3(self):
        print("method2")


"""
1.pytest test_1_example.py -s -v
-s will display print the output to stdout
-v will display the testcase status passed or failed.
2.if the test case name does not start with test_ or end with _test
pytest will not execute the test with aatest_method2

3.if the class name does not start with Test,pytest will not exeuct the test
4.pytest -k example (will run the test cases from
both the files test_1_example.py, test_2_classname_no_start_test_example.py.(Because both has example 
which matches the regular expression"
output is found in test_3_output.png

It will search the whole directory "pytest_learning_withcomment" and it will search
for testcasefilename which has example in it or a filename which does not have example in filename,
it will search for the testcase in that filewhich has example in that.
Ex:test_4_dummpy.py does not "example" in the testcase name,but inside that class
there is a testcase with name "test_method3_example" os it will exeucte that also.
test_5_dummpy_output.png



"""
