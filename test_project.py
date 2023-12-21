from project import ticker_validation, date_verification, date_process
from datetime import date
import pytest

def test_ticker_validation():
    #si el ticker existe retorna true si no retorna False
    tic = "gabagoo"
    with pytest.raises(Exception):
        ticker_validation(tic)
    ti_input= "ba"
    success, ti_info, updated_ti_input = ticker_validation(ti_input)
    assert success is True
    

def test_date_verification():
    #si el formato de fecha es correcto, retorna True y start_date
    d = "1999-01"
    test_date = date(1999, 1, 1)
    result, start_date = date_verification(d)
    assert result is True
    assert start_date == test_date

def test_date_process():
    result = date_process("2023", "01")
    assert result == date(2023, 1, 1)
    with pytest.raises(ValueError):
        date_process("2025", "17")
    with pytest.raises(ValueError):
        date_process("asfgoga", "06")

