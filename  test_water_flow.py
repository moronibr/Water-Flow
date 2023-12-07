#Moroni Bamvakiades Ramos
#11/08/2023
#Python documentation, ChatGPT, Codeium


from pytest import approx
import pytest


from water_flow import mbr_water_column_height
from water_flow import mbr_pressure_gain_from_water_height
from water_flow import mbr_pressure_loss_from_pipe


#This code snippet is a set of test cases for the function mbr_water_column_height(). 
# It verifies that the function returns the expected values for different input parameters.
def test_water_column_height():
   column_height = mbr_water_column_height(0,0)
   assert column_height == 0 
   
   column_height = mbr_water_column_height(0,10)
   assert column_height == 7.5 
   
   column_height = mbr_water_column_height(25, 0)
   assert column_height == 25 
   
   column_height = mbr_water_column_height(48.3, 12.8)
   assert column_height == 57.9 


    
#This code snippet is a test function for the mbr_pressure_gain_from_water_height function. 
#It asserts that when the function is called with different water heights, 
#it should return the expected pressure gains. 
#The approx function is used to allow for a small margin of error in the expected results.    
def test_pressure_gain_from_water_height():
    
    assert mbr_pressure_gain_from_water_height(0) == approx(0)
    
    assert mbr_pressure_gain_from_water_height(30.2) == approx(295.628)

    assert mbr_pressure_gain_from_water_height(50) == approx(489.450)
    

#This code snippet is a unit test for the function mbr_pressure_loss_from_pipe(). 
#It calls the function with different input values and asserts that the returned pressure loss matches the expected values. 
#If the assertion fails, it means that the function is not returning the expected result.    
def test_pressure_loss_from_pipe():

    pressure_loss = mbr_pressure_loss_from_pipe(0.048692, 0, 0.018,	1.75)
    assert pressure_loss == 0
    
    pressure_loss = mbr_pressure_loss_from_pipe(0.048692, 200, 0, 1.75)
    assert pressure_loss == 0
    
    pressure_loss = mbr_pressure_loss_from_pipe(0.048692, 200, 0.018, 0)
    assert pressure_loss == 0
    
    pressure_loss = mbr_pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75)
    assert pressure_loss == -113.008
    
    pressure_loss = mbr_pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65)
    assert pressure_loss == -100.462	
    
    pressure_loss = mbr_pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.55)
    assert pressure_loss == -61.576	
    
    pressure_loss = mbr_pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65)
    assert pressure_loss == -55.072	
    
    pressure_loss = mbr_pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65)
    assert pressure_loss == -110.884
    
    
    
    
pytest.main(["-v", "--tb=line", "-rN", __file__])