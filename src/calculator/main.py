from pathlib import Path
from typing import Literal

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

TEMPLATES_DIR = Path(__file__).parent / "templates"


@get("/")
async def index() -> Template:
    return Template(template_name="index.html")


@get("/api/calculate")
async def calculate(
    a: float,
    b: float,
    operator: Literal["add", "subtract", "multiply", "divide"],
) -> str:
    match operator:
        case "add":
            result = a + b
        case "subtract":
            result = a - b
        case "multiply":
            result = a * b
        case "divide":
            if b == 0:
                return "Error: Division by zero"
            result = a / b

    if result == int(result):
        return str(int(result))
    return str(result)


app = Litestar(
    route_handlers=[index, calculate],
    template_config=TemplateConfig(
        directory=TEMPLATES_DIR,
        engine=JinjaTemplateEngine,
    ),
)
