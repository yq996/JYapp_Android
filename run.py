import os
import pytest

if __name__=="__main__":
    pytest.main(["-n","1","-vs","--alluredir", "./report/json_report", "--clean-alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")