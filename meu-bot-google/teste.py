from google.oauth2 import service_account
from googleapiclient.discovery import build

# Nome do seu arquivo (ajuste se necessário)
KEY_FILE = r'C:\Users\danil\OneDrive\Área de Trabalho\Pessoal\Documentos\n8n-docker\meu-bot-google\credenciais.json'

# Escopos (permissões de leitura/escrita)
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/calendar.readonly'
]

# Autenticação
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)

# Teste Google Sheets
try:
    service_sheets = build('sheets', 'v4', credentials=creds)
    print("✅ Sucesso: Conectado ao Google Sheets!")
except Exception as e:
    print(f"❌ Erro no Sheets: {e}")

# Teste Google Calendar
try:
    service_calendar = build('calendar', 'v3', credentials=creds)
    print("✅ Sucesso: Conectado ao Google Calendar!")
except Exception as e:
    print(f"❌ Erro no Calendar: {e}")