import pytest
from project import check_guess, is_valid_word, get_random_word, format_feedback, load_word_list

SAMPLE_WORDS = ["CRANE", "BRAVE", "APPLE", "BEACH", "TIGER", "STONE", "PLACE"]

def test_check_guess_all_correct():
    result = check_guess("CRANE", "CRANE")
    assert all(s == "correct" for _, s in result)

def test_check_guess_all_absent():
    result = check_guess("FLOSS", "CRIMP")
    assert all(s == "absent" for _, s in result)

def test_check_guess_mixed():
    result = check_guess("BRAVE", "BEACH")
    assert result[0] == ("B", "correct")
    assert result[1] == ("R", "absent")
    assert result[2] == ("A", "correct")
    assert result[3] == ("V", "absent")
    assert result[4] == ("E", "present")

def test_check_guess_duplicate_letters():
    result = check_guess("SCENE", "STONE")
    assert result[4] == ("E", "correct")
    assert result[2] == ("E", "absent")

def test_check_guess_case_insensitive():
    assert check_guess("crane", "brave") == check_guess("CRANE", "BRAVE")

def test_check_guess_length():
    assert len(check_guess("TIGER", "STONE")) == 5

def test_is_valid_word_in_list():
    assert is_valid_word("crane", SAMPLE_WORDS) is True

def test_is_valid_word_not_in_list():
    assert is_valid_word("ZZZZZ", SAMPLE_WORDS) is False

def test_is_valid_word_too_short():
    assert is_valid_word("CAT", SAMPLE_WORDS) is False

def test_is_valid_word_too_long():
    assert is_valid_word("PLANET", SAMPLE_WORDS) is False

def test_is_valid_word_digits():
    assert is_valid_word("CR4NE", SAMPLE_WORDS) is False

def test_is_valid_word_empty():
    assert is_valid_word("", SAMPLE_WORDS) is False

def test_is_valid_word_whitespace():
    assert is_valid_word("  crane  ", SAMPLE_WORDS) is True

def test_get_random_word_in_list():
    assert get_random_word(SAMPLE_WORDS) in SAMPLE_WORDS

def test_get_random_word_returns_string():
    assert isinstance(get_random_word(SAMPLE_WORDS), str)

def test_get_random_word_empty_raises():
    with pytest.raises(ValueError):
        get_random_word([])

def test_get_random_word_distribution():
    results = {get_random_word(SAMPLE_WORDS) for _ in range(500)}
    assert results == set(SAMPLE_WORDS)

def test_format_feedback_returns_string():
    result = check_guess("CRANE", "BRAVE")
    assert isinstance(format_feedback(result), str)

def test_format_feedback_contains_letters():
    result = check_guess("CRANE", "BRAVE")
    output = format_feedback(result)
    for letter in "CRANE":
        assert letter in output

def test_load_word_list_valid(tmp_path):
    f = tmp_path / "words.txt"
    f.write_text("crane\nbrave\napple\n")
    words = load_word_list(str(f))
    assert "CRANE" in words

def test_load_word_list_ignores_short(tmp_path):
    f = tmp_path / "words.txt"
    f.write_text("hi\ncrane\ncat\n")
    assert load_word_list(str(f)) == ["CRANE"]

def test_load_word_list_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_word_list(str(tmp_path / "missing.txt"))

def test_load_word_list_empty_raises(tmp_path):
    f = tmp_path / "words.txt"
    f.write_text("hi\ncat\n")
    with pytest.raises(ValueError):
        load_word_list(str(f))
