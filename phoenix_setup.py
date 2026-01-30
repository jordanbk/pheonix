"""
Phoenix OpenTelemetry Setup for Claude Code Tracing

This script configures OpenTelemetry to send traces to your local Phoenix instance.
Run this at the start of your Python session to enable tracing.
"""

from phoenix.otel import register

# Register Phoenix with OpenTelemetry
# Phoenix accepts OTLP traces at the /v1/traces endpoint
tracer_provider = register(
    project_name="default",
    endpoint="http://localhost:6006/v1/traces",
    auto_instrument=True
)

print("✓ Phoenix tracing initialized")
print("  Project: default")
print("  Endpoint: http://localhost:6006")
print("  View traces at: http://localhost:6006")
