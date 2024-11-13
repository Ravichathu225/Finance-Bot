from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('BUBBLE_API_KEY')
api_base_url = os.getenv('BUBBLE_API_BASE_URL')  # Load a base URL from .env for flexibility

class DBreaderTool(BaseTool):
    """
    A tool that interacts with Bubble.io's API to perform data operations.
    This tool fetches data from or sends data to Bubble.io, allowing integration
    with other workflows as needed by the Agent.
    """


    bubble_api_url: str = Field(
        ..., description=api_base_url
    )
    api_key: str = Field(
        ..., description=api_key
    )

    def run(self):
        """
        The implementation of the run method where the tool's main functionality is executed.
        This method performs an HTTP request to Bubble.io based on the provided fields.
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Example GET request to fetch data from Bubble.io
        response = requests.get(
            f"{self.bubble_api_url}",
            headers=headers
        )

        if response.status_code == 200:
            # Process and return data if the request is successful
            data = response.json()
            return f"Data retrieved successfully: {data}"
        else:
            # Return an error message if the request fails
            return f"Error {response.status_code}: {response.text}"