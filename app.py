from flask import Flask, render_template, url_for, redirect, abort
import datetime
import json

app = Flask(__name__)

try:
    with open('data.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
except FileNotFoundError:
    print("錯誤：找不到 data.json 檔案。")
    translations = {}
except json.JSONDecodeError:
    print("錯誤：data.json 檔案格式不正確。")
    translations = {}


@app.route('/')
def index():
    # 網站根目錄預設重導向到繁體中文版
    return redirect(url_for('home', lang='zh_tw'))

@app.route('/<lang>/')
def home(lang):
    """主頁路由，根據 URL 中的 lang 參數來渲染對應語言的履歷"""
    if lang not in translations:
        abort(404)

    # 從讀取的資料中，複製一份該語言的內容，避免修改到原始資料
    resume_data = translations[lang].copy()
    
    # 動態地加入 copyright_year
    resume_data['copyright_year'] = datetime.date.today().year

    return render_template("index.html", data=resume_data, lang=lang)

if __name__ == "__main__":
    app.run(debug=True)