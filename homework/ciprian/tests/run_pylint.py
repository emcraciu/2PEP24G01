import pylint
from homework.ciprian.StockApp.decorators import log_time_decorator

@log_time_decorator
def run_pylint_test(file):
    file = '../StockApp/' + str(file)
    option = ["--rcfile=pylintrc", file]
    return pylint.run_pylint(argv=option)


if __name__ == "__main__":
    run_pylint_test('stock_app.py')
    # run_test(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\stock_app.py')