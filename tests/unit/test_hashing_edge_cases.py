import xxhash

from aiswarm.utils import hashing


def test_hash_string_empty():
    """Hashing an empty string should match xxhash of empty bytes."""
    expected = xxhash.xxh64(b"").hexdigest()
    assert hashing.hash_string("") == expected


def test_hash_bytes_empty():
    """Hashing empty bytes should produce the same digest as the empty string case."""
    expected = xxhash.xxh64(b"").hexdigest()
    assert hashing.hash_bytes(b"") == expected


def test_hash_string_vs_bytes_equivalence():
    """hash_string and hash_bytes should be equivalent for the same data content."""
    sample = "Zymis hashing test"
    expected = xxhash.xxh64(sample.encode()).hexdigest()
    assert hashing.hash_string(sample) == expected
    assert hashing.hash_bytes(sample.encode()) == expected


def test_hash_large_payload():
    """Hash a large payload (1 MiB) to ensure deterministic output and no overflow errors."""
    large_data = b"a" * (1024 * 1024)  # 1 MiB of repetitive data
    expected = xxhash.xxh64(large_data).hexdigest()
    # The utility provides both string and bytes interfaces; use bytes here.
    assert hashing.hash_bytes(large_data) == expected
