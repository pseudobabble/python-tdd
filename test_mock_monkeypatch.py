#!/usr/bin/env python
from typing import Any
from unittest.mock import MagicMock


class ApiLogger:

    def __init__(self, logger: Any) -> None:
        self.logger = logger

    def log(self, message: str) -> str:
        return self.logger.log(message)



def test__create_logger():
    logger = ApiLogger(MagicMock())

    assert isinstance(logger, ApiLogger)

def test__log(monkeypatch):

    mock_logger = MagicMock()
    mock_logger.log = MagicMock(return_value='MOCKED')

    api_logger = ApiLogger(mock_logger)
    assert api_logger.log('log message') == 'MOCKED'

    def get_foo(self, some_arg) -> str:
        return 'foo'

    api_logger = ApiLogger(mock_logger)
    monkeypatch.setattr(ApiLogger, 'log', get_foo)
    assert api_logger.log('anything') == 'foo'

