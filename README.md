# Phoenix Tracing Setup for Claude Code

This repository contains Phoenix skills and tracing setup for observing Claude interactions.

## Prerequisites

- Phoenix running at http://localhost:6006 (Docker container)
- Python 3.10+
- Virtual environment activated

## Quick Start

### 1. Install Dependencies

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set Your Anthropic API Key

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### 3. Run the Example

```bash
python example_traced_claude.py
```

This will make a traced Claude API call. View the traces at http://localhost:6006

## Using Phoenix Tracing in Your Code

Import and initialize Phoenix at the start of your Python scripts:

```python
from phoenix.otel import register

tracer_provider = register(
    project_name="default",
    endpoint="http://localhost:6006",
    auto_instrument=True
)
```

The `auto_instrument=True` setting automatically traces:
- Anthropic SDK calls
- OpenAI SDK calls
- LangChain operations
- LlamaIndex operations
- And more...

## Phoenix Skills

This repository includes custom Claude Code skills for:
- **phoenix-cli**: Phoenix CLI commands and operations
- **phoenix-evals**: Evaluation and testing workflows
- **phoenix-tracing**: Tracing and observability patterns

## Project Structure

```
.
├── .agents/skills/        # Phoenix skills for Claude Code
├── .claude/skills/        # Symlinks to agent skills
├── phoenix_setup.py       # Phoenix initialization script
├── example_traced_claude.py  # Example traced Claude call
├── requirements.txt       # Python dependencies
└── venv/                  # Virtual environment (not in git)
```

## Viewing Traces

1. Ensure Phoenix is running: http://localhost:6006
2. Run your traced code
3. Open Phoenix UI to see traces, spans, and metrics

## Resources

- [Phoenix Documentation](https://docs.arize.com/phoenix)
- [Anthropic API Documentation](https://docs.anthropic.com)
