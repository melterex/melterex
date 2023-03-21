import subprocess
# .returncode если 0 все ок, если 1 то пизда
# check_output вместо run выводит результат, но с проблемами
# url = "https://www.sec.gov/Archives/edgar/full-index/{0}/QTR{1}/master.idx".format(year, qtr)
# url = bytes(url)
print(subprocess.run(['python.exe', "test_1.py"], input=b"1\n 1 2\n"))
# subprocess.check_output(['python.exe', "test_1.py"], input=b"1\n", shell=True) 