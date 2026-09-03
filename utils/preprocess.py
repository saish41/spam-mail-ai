import re
from bs4 import BeautifulSoup


def clean_email(text):
    """
    Clean email text while preserving useful spam-related information.
    """

    text = str(text)

    # Remove HTML tags
    text = BeautifulSoup(
        text,
        "html.parser"
    ).get_text(" ")

    # Convert to lowercase
    text = text.lower()

    # Replace URLs with token
    text = re.sub(
        r"https?://\S+|www\.\S+",
        " URL ",
        text
    )

    # Replace email addresses
    text = re.sub(
        r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
        " EMAIL ",
        text
    )

    # Replace numbers
    text = re.sub(
        r"\b\d+\b",
        " NUMBER ",
        text
    )

    # Remove excessive whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()