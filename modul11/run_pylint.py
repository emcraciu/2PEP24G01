import pylint

option = ["--rcfile=pylintrc", "part1.py"]
pylint.run_pylint(argv=option)

# option = ['--generate-rcfile']
# pylint.run_pylint(argv=option)
