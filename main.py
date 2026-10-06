from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse

app = FastAPI(
    title="Smart Dark Mode Generator API",
    description="API to generate CSS rules with YouTube & video player compatibility.",
    version="1.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Smart Dark CSS with Video Players & YouTube Exclusion
SMART_DARK_CSS = """
/* 1. Force dark background on general layout containers */
html, body, header, footer, nav, aside {
    background-color: #121212 !important;
    color: #ffffff !important;
}

/* 2. Apply dark background to general divs BUT exclude video containers */
div:not([class*="player"]):not([class*="video"]):not([id*="player"]):not([id*="video"]),
section, article, main {
    background-color: #121212 !important;
    color: #ffffff !important;
}

/* 3. Ensure all text and links are readable white & light blue */
p, span, h1, h2, h3, h4, h5, h6, li, td, th, label, strong, em, b, i {
    color: #ffffff !important;
}

a, a * {
    color: #64b5f6 !important;
}

/* 4. Form Controls */
input, textarea, select, button {
    background-color: #1e1e1e !important;
    color: #ffffff !important;
    border: 1px solid #444444 !important;
}

/* 5. PROTECT VIDEO PLAYERS & MEDIA (Crucial for YouTube, Vimeo, etc.) */
video, iframe, canvas, svg,
.html5-video-player, .html5-main-video, .video-stream,
[class*="player"], [id*="player"] {
    background-color: transparent !important;
    opacity: 1 !important;
    filter: none !important;
}
"""

@app.get("/generate-dark-css")
def get_dark_css(url: str = Query(..., description="Target website URL")):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path

    return {
        "status": "success",
        "domain": domain,
        "mode": "video_compatible_dark",
        "css": SMART_DARK_CSS.strip()
    }
