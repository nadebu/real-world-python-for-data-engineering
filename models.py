from dataclasses import dataclass
from typing import Dict, List, Literal, Optional


@dataclass
class CharacterSchema:
    id: int
    name: str
    status: Literal['Alive', 'Dead', 'Unknown']
    species: str
    type: str
    gender: Literal["Female", "Male", "Genderless", "Unknown"]
    origin: Dict[str, str]
    location: Dict[str, str]
    image: str
    episode: List[str]
    url: str
    created: str

@dataclass
class ApiInfo:
    count: int
    pages: int
    next: Optional[str]
    prev: Optional[str]

@dataclass
class ApiResponse:
    info: ApiInfo
    results: List[CharacterSchema]

    def __post_init__(self):
        self.info = ApiInfo(**self.info)
        self.results = [CharacterSchema(**item) for item in self.results]