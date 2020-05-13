import sys
sys.path.append('..')

from mycodes.mycode import WantTest
from mycodes.mycode import AdditionalClass
import pytest

obj = WantTest()

@pytest.fixture()
def return_obj():
    return obj


obj_addition = AdditionalClass([1,2,3])
obj_addition2 = AdditionalClass([])

@pytest.fixture()
def return_additional_obj():
    return obj_addition

@pytest.fixture()
def return_additional_obj2():
    return obj_addition2

