# DigitalOcean App Platform Deployment

This guide covers deploying the standalone Docker image to DigitalOcean App Platform.

## Prerequisites

- DigitalOcean account
- GitHub repository connected to DigitalOcean
- Domain name (optional, for custom domain)

## Deployment Methods

### Method 1: Using App Spec (Recommended)

1. **Install doctl CLI** (optional):
   ```bash
   brew install doctl
   doctl auth init
   ```

2. **Create app from spec**:
   ```bash
   doctl apps create --spec .do/app.yaml
   ```

3. **Or update existing app**:
   ```bash
   doctl apps update YOUR_APP_ID --spec .do/app.yaml
   ```

### Method 2: Using DigitalOcean Console

1. Go to [DigitalOcean Apps](https://cloud.digitalocean.com/apps)
2. Click **Create App**
3. Select your GitHub repository
4. Configure:
   - **Source**: Select `Dockerfile.standalone`
   - **HTTP Port**: `80`
   - **Instance Size**: Basic (512MB RAM recommended)
5. Add environment variables:
   - `DOMAIN`: Your app domain (e.g., `yourapp.ondigitalocean.app`)
   - `SYSTEM_LABEL`: Optional label (e.g., `Production`)
6. Click **Create Resources**

### Method 3: Import App Spec

1. Go to DigitalOcean Apps
2. Click **Create App**
3. Choose **Import from GitHub**
4. Select repository
5. Click **Edit App Spec**
6. Paste contents from `.do/app.yaml`
7. Click **Save** and **Create Resources**

## Configuration

### Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `DOMAIN` | Your app domain | No | `yourapp.ondigitalocean.app` |
| `SYSTEM_LABEL` | Display label | No | `Production Server` |

### Custom Domain

1. Go to your app settings
2. Navigate to **Domains**
3. Click **Add Domain**
4. Enter your domain name
5. Update DNS records as instructed

**Note**: DigitalOcean automatically provides HTTPS with Let's Encrypt for custom domains.

## App Spec Configuration

The `.do/app.yaml` file contains:

- **Region**: `nyc` (New York) - change as needed
- **Instance Size**: `basic-xxs` (512MB RAM, $5/month)
- **Auto-deploy**: Enabled on push to `main` branch
- **Health Check**: HTTP check on `/` endpoint

### Available Regions

- `nyc` - New York
- `sfo` - San Francisco
- `ams` - Amsterdam
- `sgp` - Singapore
- `lon` - London
- `fra` - Frankfurt
- `tor` - Toronto
- `blr` - Bangalore

### Instance Sizes

| Size | RAM | vCPU | Price/month |
|------|-----|------|-------------|
| `basic-xxs` | 512MB | 1 | $5 |
| `basic-xs` | 1GB | 1 | $12 |
| `basic-s` | 2GB | 1 | $24 |

## Updating the App

### Auto-Deploy (Default)

Push to your `main` branch and DigitalOcean will automatically rebuild and deploy.

### Manual Deploy

```bash
doctl apps create-deployment YOUR_APP_ID
```

## Monitoring

### View Logs

```bash
# Using doctl
doctl apps logs YOUR_APP_ID --type run

# Or in console
# Go to App → Runtime Logs
```

### Metrics

View in DigitalOcean console:
- CPU usage
- Memory usage
- Request count
- Response times

## Troubleshooting

### Build Fails

1. Check build logs in console
2. Verify `Dockerfile.standalone` is in repository root
3. Ensure all required files are present

### App Won't Start

1. Check runtime logs
2. Verify HTTP port is set to `80`
3. Check environment variables are set correctly

### Health Check Fails

1. Verify app responds on `/` endpoint
2. Check health check settings in app spec
3. Increase `initial_delay_seconds` if needed

## Cost Optimization

- Start with `basic-xxs` ($5/month)
- Enable auto-scaling only if needed
- Use single instance for low traffic
- Monitor usage in billing section

## HTTPS/SSL

- **Automatic**: DigitalOcean provides free SSL for `.ondigitalocean.app` domains
- **Custom Domain**: Free Let's Encrypt SSL automatically configured
- **No configuration needed**: SSL is handled by the platform

## Example URLs

After deployment, your app will be available at:

- Default: `https://yourapp-xxxxx.ondigitalocean.app`
- Custom: `https://yourdomain.com` (if configured)

## Additional Resources

- [DigitalOcean App Platform Docs](https://docs.digitalocean.com/products/app-platform/)
- [App Spec Reference](https://docs.digitalocean.com/products/app-platform/reference/app-spec/)
- [doctl CLI Reference](https://docs.digitalocean.com/reference/doctl/)
