# Litestar HTMX Example

A simple calculator application built with Litestar and HTMX.

## Overview

This project demonstrates how to build an interactive web UI using Python's [Litestar](https://litestar.dev/) framework combined with [HTMX](https://htmx.org/), enabling partial page updates without full page reloads.

### Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Partial page updates with HTMX
- REST API endpoint (`/api/calculate`)
- OpenAPI documentation (`/schema`)

## Requirements

* [uv](https://docs.astral.sh/uv/): Python package manager
* [Task](https://taskfile.dev/): Task runner

You can use the provided [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) to automatically set up the development environment with all requirements.

## Tech Stack

### Application
- **[Litestar](https://litestar.dev/)**: High-performance Python web framework
- **[HTMX](https://htmx.org/)**: Library for AJAX requests directly from HTML
- **[Jinja2](https://jinja.palletsprojects.com/)**: Template engine
- **[Pydantic](https://docs.pydantic.dev/)**: Data validation and settings management
- **[DaisyUI](https://daisyui.com/) + [Tailwind CSS](https://tailwindcss.com/)**: UI styling
- **[structlog](https://www.structlog.org/)**: Structured logging for better observability

### Development Tools
- **[uv](https://docs.astral.sh/uv/)**: Fast Python package manager
- **[Ruff](https://docs.astral.sh/ruff/)**: Fast Python linter and formatter
- **[Pyright](https://microsoft.github.io/pyright/)**: Static type checker
- **[pytest](https://docs.pytest.org/)**: Testing framework
- **[pip-audit](https://github.com/pypa/pip-audit)**: Security vulnerability scanner
- **[Task](https://taskfile.dev/)**: Task runner

## Setup

Install dependencies:

```sh
uv sync
```

## Usage

### Start the Development Server

```sh
task dev
```

Open http://localhost:8000 in your browser to access the calculator app.

### Available Commands

```sh
# Start development server (with hot reload)
task dev

# Check code quality (typecheck + lint)
task check

# Format code
task format

# Run tests
task test

# Audit dependencies for vulnerabilities
task audit
```

List all available commands:

```sh
task --list-all
```

## API

### REST API

The calculator is also available as a REST API:

```sh
curl "http://localhost:8000/api/calculate?lhs=10&rhs=5&operator=add"
# 15.0
```

Available operators: `add`, `subtract`, `multiply`, `divide`

### API Documentation

After starting the development server, visit http://localhost:8000/schema to view the OpenAPI documentation (Scalar).

## License

MIT-0
