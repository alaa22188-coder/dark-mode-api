from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse

app = FastAPI(
    title="Smart Dark Mode Generator API",
    description="API to generate CSS rules for turning websites into dark mode for Chrome Extensions.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Improved Dark CSS: White readable text & comfortable contrast
SMART_DARK_CSS = """
html {
    filter: invert(90%) hue-rotate(180deg) !important;
    background-color: #121212 !important;
}

/* Invert back media elements to preserve natural colors */
img, video, iframe, canvas, svg, [style*="background-image"] {
    filter: invert(100%) hue-rotate(180deg) !important;
}

/* Fix text and links color for maximum readability */
body, p, span, h1, h2, h3, h4, h5, h6, li, td, th {
    color: #e0e0e0 !important;
}

a, a * {
    color: #ffffff !important;
    text-decoration: underline !important;
}

input, textarea, select, button {
    background-color: #1e1e1e !important;
    color: #ffffff !important;
    border-color: #444444 !important;
}
"""

@app.get("/generate-dark-css")
def get_dark_css(url: str = Query(..., description="Target website URL")):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path

    return {
        "status": "success",
        "domain": domain,
        "mode": "smart_dark",
        "css": SMART_DARK_CSS.strip()
    }
