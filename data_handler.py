import statzcw
import csv
import statistics


def read_data(file: csv) -> tuple:
    x, y = [], []
    with open(file, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            x.append(row['x'])
            y.append(row['y'])
    return x, y

def IO_test(data: dict):
    data_string = " "
    for keyword in data.keys():
        data_string = data_string + keyword + ', '
    print('Data sets:' + data_string)
    print('Run IO test\n')
    [print(f'{keyword}:{values}') for keyword, values in data.items()]


def run_stazcw(lx: list, ly:list) -> list:
    return [
        statzcw.zmean(lx),
        statzcw.zvariance(lx),
        statzcw.zmean(ly),
        statzcw.zvariance(ly),
        statzcw.zcorr(lx, ly)
    ]

def run_statistics(lx: list, ly:list) -> list:
    return[
        statistics.mean(lx),
        statistics.variance(lx),
        statistics.mean(ly),
        statistics.variance(ly),
        statistics.correlation(lx,ly)
    ]

def run_tests(data: dict):
    for keyword, values in data.items():
        pass


def display_data(data: dict):
    IO_test(data)
    run_stazcw(data['x'],data['y'])
    run_statistics(data['x'],data['y'])




def gather_data(data: list) -> dict:
    return {d: read_data(d) for d in data}


data = gather_data(['dataZero.csv', 'dataOne.csv', 'dataTwo.csv', 'dataThree.csv'])
display_data(data)
#
# - Count of X
# - Count of Y
# - Mean of X
# - Sample Variance of X
# - Mean of Y
# - SampleVariance of Y
# - Correlation between X and Y (should be ~0.816)
#
# Also produce the
#
# - Median of X
# - Median of Y
# - Mode of X
# - Mode of Y
# - Sample Std deviation of X
# - Sample Std Deviation of Y
# - Standard Error of the Mean of X
# - Standard Error of the Mean of Y
#
#
