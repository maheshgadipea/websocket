#!/bin/bash

# Run the Gunicorn command via the Flask CLI
exec python /application/application/gunicorn_cli.py gunicorn
