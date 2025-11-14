from unittest import TestCase
from unittest.mock import patch, MagicMock
import requests

def fetch_page():
    """Simple function that fetches a page and handles errors."""
    try:
        quote_page = "https://www.drive.com.au/showrooms/mitsubish/asx/#review/"
        r = requests.get(quote_page)
        r.raise_for_status()
        page = r.text
        # print("Type of the variable 'page':", page.__class__.__name__)
        # print(f"Page Retrieved. Request Status: {r.status_code}, Page Size: {len(page)}")
        return page
    except Exception as e:
        # print(f"Error while processing response: {e}")
        return e

class WebscrapeTestCase(TestCase):
    # 🔹 Test for the failure case (simulated exception)
    def test_fetch_page_error(self):
        with patch("requests.get", side_effect=requests.exceptions.ConnectionError("Simulated failure")):
            result = fetch_page()
            print("Result in error test:", result)
            self.assertEqual(str(result), "Simulated failure")

    # 🔹 Test for the happy path (successful request)
    def test_fetch_page_success(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html>Mock Page</html>"
        mock_response.raise_for_status.return_value = None  # no error

        with patch("requests.get", return_value=mock_response):
            result = fetch_page()
            self.assertEqual(mock_response.status_code, 200)
            assert result == "<html>Mock Page</html>"
