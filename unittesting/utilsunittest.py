from matritools import utils as mu
import pytest

# region no clamp, no handle error

def test_interpolator_no_clamp_no_handle_error_within_range():
	assert mu.make_interpolator(0, 10, 20, 30)(5) == 25
	
def test_interpolator_no_clamp_no_handle_error_out_of_range():
	assert mu.make_interpolator(0, 10, 20, 30)(15) == 35
	
def test_interpolator_no_clamp_no_handle_error_bad_input():
	with pytest.raises(TypeError):
		mu.make_interpolator(0, 10, 20, 30)('15')
		
# endregion

# region clamp, no handle error

def test_interpolator_clamp_no_handle_error_within_range():
	assert mu.make_interpolator(0, 10, 20, 30, True, )(5) == 25
	
def test_interpolator_clamp_no_handle_error_lower_than_range():
	assert mu.make_interpolator(0, 10, 20, 30, True, )(-1) == 20
	
def test_interpolator_clamp_no_handle_error_higher_than_range():
	assert mu.make_interpolator(0, 10, 20, 30, True, )(11) == 30

# endregion

# region no clamp, handle error
		
def test_interpolator_no_clamp_handle_error_no_default_value_castable_str():
	assert mu.make_interpolator(0, 10, 20, 30, False, True)('15') == 35
	
def test_interpolator_no_clamp_handle_error_no_default_value_bad_input():
	assert mu.make_interpolator(0, 10, 20, 30, False, True)('a') == None
	
def test_interpolator_no_clamp_handle_error_default_value_bad_input():
	assert mu.make_interpolator(0, 10, 20, 30, False, True, 5)('a') == 5
	
# endregion
