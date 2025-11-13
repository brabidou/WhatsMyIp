# WhatsMyIp

A simple Flask web application that displays your IP address and connection details. Handles proxy scenarios and provides both a web interface and JSON API endpoint.

## Features

- 🌐 Clean, modern web interface
- 🔍 Detects IP address through proxies (X-Forwarded-For, X-Real-IP)
- 📊 Shows connection details (User Agent, Remote Address, etc.)
- 🔌 JSON API endpoint for programmatic access
- 🎨 Responsive design with gradient styling

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

### 1. Clone or download this repository

```bash
cd /path/to/WhatsMyIp
```

### 2. Create a virtual environment

Creating a virtual environment isolates your project dependencies from system-wide Python packages.

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 4. Install dependencies

```bash
pip install flask
```

Or if you have a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated (you should see `(venv)` in your prompt)

2. Run the Flask application:

```bash
python app.py
```

3. Open your browser and navigate to:
   - Web interface: `http://127.0.0.1:5001`
   - API endpoint: `http://127.0.0.1:5001/api/ip`

## API Usage

### Get IP as JSON

```bash
curl http://127.0.0.1:5001/api/ip
```

**Response:**
```json
{
  "ip": "192.168.1.100",
  "x_forwarded_for": "",
  "x_real_ip": "",
  "remote_addr": "192.168.1.100",
  "behind_proxy": false
}
```

## Project Structure

```
WhatsMyIp/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # HTML template with styling
├── venv/                 # Virtual environment (not committed to git)
└── README.md            # This file
```

## Deactivating the Virtual Environment

When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```

## Development

The application runs in debug mode by default, which means:
- Auto-reloads when you make code changes
- Provides detailed error messages
- **Do not use in production!**

For production deployment, use a production WSGI server like Gunicorn or uWSGI.

## Configuration

To change the port, edit `app.py`:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  # Change port here
```

## Troubleshooting

### Port already in use

If you see "Address already in use" error, either:
- Stop the other service using that port
- Change the port in `app.py`
- On macOS, disable AirPlay Receiver (System Preferences → General → AirDrop & Handoff)

### Module not found errors

Make sure you:
1. Activated the virtual environment (`source venv/bin/activate`)
2. Installed Flask (`pip install flask`)

## License

MIT License - feel free to use this project however you'd like!
