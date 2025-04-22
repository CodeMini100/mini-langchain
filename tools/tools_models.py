from typing import List, Optional
from pydantic import BaseModel


class SearchQuery(BaseModel):
    """
    Model representing the input for a search query.
    """

    query: str
    limit: int = 10
    offset: int = 0
    # TODO: Add any additional fields as needed


class SearchResultItem(BaseModel):
    """
    Model representing a single search result item.
    """

    title: str
    url: str
    description: Optional[str] = None
    # TODO: Add any additional fields as needed


class SearchResults(BaseModel):
    """
    Model representing the output of search results.
    """

    results: List[SearchResultItem]
    total_results: int
    # TODO: Add any additional fields as needed