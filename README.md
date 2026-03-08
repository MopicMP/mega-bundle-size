# mega-bundle-size

> Mega check js bundle size and limits

[![PyPI version](https://badge.fury.io/py/mega-bundle-size.svg)](https://pypi.org/project/mega-bundle-size/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)

## Installation

```bash
pip install mega-bundle-size
```

## Quick Start

```python
from mega_bundle_size import size

# Basic usage
result = size("your input here")
print(result)
```

## Features

- Simple, clean API with type hints
- Zero dependencies (pure Python)
- Python 3.8+ compatible
- Fully tested
- Lightweight (< 5KB)

## API Reference

### `size(input)`

Main utility function.

**Parameters:**
- `input` — The input data to process

**Returns:** Processed result

### `batch(inputs)`

Process multiple inputs at once.

**Parameters:**
- `inputs` — List of inputs

**Returns:** List of results

## Examples

```python
from mega_bundle_size import size

# Example 1: Basic usage
result = size("Hello World")

# Example 2: Batch processing
from mega_bundle_size import batch
results = batch(["item1", "item2", "item3"])
```

## Running Tests

```bash
pip install pytest
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

### Learn More

**Want to build tools like this?** Check out the
**[Website From Scratch](https://gumroad.com/l/website-from-scratch)** course — it teaches you
step-by-step how to create useful Python utilities from scratch,
with real-world projects and best practices.

*Built with skills from [Website From Scratch](https://gumroad.com/l/website-from-scratch)*
