from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse

app = FastAPI(
    title="Smart Dark Mode Generator API",
    description="API to generate bulletproof dark mode CSS compatible with YouTube and media players.",
    version="1.3.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Bulletproof Dark CSS - Zero Video Interference
SMART_DARK_CSS = """
/* 1. Global background tint without affecting video overlays */
html {
    background-color: #0f0f0f !important;
}

/* 2. Target text and background directly on structural components */
body, header, nav, footer, main, article, section, aside, div, p, span, a, li, td, th, h1, h2, h3, h4, h5, h6 {
    background-color: #0f0f0f !important;
    color: #f1f1f1 !important;
    border-color: #272727 !important;
}

/* 3. Link color optimization */
a, a * {
    color: #3ea6ff !important;
}

/* 4. Complete exclusion for videos, thumbnails, and media containers */
video, iframe, canvas, svg, img,
.html5-video-player, .html5-main-video, .video-stream,
[class*="player"], [id*="player"], [class*="video"], [id*="video"] {
    background-color: transparent !important;
    filter: none !important;
    mix-blend-mode: normal !important;
}

/* 5. Inputs & Buttons */
input, textarea, select, button {
    background-color: #212121 !important;
    color: #ffffff !important;
    border: 1px solid #3d3d3d !important;
}
"""

@app.get("/generate-dark-css")
def get_dark_css(url: str = Query(..., description="Target website URL")):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path

    return {
        "status": "success",
        "domain": domain,
        "mode": "bulletproof_media_dark",
        "css": SMART_DARK_CSS.strip()
    }
