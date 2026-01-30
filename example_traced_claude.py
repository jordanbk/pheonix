"""
Example: Tracing Claude API calls with Phoenix

This script demonstrates how to trace Claude API interactions using Phoenix.
Make sure Phoenix is running at http://localhost:6006 before running this.
"""

# Import and initialize Phoenix tracing
from phoenix.otel import register

tracer_provider = register(
    project_name="default",
    endpoint="http://localhost:6006/v1/traces",
    auto_instrument=True  # Auto-instruments Anthropic SDK and other supported libraries
)

print("✓ Phoenix tracing enabled\n")

# Now use the Anthropic SDK - all calls will be automatically traced
from anthropic import Anthropic

# Initialize the client
client = Anthropic()  # Uses ANTHROPIC_API_KEY environment variable

# Make a traced API call
print("Making a traced Claude API call...")
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is Phoenix observability?"}
    ]
)

print(f"\nClaude's response: {message.content[0].text}")
print("\n✓ Check Phoenix at http://localhost:6006 to see the trace!")
