import pytest
from pydantic import ValidationError
from ssr import Facility

facility1 = '''
name: Facility 1
type: Satellite Control Site
lat: 12.345
lon: 23.456
'''

facility2 = '''
name: Facility 2
type: Satellite Control Site
lat: 23.456
lon: 34.567
'''

@pytest.mark.parametrize('facility', [facility1, facility2])
def test_facility_1(facility):
    Facility.from_yaml(facility)

def test_invalid_type():
    facility = '''
        name: Facility 3
        type: Invalid Facility Type
        lat: 12.345
        lon: 23.456
    '''
    with pytest.raises(ValidationError):
        Facility.from_yaml(facility)

def test_invalid_latitude():
    facility = '''
        name: Facility 3
        type: Satellite Control Site
        lat: 99.345
        lon: 23.456
    '''
    with pytest.raises(ValidationError):
        Facility.from_yaml(facility)

def test_invalid_latitude():
    facility = '''
        name: Facility 3
        type: Satellite Control Site
        lat: 12.345
        lon: 320.456
    '''
    with pytest.raises(ValidationError):
        Facility.from_yaml(facility)
