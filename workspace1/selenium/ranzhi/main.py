from runner.test_runner import TestRunner

class Main:

    def start(self):
        '''调用runner方法，运行测试用例'''
        TestRunner().runner()

if __name__ == "__main__":
    Main().start()