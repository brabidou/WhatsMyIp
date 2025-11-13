# Standalone Docker Image with Automatic HTTPS

This is an all-in-one Docker image with **Caddy** reverse proxy that automatically handles HTTPS with Let's Encrypt.

## Why Caddy?

- **Automatic HTTPS**: Just set a domain, Caddy handles the rest
- **Auto-renewal**: SSL certificates renew automatically
- **Simple**: Minimal configuration needed
- **Built-in**: Everything in one container

## Build

```bash
docker build -f Dockerfile.standalone -t whatsmyip-standalone .
```

## Usage

### Option 1: HTTP Only (localhost/testing)

```bash
docker run -p 80:80 whatsmyip-standalone
```

Access at: `http://localhost`

### Option 2: Automatic HTTPS (production)

```bash
docker run -p 80:80 -p 443:443 \
  -e DOMAIN=ip.example.com \
  -e SYSTEM_LABEL="Production Server" \
  -v caddy-data:/data/caddy \
  whatsmyip-standalone
```

**Requirements:**
- Domain must point to your server's IP
- Ports 80 and 443 must be accessible from the internet
- That's it! Caddy automatically gets SSL certificates

Access at: `https://ip.example.com`

### Option 3: With Email for Let's Encrypt Notifications

```bash
docker run -p 80:80 -p 443:443 \
  -e DOMAIN=ip.example.com \
  -e ACME_EMAIL=admin@example.com \
  -e SYSTEM_LABEL="My Server" \
  -v caddy-data:/data/caddy \
  whatsmyip-standalone
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DOMAIN` | Your domain name | `localhost` |
| `SYSTEM_LABEL` | Label shown in app | `""` |

## How It Works

1. **Flask** runs on port 5050 (internal)
2. **Caddy** listens on ports 80/443 and proxies to Flask
3. When `DOMAIN` is set to a real domain, Caddy automatically:
   - Obtains SSL certificate from Let's Encrypt
   - Redirects HTTP to HTTPS
   - Renews certificates before expiry

## Persistent SSL Certificates

The `-v caddy-data:/data/caddy` volume stores SSL certificates so they persist across container restarts.

## Examples

### Development (no HTTPS)
```bash
docker run -p 80:80 whatsmyip-standalone
# Access: http://localhost
```

### Production (automatic HTTPS)
```bash
docker run -d --name whatsmyip \
  -p 80:80 -p 443:443 \
  -e DOMAIN=ip.mysite.com \
  -e SYSTEM_LABEL="US-East Server" \
  -v caddy-data:/data/caddy \
  --restart unless-stopped \
  whatsmyip-standalone

# Access: https://ip.mysite.com
```

## Troubleshooting

### SSL Certificate Not Working

1. **Check DNS**: Domain must point to your server
   ```bash
   nslookup ip.example.com
   ```

2. **Check Ports**: 80 and 443 must be accessible
   ```bash
   curl -I http://ip.example.com
   ```

3. **Check Logs**:
   ```bash
   docker logs <container-id>
   ```

### View Logs

```bash
# Follow logs
docker logs -f <container-id>

# Last 100 lines
docker logs --tail 100 <container-id>
```

## Comparison

| Method | Containers | Complexity | HTTPS Setup |
|--------|-----------|------------|-------------|
| **Standalone** | 1 | Simplest | Automatic |
| Docker Compose | 2 | Medium | Manual config |
| Manual | 1 | Complex | Manual |

## Notes

- Caddy automatically handles HTTP to HTTPS redirect when using a real domain
- For `localhost`, only HTTP is used (no SSL)
- SSL certificates are stored in `/data/caddy` - mount as volume for persistence
- First certificate request may take 10-30 seconds
