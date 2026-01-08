from pathlib import Path
from typing import Literal

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.exceptions import HTTPException
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
from litestar.response import Template
from litestar.template.config import TemplateConfig

TEMPLATES_DIR = Path(__file__).parent / "templates"


@get("/", include_in_schema=False)
async def index() -> Template:
    return Template(template_name="index.html")


@get("/calculate", include_in_schema=False)
async def calculate_htmx(
    lhs: float,
    rhs: float,
    operator: Literal["add", "subtract", "multiply", "divide"],
) -> str:
    try:
        result = calculate(lhs, rhs, operator)
        result_str = str(int(result)) if result == int(result) else str(result)
        return f"""{result_str}
<div id="error-message" hx-swap-oob="innerHTML"></div>"""
    except ValueError as e:
        return f"""<span class="text-red-500">Error</span>
<div id="error-message" hx-swap-oob="innerHTML">{e}</div>"""


# Although not used, this shows how you could also expose a REST endpoint.
@get("/api/calculate")
async def calculate_rest(
    lhs: float,
    rhs: float,
    operator: Literal["add", "subtract", "multiply", "divide"],
) -> float:
    try:
        return calculate(lhs, rhs, operator)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


def calculate(
    lhs: float,
    rhs: float,
    operator: Literal["add", "subtract", "multiply", "divide"],
) -> float:
    match operator:
        case "add":
            return lhs + rhs
        case "subtract":
            return lhs - rhs
        case "multiply":
            return lhs * rhs
        case "divide":
            if rhs == 0:
                raise ValueError("Zero division error")
            return lhs / rhs


app = Litestar(
    route_handlers=[index, calculate_htmx, calculate_rest],
    template_config=TemplateConfig(
        directory=TEMPLATES_DIR,
        engine=JinjaTemplateEngine,
    ),
    # If you want to provide a REST API, you can enable API documentation here by including openapi_config.
    # API documentation is available at `/schema`
    openapi_config=OpenAPIConfig(
        title="calculator-api",
        description="Calculator API documentation",
        version="0.1.0",
        render_plugins=[ScalarRenderPlugin()],
    ),
)
