import pytest

from functions import clear_punctuation


def test_clear_punctuation():
    result = clear_punctuation('%мама, !мыла, ?раму.')
    assert result == "мама мыла раму", "Ошибка в удаление знаков"
