import pytest
import yaml
from pydantic import ValidationError
import ssr
from ssr import Facility

facility1 = '''
!Facility
name: Facility 1
type: Satellite Control Site
lat: 12.345
lon: 23.456
'''

facility2 = '''
!Facility
name: Facility 2
type: Satellite Control Site
lat: 23.456
lon: 34.567
'''

from ssr import Facility
import yaml
yaml.add_constructor('Facility', Facility, yaml.FullLoader)

@pytest.mark.parametrize('facility', [facility1, facility2])
def test_facility_1(facility):
    yaml.load(facility, yaml.FullLoader)

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
