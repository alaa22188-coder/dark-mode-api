from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse

app = FastAPI(
    title="Smart Dark Mode Generator API",
    description="API to generate zero-conflict dark mode CSS for video sites like YouTube.",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Zero-Conflict Dark CSS (Strictly Excludes Video Players & Shadow DOM Trees)
SMART_DARK_CSS = """
/* 1. Global Page Background & Default Text */
html, body {
    background-color: #0f0f0f !important;
    color: #f1f1f1 !important;
}

/* 2. Color structural containers EXCEPT anything inside a video player or YouTube player */
body *:not(video):not(iframe):not(canvas):not(svg):not(path):not(img):not(.html5-video-player):not(.html5-main-video):not(.video-stream):not(#movie_player):not([class*="player"]):not([id*="player"]):not([class*="ytp-"]) {
    background-color: #0f0f0f !important;
    color: #f1f1f1 !important;
    border-color: #272727 !important;
}

/* 3. Readable Link Color */
a, a * {
    color: #3ea6ff !important;
}

/* 4. Form inputs */
input, textarea, select, button {
    background-color: #212121 !important;
    color: #ffffff !important;
    border: 1px solid #3d3d3d !important;
}

/* 5. Force absolute neutrality on ALL video elements and YouTube overlays */
video, 
iframe, 
canvas, 
svg, 
img,
.html5-video-player, 
.html5-video-player *, 
#movie_player, 
#movie_player *,
.video-stream,
[class*="ytp-"] {
    background-color: transparent !important;
    filter: none !important;
    mix-blend-mode: normal !important;
    opacity: 1 !important;
}
"""

@app.get("/generate-dark-css")
def get_dark_css(url: str = Query(..., description="Target website URL")):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path

    return {
        "status": "success",
        "domain": domain,
        "mode": "zero_conflict_dark",
        "css": SMART_DARK_CSS.strip()
    }
