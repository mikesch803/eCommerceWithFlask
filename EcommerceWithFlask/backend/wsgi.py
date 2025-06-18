from app import app  # or whatever your main app file is named

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=7777)
