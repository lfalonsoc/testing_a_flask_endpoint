from typing import Any
from unittest import TestCase

from app.app import app


class BaseTest(TestCase):
    def setUp(self) -> None:
        app.testing = True
        self.app: Any = app.test_client
