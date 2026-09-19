"""
Dummy Calculator MCP server -- a minimal example for deploying to Horizon.

Horizon just needs an importable module exposing a FastMCP instance, so
this file has no FastAPI/uvicorn wrapping at all -- the entrypoint is
simply "dummy.py:mcp".

Local test:
    uv run fastmcp dev dummy.py

Horizon deploy:
    1. Push this file (+ pyproject.toml / uv.lock with a "fastmcp" dependency)
       to its own clean repo.
    2. Sign in at https://horizon.prefect.io with that GitHub account.
    3. Select the repository.
    4. Configure:
         Server name: calculator
         Entrypoint:  dummy.py:mcp
"""
from fastmcp import FastMCP

mcp = FastMCP("Calculator")


@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b


@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the difference."""
    return a - b


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the product."""
    return a * b


@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide a by b and return the quotient. Raises an error if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool
def power(base: float, exponent: float) -> float:
    """Raise base to exponent and return the result."""
    return base ** exponent


if __name__ == "__main__":
    mcp.run()
