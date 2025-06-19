from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>My First Web Page</title>
        </head>
        <body style="background-color:#f0f8ff;">
            <h1>こんにちは！これは私のホームページです 🌟</h1>
            <p>FastAPI から HTML を返しています。</p>
            <ul>
                <li>自己紹介</li>
                <li>趣味</li>
                <li>連絡先</li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present: str):
    message = f"🎁 わあ！『{present}』をありがとう！あなたに特製クッキーをプレゼントします 🍪"
    return JSONResponse(content={"response": message})