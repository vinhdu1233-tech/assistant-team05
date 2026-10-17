
# LLM Service Interface

## Purpose

This document defines the interface for future Large Language
Model (LLM) integrations in the Smart Virtual Assistant.

## Interface

The interface is defined in `src/llm_interface.py`.

- `LLMService`: abstract base class for LLM providers.
- `generate_response(prompt: str) -> str`: generates a text response.
- `LLMServiceError`: represents service-related failures.

## Input and Output

The prompt must be a non-empty string. A successful implementation
returns a string containing the generated response.

## Error Handling and Fallback

- Reject empty prompts with `ValueError`.
- Raise `LLMServiceError` when generation fails or the service is
  unavailable.
- Implementations may return a safe fallback message when appropriate.
- Do not expose API keys, credentials, or internal provider errors.

## Future Implementations

Future providers should subclass `LLMService`, implement
`generate_response`, and handle provider-specific errors.

The interface does not make actual network calls or require an API key.
