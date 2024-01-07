import pytest

from python_cicd_demo.main import main


def test_main():
    try:
        main()
    except Exception:
        pytest.fail("main() raised an exception")
