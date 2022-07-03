from markdown import markdown
from bs4 import BeautifulSoup


def convert_markdown_text_to_plaintext(text: str) -> str:
    """
    Converts markdown text to plaintext
    :param text:
    :return:
    """
    html = markdown(text)
    if html is None:
        return ''

    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()
