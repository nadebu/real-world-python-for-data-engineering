from typing import List

from models import ApiParameters, CharacterSchema
from randmapi import get_endpoint

ENDPOINT = "character"

def get_all_paginated_results(
        endpoint: str, pages: int, params: ApiParameters
) -> List[CharacterSchema]:
    all_results = []
    for page in range(1, pages + 1):
        params.page = page
        print(f"Calling page {page}...")
        response = get_endpoint(endpoint, params)
        all_results.extend(response.results)
    return all_results

if __name__ == "__main__":
    params = ApiParameters()
    initial_response = get_endpoint(ENDPOINT, params)
    results = get_all_paginated_results(ENDPOINT, initial_response.info.pages, params)
    print(f"Total records: {len(results)}")
