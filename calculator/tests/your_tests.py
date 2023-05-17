#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run("3 * 3").output == "9"
assert run("2 + 2").exit_status == 0

###

print("All tests passed!")
