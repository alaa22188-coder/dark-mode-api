from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse

app = FastAPI(
    title="Smart Dark Mode Generator API",
    description="API to generate clean CSS rules for turning websites into dark mode.",
    version="1.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clean Direct Dark Mode CSS without filter conflicts
SMART_DARK_CSS = """
/* Force dark background on main containers */
html, body, div, section, article, main, header, footer, nav, aside {
    background-color: #121212 !important;
    color: #ffffff !important;
}

/* Ensure ALL text elements are clear bright white */
p, span, h1, h2, h3, h4, h5, h6, li, td, th, label, strong, em, b, i {
    color: #ffffff !important;
    background-color: transparent !important;
}

/* Links readable in light blue/cyan */
a, a * {
    color: #64b5f6 !important;
    background-color: transparent !important;
}

/* Inputs & Form controls */
input, textarea, select, button {
    background-color: #1e1e1e !important;
    color: #ffffff !important;
    border: 1px solid #444444 !important;
}

/* Preserve original media without modifications */
img, video, iframe, canvas, svg {
    opacity: 0.9 !important;
}
"""

@app.get("/generate-dark-css")
def get_dark_css(url: str = Query(..., description="Target website URL")):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path

    return {
        "status": "success",
        "domain": domain,
        "mode": "clean_dark",
        "css": SMART_DARK_CSS.strip()
    }
