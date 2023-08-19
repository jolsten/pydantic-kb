import pytest
import yaml
from pydantic import ValidationError
from ssr import load_yaml, Facility

def test_facility_1():
    facility = '''
        ---!Facility
        name: Valid Facility
        type: Satellite Control Site
        lat: 12.345
        lon: 23.456
    '''
    seq = load_yaml(facility)
    print(seq)
    for f in seq:
        assert isinstance(f, Facility)

def test_invalid_type():
    facility = '''
    ---!Facility
        name: Invalid Type
        type: Invalid Facility Type
        lat: 12.345
        lon: 23.456
    '''
    with pytest.raises(ValidationError):
        load_yaml(facility)

def test_invalid_latitude():
    facility = '''
    ---!Facility
        name: Invalid Latitude
        type: Satellite Control Site
        lat: 99.345
        lon: 23.456
    '''
    with pytest.raises(ValidationError):
        load_yaml(facility)

def test_invalid_longitude():
    facility = '''
    ---!Facility
        name: Invalid Longitude
        type: Satellite Control Site
        lat: 12.345
        lon: 320.456
    '''
    with pytest.raises(ValidationError):
        load_yaml(facility)
