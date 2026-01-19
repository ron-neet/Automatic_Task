import pytest
from phone_utils import normalize_phone

class TestNormalizePhone:
    
    # Valid Phone Numbers
    @pytest.mark.parametrize(
        "input_phone, expected",
        [
            ("9818725094", "+9779818725094"),
            ("09818725094", "+9779818725094"),
            ("9818725094", "+9779818725094"),
            ("9718725094", "+9779718725094"),
        ],
    )
    def test_valid_numbers(self, input_phone, expected):
        assert normalize_phone(input_phone) == expected
        
    # Invalid Phone Numbers
    @pytest.mark.parametrize(
        "input_phone",
        [
            ("9123456789"),
            ("981872"),
            ("9818ronit"),
        ],
    )
    def test_invalid_numbers(self, input_phone):
        with pytest.raises(ValueError):
            normalize_phone(input_phone)    
            
    # Edge Cases        
    @pytest.mark.parametrize(
        "input_phone, expected",
        [
            ("98 18 72 50 94", "+9779818725094"),
            ("(098)18725094", "+9779818725094"),
            ("+977-981-8725094", "+9779818725094"),
            ("97-18-72-50-94", "+9779718725094"),
        ],
    )
    def test_edge_cases(self, input_phone, expected):
        assert normalize_phone(input_phone) == expected
            