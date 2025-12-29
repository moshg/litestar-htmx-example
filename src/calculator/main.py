from pathlib import Path
from typing import Literal

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
from litestar.response import Template
from litestar.template.config import TemplateConfig

TEMPLATES_DIR = Path(__file__).parent / "templates"


@get("/", include_in_schema=False)
async def index() -> Template:
    return Template(template_name="index.html")


@get("/api/calculate")
async def calculate(
    lhs: float,
    rhs: float,
    operator: Literal["add", "subtract", "multiply", "divide"],
) -> str:
    match operator:
        case "add":
            result = lhs + rhs
        case "subtract":
            result = lhs - rhs
        case "multiply":
            result = lhs * rhs
        case "divide":
            if rhs == 0:
                return """<span class="text-red-500">Error</span>
<div id="error-message" hx-swap-oob="innerHTML">Zero division error</div>"""
            result = lhs / rhs

    result_str = str(int(result)) if result == int(result) else str(result)

    return f"""{result_str}
<div id="error-message" hx-swap-oob="innerHTML"></div>"""


app = Litestar(
    route_handlers=[index, calculate],
    template_config=TemplateConfig(
        directory=TEMPLATES_DIR,
        engine=JinjaTemplateEngine,
    ),
    openapi_config=OpenAPIConfig(
        title="calculator-api",
        description="Calculator API documentation",
        version="0.1.0",
        render_plugins=[ScalarRenderPlugin()],
    ),
)
