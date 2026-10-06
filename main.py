from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse

app = FastAPI(
    title="Smart Dark Mode Generator API",
    description="API to generate zero-conflict dark mode CSS compatible with YouTube Regular Videos & Shorts.",
    version="2.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Zero-Conflict Dark CSS (Supports Regular YouTube + YouTube Shorts)
SMART_DARK_CSS = """
/* 1. Global Page Background & Text */
html, body {
    background-color: #0f0f0f !important;
    color: #f1f1f1 !important;
}

/* 2. Color structural containers EXCEPT video players, YouTube players & SHORTS components */
body *:not(video):not(iframe):not(canvas):not(svg):not(path):not(img):not(.html5-video-player):not(.html5-main-video):not(.video-stream):not(#movie_player):not([class*="player"]):not([id*="player"]):not([class*="ytp-"]):not(ytd-shorts):not(ytd-reel-video-renderer):not([class*="shorts"]):not([id*="shorts"]):not([class*="overlay"]) {
    background-color: #0f0f0f !important;
    color: #f1f1f1 !important;
    border-color: #272727 !important;
}

/* 3. Link Colors */
a, a * {
    color: #3ea6ff !important;
}

/* 4. Form inputs */
input, textarea, select, button {
    background-color: #212121 !important;
    color: #ffffff !important;
    border: 1px solid #3d3d3d !important;
}

/* 5. Complete immunity for Video Elements, YouTube Regular Players & YouTube SHORTS Overlays */
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
[class*="ytp-"],
ytd-shorts,
ytd-shorts *,
ytd-reel-video-renderer,
ytd-reel-video-renderer *,
[class*="shorts-player"],
[class*="reel-player"] {
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
        "mode": "shorts_and_video_compatible",
        "css": SMART_DARK_CSS.strip()
    }
