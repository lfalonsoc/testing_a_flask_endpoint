import json

from typing import Any
from app.tests.system.test_base import BaseTest

from app.app import app


class TestHome(BaseTest):
    def test_home(self) -> None:
        with app.test_client() as c:
            resp: Any = c.get("/")

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(
                json.loads(resp.get_data()),
                {"message": "Hello, World!"},
            )
