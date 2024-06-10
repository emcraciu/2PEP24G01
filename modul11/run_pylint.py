import pylint

# option = ["--rcfile=pylintrc", "part1.py"]
# pylint.run_pylint(argv=option)

option = ["--rcfile=pylintrc", "part2.py"]
pylint.run_pylint(argv=option)

# option = ['--generate-rcfile', ".generated_rc"]
# pylint.run_pylint(argv=option)
