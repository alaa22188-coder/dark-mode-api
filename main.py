from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse

app = FastAPI(
    title="Smart Dark Mode Generator API",
    description="API to generate CSS rules for turning websites into dark mode for Chrome Extensions.",
    version="1.0.0"
)

# تفعيل CORS ليتمكن متصفح كروم من استدعاء الـ API بدون مشاكل أمنية
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# كود الـ CSS الذكي لإنشاء الدارك مود
SMART_DARK_CSS = """
/* Smart Dark Mode Filter */
html {
    filter: invert(90%) hue-rotate(180deg) !important;
    background-color: #121212 !important;
}

/* الاستثناءات: استعادة الألوان الطبيعية للصور، الفيديوهات، والوسائط */
img, video, iframe, canvas, svg, [style*="background-image"] {
    filter: invert(100%) hue-rotate(180deg) !important;
}

/* تحسين تباديل الألوان للشاشات والمدخلات */
input, textarea, select, button {
    background-color: #1e1e1e !important;
    color: #e0e0e0 !important;
    border-color: #333333 !important;
}

/* تعديل ألوان الروابط لتبدو واضحة على الخلفية الداكنة */
a {
    color: #8ab4f8 !important;
}
"""

@app.get("/generate-dark-css")
def get_dark_css(url: str = Query(..., description="Target website URL")):
    """
    يستقبل رابط الموقع ويرجع كود الـ CSS الجاهز للحقن المباشر في إضافة الكروم.
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path

    return {
        "status": "success",
        "domain": domain,
        "mode": "smart_dark",
        "css": SMART_DARK_CSS.strip()
    }