from my_module import add

# test_fetch_data.py

import requests
import pytest
from my_module import fetch_data


def test_fetch_data_success(mocker):
    # Mock the requests.get function
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "example"}
    mocker.patch.object(requests, "get", return_value=mock_response)

    # Test the function
    data = fetch_data("http://example.com/api/data")
    assert data == {"data": "example"}


def test_fetch_data_failure(mocker):
    # Mock the requests.get function to raise an exception
    mocker.patch.object(requests, "get", side_effect=requests.RequestException)

    # Test the function
    data = fetch_data("http://example.com/api/data")
    assert data is None


def test_add():
    assert add(2, 3) == 5
