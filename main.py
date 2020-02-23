# -*- coding: utf-8 -*-
import time
import unittest
# from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner


def suite():
    start_dir = "/var/lib/jenkins/workspace/SL_Regression_Test(Release)"
    top = ".\SL_Regression_Test(Release)"
    print(start_dir)
    suite = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern='*test.py', top_level_dir=None)
    return suite


if __name__ == '__main__':
    localtime = time.localtime(time.time())
    now = str(localtime.tm_year) + '.' + str(localtime.tm_mon) + '.' + str(localtime.tm_mday) + '.' + str(
        localtime.tm_hour) + '.' + str(localtime.tm_min)
    fp = open('/SL_Test_Report(%s).html' % now, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='{ SL_Test_Report }',
        # description='',
        description="wq"
    )
    suite = suite()
    runner.run(suite)
    fp.close()
