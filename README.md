# 簡易物流倉儲管理系統 (WMS)


## 後端開發環境
- Python (使用 `uv` 管理)
- 框架: FastAPI

## 快速啟動
1. 安裝 uv (若尚未安裝): `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. 同步依賴: `uv sync`
3. 啟動伺服器: `uv run uvicorn app.main:app --reload`

## 測試帳號
- **帳號**: `admin`
- **密碼**: `admin`

## API 文件
啟動後訪問: `http://127.0.0.1:8000/docs`