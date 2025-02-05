from unittest.mock import mock_open, patch

from src.utils import read_json_transactions


@patch("os.path.isfile")
def test_file_does_not_exist(mock_isfile):
    mock_isfile.return_value = False
    result = read_json_transactions("non_existent_file.json")
    assert result == []


@patch("os.path.isfile")
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"amount": 100, "currency": "EUR"}]',
)
def test_read_valid_json(mock_file, mock_isfile):
    mock_isfile.return_value = True
    result = read_json_transactions("valid_file.json")
    expected = [{"amount": 100, "currency": "EUR"}]
    assert result == expected


@patch("os.path.isfile")
@patch("builtins.open", new_callable=mock_open, read_data="not a json")
def test_read_invalid_json(mock_file, mock_isfile):
    mock_isfile.return_value = True
    result = read_json_transactions("invalid_file.json")
    assert result == []


@patch("os.path.isfile")
@patch("builtins.open", new_callable=mock_open, read_data="{}")
def test_read_empty_json_object(mock_file, mock_isfile):
    mock_isfile.return_value = True
    result = read_json_transactions("empty_object.json")
    assert result == []
