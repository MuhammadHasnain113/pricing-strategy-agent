# Railway Deployment Guide

This project is now configured for Railway deployment. Here's what has been set up:

## Files Created/Updated for Railway:

1. **Dockerfile** (root level) - Main Docker configuration
2. **Procfile** - Alternative deployment method (if Dockerfile isn't used)
3. **railway.json** - Railway-specific configuration
4. **.dockerignore** - Excludes unnecessary files from Docker build
5. **src/main.py** - Updated to support PORT environment variable

## Quick Deployment Steps:

### Option 1: Using Railway Dashboard (Recommended)

1. Go to [railway.app](https://railway.app) and sign in
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will automatically:
   - Detect the Dockerfile
   - Build the container
   - Deploy the application

### Option 2: Using Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

## Important Notes:

- **PORT Environment Variable**: Railway automatically sets the `PORT` environment variable. The app is configured to use it.
- **Model File**: The app works without a trained model (uses fallback). If you want to use a trained model, ensure `src/models/psa_model_v1.pkl` exists in your repository or is added during build.
- **Health Check**: Once deployed, check `/health` endpoint to verify the app is running.
- **API Endpoints**:
  - Health: `/health`
  - Pricing API: `/api/v1/pricing/recommend`

## Troubleshooting:

If deployment fails:

1. **Check Railway logs**: View deployment logs in Railway dashboard
2. **Verify Dockerfile**: Ensure Dockerfile is in the root directory
3. **Check requirements.txt**: All dependencies should be listed
4. **Port binding**: Ensure the app binds to `0.0.0.0` and uses `$PORT` environment variable

## Environment Variables (Optional):

If you need to set environment variables in Railway:
1. Go to your project settings in Railway
2. Navigate to "Variables" tab
3. Add any required environment variables

The app will work with default values if no environment variables are set.

