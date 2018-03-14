import HTMLTestRunner
import unittest

from HtmlTestRunner import runner

from TestCase.test_login import test_login

if __name__ == '__main__':
    #suitcase = unittest.TestLoader().loadTestsFromTestCase(test_login)
    #unittest.TextTestRunner(verbosity=2).run(suitcase)
    suite = unittest.TestLoader().loadTestsFromTestCase(test_login)

    filename = 'D:\lqf\eli_test\TestReport\Report.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"TestReport",
        description=u"Result"
    )
    runner.run(suite)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    fp.close()