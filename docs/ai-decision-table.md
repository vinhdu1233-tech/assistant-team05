
# Rule-Based Logic vs AI-Assisted Decisions

## Goal

Explain when the Smart Virtual Assistant should use deterministic
rule-based logic and when AI assistance may be appropriate.

## Decision Table

| User request | Approach | Reason |
|---|---|---|
| What time is my meeting? | Rule-based | Retrieves a known calendar value. |
| Convert 5 km to meters | Rule-based | Uses a deterministic calculation. |
| What tasks are due today? | Rule-based | Filters tasks using dates and status. |
| Summarize a long meeting transcript | AI-assisted | Produces a concise summary of unstructured text. |
| Rewrite an email politely | AI-assisted | Requires flexible language generation. |
| Classify feedback by sentiment | AI-assisted | Interprets natural language and context. |
| Is my appointment at 10:00? | Rule-based | Checks a specific stored appointment. |

## Reasons for Classification

Rule-based logic is preferred when the answer can be obtained
through exact lookup, explicit conditions, or deterministic calculation.
It is predictable, easy to test, and generally inexpensive.

AI assistance is useful for language-heavy tasks such as summarization,
rewriting, and interpreting unstructured user input. Its outputs may
vary and can contain errors, so important results should be verified.

## Accuracy

Rule-based systems are reliable when their rules and input data are
correct, but they may not handle unexpected language or situations well.

AI systems can interpret flexible requests but may generate incorrect
or unsupported information. High-impact decisions should not rely on
unverified AI output.

## Privacy

Only send information necessary for an AI task to the model provider.
Sensitive data should be minimized or removed where possible.
Provider retention and processing policies must be reviewed before
integrating an external service.

Rule-based processing may keep data local, depending on the system
architecture and data sources.

## Implementation Complexity

Rule-based logic is straightforward for stable, clearly defined tasks,
but complex rule sets can become difficult to maintain.

AI integration requires model configuration, error handling,
testing, latency management, and potentially API costs.

## Recommendations

1. Prefer rule-based logic for calculations, exact lookups, and
   predictable workflows.
2. Use AI assistance for summarization, rewriting, and flexible
   language interpretation.
3. Validate AI outputs when accuracy matters.
4. Apply privacy controls before sending data to external providers.
5. Use a hybrid approach when deterministic checks can validate
   AI-generated results.
