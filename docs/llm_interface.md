
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

The prompt must be a string containing at least one
non-whitespace character.

- A prompt that is not a string raises `TypeError`.
- An empty or whitespace-only prompt raises `ValueError`.
- A successful response must be a string.
- A response with an invalid type raises `TypeError`.

## Error Handling and Fallback

- Invalid prompts raise `TypeError` or `ValueError`
  during input validation.
- Provider implementations should raise `LLMServiceError`
  when generation fails or the service is unavailable.
- Implementations may return a safe fallback message when
  appropriate.
- Implementations must avoid exposing API keys, credentials,
  or sensitive internal provider errors.
- Provider-specific errors should be handled according to
  the application's error-handling policy.

## Future Implementations

Future providers should subclass `LLMService` and implement
`_generate_response(prompt: str) -> str`.

Callers should use `generate_response()` to ensure common
input validation and response-type checking are applied.

The interface does not make actual network calls or require an API key.
