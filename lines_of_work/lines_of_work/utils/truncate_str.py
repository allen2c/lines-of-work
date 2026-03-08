import logging
from typing import Optional

import tiktoken

logger = logging.getLogger(__name__)


def truncate_str(
    s: str,
    *,
    max_tokens: int,
    encoding: Optional["tiktoken.Encoding"] = None,
) -> str:
    encoding = encoding or tiktoken.get_encoding("o200k_base")

    tokens = encoding.encode(s)
    if len(tokens) <= max_tokens:
        return s
    logger.warning(
        f"Truncating string from {len(tokens)} tokens to {max_tokens} tokens"
    )
    return encoding.decode(tokens[:max_tokens]) + "... [truncated]"
