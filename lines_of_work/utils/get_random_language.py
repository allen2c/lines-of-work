import random
from typing import Optional

from google_language_support import LanguageCodes


def get_random_language() -> Optional["LanguageCodes"]:
    return random.choice(
        [
            LanguageCodes.ENGLISH,
            LanguageCodes.CHINESE_SIMPLIFIED,
            LanguageCodes.CHINESE_TRADITIONAL,
            LanguageCodes.HINDI,
            LanguageCodes.SPANISH,
            LanguageCodes.FRENCH,
            LanguageCodes.BENGALI,
            LanguageCodes.RUSSIAN,
            LanguageCodes.PORTUGUESE,
            LanguageCodes.INDONESIAN,
            LanguageCodes.GERMAN,
            LanguageCodes.JAPANESE,
            LanguageCodes.MARATHI,
            LanguageCodes.TELUGU,
            LanguageCodes.TURKISH,
            LanguageCodes.TAMIL,
            LanguageCodes.VIETNAMESE,
            LanguageCodes.THAI,
        ]
    )
