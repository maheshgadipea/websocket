# gunicorn.py
import os

bind = "0.0.0.0:5000"  # Listen on all IP addresses, port 5000
workers = 4 # Number of worker processes
worker_class = "eventlet"  # You can change this to "gevent" or "aiohttp" if needed
timeout = 600  # Timeout for worker processes
loglevel = "info"  # Log level for Gunicorn logs
chdir = os.path.dirname(os.path.abspath(__file__)) 