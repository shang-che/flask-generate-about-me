# freeze.py (修正版)
import os
from flask_frozen import Freezer
from app import app, translations

# --- 設定 ---
# 1. 統一定義預設語言，方便未來修改
DEFAULT_LANG = 'zh_tw'

# 2. 設定輸出的靜態檔案要放在名為 'build' 的資料夾中
app.config['FREEZER_DESTINATION'] = 'build'
freezer = Freezer(app)

@freezer.register_generator
def home_url_generator():
    """為 Freezer 指明所有需要生成的動態語言路由"""
    for lang in translations.keys():
        yield 'home', {'lang': lang}

def create_redirect_page():
    """在 build 資料夾中建立一個根目錄的 index.html 來處理重導向"""
    # ▼▼▼ 主要修正點 ▼▼▼
    # 將重導向 URL 從絕對路徑 "/zh_tw/" 改為相對路徑 "zh_tw/"
    # 並使用 f-string 讓它變得動態
    redirect_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Redirecting...</title>
        <link rel="canonical" href="{DEFAULT_LANG}/"/>
        <meta http-equiv="refresh" content="0; url={DEFAULT_LANG}/">
    </head>
    <body>
        <p>If you are not redirected automatically, follow this <a href="{DEFAULT_LANG}/">link</a>.</p>
    </body>
    </html>
    """
    # ▲▲▲ 主要修正點 ▲▲▲
    
    # 確保 build 資料夾存在
    build_dir = app.config['FREEZER_DESTINATION']
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
        
    # 寫入重導向檔案
    with open(os.path.join(build_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(redirect_html)


if __name__ == '__main__':
    print("Generating static site...")
    freezer.freeze() # 執行生成
    create_redirect_page() # 建立重導向頁面
    print("Static site generated in 'build/' folder.")