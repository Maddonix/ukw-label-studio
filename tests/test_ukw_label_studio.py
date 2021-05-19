
from ukw_label_studio.cli import main


def test_main():
    assert main([]) == 0
