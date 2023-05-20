from bs4 import Tag


def safe_parsing(parsing, sibling_search=None) -> str:
    if sibling_search and parsing is not None:
        return safe_parsing(
            parsing.find(
                sibling_search.get('tag'),
                {
                    sibling_search.get('params').get('attr'): 
                    sibling_search.get('params').get('value')
                }
            )
        )
    elif isinstance(parsing, str):
        return parsing
    elif isinstance(parsing, Tag):
        return parsing.text
