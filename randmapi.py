from dataclasses import asdict

import requests

from models import ApiParameters, ApiResponse

BASE_URL = "https://rickandmortyapi.com/api"

def get_endpoint(endpoint: str, params: ApiParameters) -> ApiResponse:
    """ Return `ApiRespons` from Rick and Morty `endpoint`"""
    response = requests.get(f"{BASE_URL}/{endpoint}", params=asdict(params))
    response.raise_for_status()
    response = ApiResponse(**response.json())
    return response