from waitress import serve
from InventoryManagement.wsgi import application  # Replace "myproject" with your Django project name

serve(application, host='0.0.0.0', port=8000)