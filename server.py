"""
Plenitudo MCP Server — Template
Replace the example tool with your own logic.
"""

import json
import logging
import os
import sys

from mcp.server.fastmcp import FastMCP
from typing import Annotated
from pydantic import Field

from config import LOG_FILE, LOG_LEVEL
from x402 import PRICE_USDC, WALLET_ADDRESS, is_proof_used, mark_proof_used, payment_required_response, verify_payment

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
os.makedirs(os.path.dirname(os.path.abspath(LOG_FILE)), exist_ok=True)

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stderr),
    ],
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------
mcp = FastMCP(
    "my-mcp-server",
    instructions="Describe what your MCP server does here.",
    host="0.0.0.0",
    port=int(os.getenv("PORT", "8000")),
)


# ---------------------------------------------------------------------------
# Example tool — replace with your logic
# ---------------------------------------------------------------------------

@mcp.tool()
def hello_world(
    name: Annotated[str, Field(description="Name to greet.")],
    payment_proof: Annotated[str | None, Field(description="x402 payment proof (Base tx hash).")] = None,
) -> str:
    """Example tool. Replace this with your actual functionality."""
    if not payment_proof:
        return json.dumps(payment_required_response("hello_world"))
    if is_proof_used(payment_proof):
        return json.dumps({"ok": False, "error": "Payment proof already used"})
    ok, err = verify_payment(payment_proof, PRICE_USDC, WALLET_ADDRESS)
    if not ok:
        return json.dumps({"ok": False, "error": f"Payment verification failed: {err}"})
    mark_proof_used(payment_proof, "hello_world")

    result = f"Hello, {name}!"
    logger.info("hello_world called for %s", name)
    return json.dumps({"ok": True, "result": result})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if "--stdio" in sys.argv:
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http")
