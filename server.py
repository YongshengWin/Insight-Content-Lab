import http.server
import socketserver
import os

PORT = 8000

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # 简化日志输出，方便观察数据请求
        print(f"[Server] {args[0]} {args[1]} -> {args[2]}")

if __name__ == "__main__":
    print(f"--- 灵感捕捉计划：本地部署预览 ---")
    if not os.path.exists("data.csv"):
        print("警告: 目录下未发现 data.csv，请确保文件存在")
    
    with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
        print(f"地址: http://localhost:{PORT}")
        httpd.serve_forever()
