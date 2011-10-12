# vim: sw=4:ts=4:et:ai

import os
import os.path
import re
import doctest

def main():
    # Execute all problems and show their answer
    problems = []
    for filename in os.listdir('.'):
        if not os.path.isfile(filename):
            continue
        matches = re.match(r'^problem(\d+).py$', filename)
        if not matches:
            continue
        problem_num = int(matches.group(1))
        problems.append(problem_num)

    problems.sort()
    for problem_num in problems:
        module = 'problem%i' % problem_num
        x = __import__(module)
        doctest.testmod(x)
        try:
            print("Problem %s result: %i" % (problem_num, x.main()))
        except AttributeError:
            print("Module '%s' is not compatible (no main)." % module)
        except TypeError:
            print("Module '%s' problem when executing main." % module)

if __name__ == '__main__':
    main()

