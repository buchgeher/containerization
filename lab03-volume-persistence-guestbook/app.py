import http.server
import urllib.parse
import os
import datetime

DATA_FILE = "/data/entries.txt"

class GuestbookHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        entries_html = ""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                for line in reversed(lines):
                    entries_html += f"<li style='padding:6px 0; border-bottom:1px solid #334155; color:#cbd5e1;'>{line}</li>"

        if not entries_html:
            entries_html = "<li style='color:#64748b; font-style:italic;'>No entries yet. Leave the first note!</li>"

        html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Docker Volume Guestbook</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0f172a; color: #f8fafc;
      max-width: 650px; margin: 40px auto; padding: 20px;
    }}
    .box {{
      background: #1e293b; padding: 25px; border-radius: 12px;
      border: 1px solid #334155; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    h2 {{ color: #38bdf8; margin-top: 0; }}
    input[type=text] {{
      width: 70%; padding: 10px; border-radius: 6px;
      border: 1px solid #475569; background: #0f172a; color: #f8fafc; font-size: 14px;
    }}
    button {{
      padding: 10px 18px; border-radius: 6px; border: none;
      background: #10b981; color: white; font-weight: bold; cursor: pointer;
    }}
    button:hover {{ background: #059669; }}
    ul {{ list-style: none; padding-left: 0; margin-top: 20px; }}
    .badge {{
      background: #0284c7; color: white; font-size: 11px;
      padding: 3px 8px; border-radius: 4px; font-mono;
    }}
  </style>
</head>
<body>
  <div class="box">
    <h2>📖 Persistent Guestbook Demo</h2>
    <p style="color:#94a3b8; font-size:13px;">
      Data file target: <code class="badge">{DATA_FILE}</code> (Backed by a Docker Named Volume)
    </p>

    <form method="POST" action="/submit">
      <input type="text" name="msg" placeholder="Type a message..." required autofocus>
      <button type="submit">Submit Entry</button>
    </form>

    <h3 style="color:#e2e8f0; margin-top:30px;">Saved Messages:</h3>
    <ul>
      {entries_html}
    </ul>
  </div>
</body>
</html>"""
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(length).decode("utf-8")
        parsed = urllib.parse.parse_qs(post_data)
        msg = parsed.get("msg", [""])[0].strip()

        if msg:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry_line = f"[{timestamp}] {msg}"
            os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
            with open(DATA_FILE, "a", encoding="utf-8") as f:
                f.write(entry_line + "\n")

        # Redirect back to homepage
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

if __name__ == "__main__":
    port = 8000
    server = http.server.HTTPServer(("", port), GuestbookHandler)
    print(f"Guestbook server listening on http://0.0.0.0:{port}...")
    server.serve_forever()
