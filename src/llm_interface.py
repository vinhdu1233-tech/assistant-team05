
"""Define the interface for future LLM service implementations."""

from abc import ABC, abstractmethod


class LLMServiceError(Exception):
    """Raised when an LLM service cannot generate a response."""


class LLMService(ABC):
    """Abstract base class for future LLM service providers."""

    def generate_response(self, prompt: str) -> str:
        """Validate the prompt and generate a response.

        Args:
            prompt: Non-empty user input.

        Returns:
            The generated response as a string.

        Raises:
            TypeError: If the prompt or response has an invalid type.
            ValueError: If the prompt is empty or contains only whitespace.
            LLMServiceError: If generation fails or the service is unavailable.
        """
        if not isinstance(prompt, str):
            raise TypeError("Prompt must be a string.")

        if not prompt.strip():
            raise ValueError("Prompt must not be empty.")

        response = self._generate_response(prompt)

        if not isinstance(response, str):
            raise TypeError("LLM service must return a string.")

        return response

    @abstractmethod
    def _generate_response(self, prompt: str) -> str:
        """Generate a response using a specific LLM provider.

        Subclasses must implement this method.

        Args:
            prompt: A validated, non-empty prompt.

        Returns:
            The generated response as a string.

        Raises:
            LLMServiceError: If generation fails or the service is unavailable.
        """
        raise NotImplementedError(
            "Subclasses must implement _generate_response()."
        )
