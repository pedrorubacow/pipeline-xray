import pytest

from pipeline_xray import main


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()

    captured = capsys.readouterr()

    assert captured.out == "Hello from pipeline-xray!\n"
