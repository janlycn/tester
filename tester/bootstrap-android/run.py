
import os
import sys

from settings import TEST_COLLECTION

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        raise RuntimeError('缺少参数')

    test_key = sys.argv[1]
    tests_folder = os.path.abspath(__file__ + '/../tests')
    reports_folder = os.path.abspath(__file__ + '/../reports')

    command = None

    if test_key == 'all':
        command = 'pytest %s --html=%s --self-contained-html' % (
            tests_folder, reports_folder + '/all.html')
    elif TEST_COLLECTION.get(test_key) != None:
        test_mode = TEST_COLLECTION[test_key]
        if isinstance(test_mode, dict):
            command = 'pytest %s --html=%s --self-contained-html' % (
                tests_folder + '/%s' % test_mode["pattern"], reports_folder + '/%s' % test_mode["report"])
        if isinstance(test_mode, str):
            command = 'pytest %s/%s' % (tests_folder, test_mode)

    if command:
        print(command)
        os.system(command)
    else:
        raise RuntimeError('参数错误')
