import pytest

from matcher.score.logic import calculate_match_score
from matcher.score.errors import EmptyInputRecord


@pytest.mark.parametrize(
    'input_record, db_record',
    [
        (
            {'col1': 'val1', 'col2': 'val2'},
            None
        )
    ]
)
def test_calculate_match_score_with_empty_db_record(input_record, db_record):
    expected = 0.00
    result = calculate_match_score(input_record, db_record)

    assert expected == result


@pytest.mark.parametrize(
    'input_record, db_record',
    [
        (
            None,
            None
        )
    ]
)
def test_calculate_match_score_empty_input_record(input_record, db_record):
    with pytest.raises(EmptyInputRecord):
        calculate_match_score(input_record, db_record)
