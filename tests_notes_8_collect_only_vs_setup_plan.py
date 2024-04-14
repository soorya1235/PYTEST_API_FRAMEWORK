"""
The --collect-only and --setup-plan options in pytest serve different purposes,
but they can be complementary in certain scenarios:

--collect-only: This option is used to collect information about the tests without actually executing them.
It provides a detailed report of all the tests that pytest has discovered in your project, including test functions,
test classes, fixtures, and any custom markers. The purpose is mainly to inspect how pytest discovers tests and to
debug any issues related to test discovery.

--setup-plan: This option is used to display a plan of what fixtures would be set up for each test without running
the tests or actually setting up the fixtures. It helps you understand the fixture dependency graph and fixture setup
order in your test suite. This can be useful for debugging fixture-related issues and for understanding how pytest sets up fixtures before running tests.

In summary, --collect-only is focused on test discovery, while --setup-plan is focused on fixture setup planning.
Depending on your needs, you may use one or both options to gain insights into your test suite and ensure its
correctness and efficiency.
"""