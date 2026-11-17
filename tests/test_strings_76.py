"""Тесты задачи №76."""

import pytest
from conftest import assert_case, case_ids

COMPRESS = {
    "module": "solution",
    "cases": [
        {"input": {"word": "aasssbb"}, "output": "a2s3b2"},
        {"input": {"word": ""}, "output": ""},
        {"input": {"word": "abc"}, "output": "abc"},
        {"input": {"word": "aaaa"}, "output": "a4"},
        {"input": {"word": "abbba"}, "output": "ab3a"},
    ],
}

DECOMPRESS = {
    "module": "solution",
    "cases": [
        {"input": {"encoded": "a2s3b2"}, "output": "aasssbb"},
        {"input": {"encoded": ""}, "output": ""},
        {"input": {"encoded": "abc"}, "output": "abc"},
        {"input": {"encoded": "a10"}, "output": "aaaaaaaaaa"},
    ],
}


@pytest.mark.parametrize("case", COMPRESS["cases"], ids=case_ids(COMPRESS["cases"]))
def test_compress_string(solution, case):
    assert_case(solution, "compress_string", COMPRESS, case)


@pytest.mark.parametrize("case", DECOMPRESS["cases"], ids=case_ids(DECOMPRESS["cases"]))
def test_decompress_string(solution, case):
    assert_case(solution, "decompress_string", DECOMPRESS, case)


@pytest.mark.parametrize("word", ["aasssbb", "abc", "", "zzzz", "abbbaab"])
def test_roundtrip(solution, word):
    assert solution.decompress_string(solution.compress_string(word)) == word
