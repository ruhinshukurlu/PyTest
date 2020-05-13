import pytest

@pytest.mark.usefixtures('return_obj')
class TestMycode:
    def test_hello_world(self, return_obj):
        assert return_obj.hello_world() == "hello,world"
    
    def test_integer_division(self,return_obj):
        assert return_obj.integer_division(6,2) == 3
        #assert mycode.integer_division(3,0) == "Division by zero detected!!!"
        with pytest.raises(ZeroDivisionError):
            return_obj.integer_division(6,0)
        #assert mycode.integer_division('tech',6) == "Expecting integers as parameters!" 
        with pytest.raises(TypeError):
            return_obj.integer_division('tech',5)
        assert isinstance(return_obj.integer_division(8.4,2),int)

    @pytest.mark.usefixtures('return_additional_obj','return_additional_obj2')
    def test_additional_obj_counter(self,return_additional_obj,return_additional_obj2):
        assert return_additional_obj.counter() == 3
        assert return_additional_obj2.counter() == 0
    