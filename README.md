# WhatsMyIp

A simple Flask web application that displays your IP address and connection details. Handles proxy scenarios and provides both a web interface and JSON API endpoint.

## Features

- 🌐 Clean, modern web interface
- 🔍 Detects IP address through proxies (X-Forwarded-For, X-Real-IP)
- 📊 Shows connection details (User Agent, Remote Address, etc.)
- 🔌 JSON API endpoint for programmatic access
- 🎨 Responsive design with gradient styling

## Prerequisites

### For Local Development
- Python 3.7 or higher
- pip (Python package installer)

### For Docker
- Docker installed on your system
- (Optional) Docker Compose

## Quick Start with Docker

### Pull from GitHub Container Registry

```bash
docker pull ghcr.io/brabidou/whatsmyip:latest
docker run -p 5001:5001 ghcr.io/brabidou/whatsmyip:latest
```

Then visit `http://localhost:5001`

### Build locally

```bash
docker build -t whatsmyip .
docker run -p 5001:5001 whatsmyip
```

## Installation (Local Development)

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
├── .github/
│   └── workflows/
│       └── docker-publish.yml  # GitHub Actions workflow
├── app.py                      # Main Flask application
├── templates/
│   └── index.html             # HTML template with styling
├── Dockerfile                  # Docker image definition
├── .dockerignore              # Docker build exclusions
├── requirements.txt           # Python dependencies
├── venv/                      # Virtual environment (not committed to git)
└── README.md                  # This file
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

## Docker Deployment

### GitHub Container Registry

This project automatically builds and publishes Docker images to GitHub Container Registry (GHCR) on every push to the main branch.

**Workflow triggers:**
- Push to `main` or `master` branch
- New version tags (e.g., `v1.0.0`)
- Manual workflow dispatch

**Image tags:**
- `latest` - Latest build from main branch
- `main` - Latest build from main branch
- `v1.0.0` - Specific version tags
- `sha-<commit>` - Specific commit builds

### Setting up GitHub Actions

The workflow is already configured in `.github/workflows/docker-publish.yml`. To enable it:

1. Push your code to GitHub
2. The workflow will automatically run on push to main/master
3. Images will be published to `ghcr.io/<your-username>/whatsmyip`

**Note:** The `GITHUB_TOKEN` is automatically provided by GitHub Actions, no additional secrets needed.

### Making the image public

By default, GHCR images are private. To make it public:

1. Go to your GitHub profile → Packages
2. Find the `whatsmyip` package
3. Click "Package settings"
4. Scroll down and click "Change visibility"
5. Select "Public"

### Running the published image

```bash
# Pull and run latest version
docker pull ghcr.io/<your-username>/whatsmyip:latest
docker run -d -p 5001:5001 ghcr.io/<your-username>/whatsmyip:latest

# Run specific version
docker run -d -p 5001:5001 ghcr.io/<your-username>/whatsmyip:v1.0.0
```

## License

MIT License - feel free to use this project however you'd like!
