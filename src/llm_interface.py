
"""Define the interface for future LLM service implementations."""

from abc import ABC, abstractmethod


class LLMServiceError(Exception):
    """Raised when an LLM service cannot generate a response."""


class LLMService(ABC):
    """Abstract interface for a Large Language Model service."""

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate a text response for the given prompt.

        Args:
            prompt: Non-empty user input.

        Returns:
            The generated response as a string.

        Raises:
            ValueError: If the prompt is empty.
            LLMServiceError: If generation fails or the service is unavailable.

        Implementations should handle provider errors and either raise
        LLMServiceError or return a safe fallback message.
        """
        if not prompt or not prompt.strip():
            raise ValueError("Prompt must not be empty.")

        raise NotImplementedError(
            "Subclasses must implement generate_response()."
        )
