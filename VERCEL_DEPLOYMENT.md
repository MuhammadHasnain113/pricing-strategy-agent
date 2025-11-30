# Vercel Deployment Guide

This project is configured for Vercel deployment as a serverless FastAPI application.

## Files Created/Updated for Vercel:

1. **vercel.json** - Vercel deployment configuration
2. **api/index.py** - Serverless function entry point
3. **.vercelignore** - Files to exclude from Vercel deployment
4. **README.md** - Updated with Vercel deployment instructions

## Quick Deployment Steps:

### Option 1: Using Vercel Dashboard (Recommended)

1. **Go to Vercel:**
   - Visit [vercel.com](https://vercel.com)
   - Sign in with your GitHub account

2. **Create New Project:**
   - Click "New Project"
   - Import your repository: `MuhammadHasnain113/pricing-strategy-agent`
   - Or search for your repository

3. **Configure Project:**
   - Framework Preset: Select "Other" or leave as default
   - Root Directory: Leave as default (`.`)
   - Build Command: Leave empty (Vercel will auto-detect)
   - Output Directory: Leave empty
   - Install Command: `pip install -r requirements.txt`

4. **Environment Variables (Optional):**
   - Add any required environment variables in the project settings
   - Go to Settings → Environment Variables
   - The app will work with default values if not set

5. **Deploy:**
   - Click "Deploy"
   - Wait for the build to complete
   - Your app will be live at a Vercel URL

### Option 2: Using Vercel CLI

```bash
# Install Vercel CLI globally
npm install -g vercel

# Login to Vercel
vercel login

# Deploy (from project root)
vercel

# For production deployment
vercel --prod
```

## Project Structure for Vercel:

```
pricing-strategy-agent/
├── api/
│   ├── __init__.py
│   └── index.py          # Vercel serverless function entry point
├── src/
│   ├── main.py          # FastAPI application
│   └── ...
├── vercel.json          # Vercel configuration
├── .vercelignore        # Files to exclude
└── requirements.txt     # Python dependencies
```

## Important Notes:

- **Serverless Functions**: The app runs as a serverless function on Vercel
- **Python Runtime**: Vercel uses Python 3.x (automatically detected)
- **Model File**: The app works without a trained model (uses fallback). If you want to use a trained model, ensure `src/models/psa_model_v1.pkl` exists in your repository
- **API Endpoints**:
  - Health: `/health`
  - Pricing API: `/api/v1/pricing/recommend`
- **Cold Starts**: Serverless functions may have cold start delays on first request

## Troubleshooting:

### Build Failures:

1. **Check Vercel Logs**: View deployment logs in Vercel dashboard
2. **Verify requirements.txt**: Ensure all dependencies are listed
3. **Check Python Version**: Vercel should auto-detect, but you can specify in `vercel.json` if needed
4. **Verify vercel.json**: Ensure the configuration is correct

### Runtime Errors:

1. **Check Function Logs**: View runtime logs in Vercel dashboard
2. **Verify Imports**: Ensure all Python imports are correct
3. **Check Path Issues**: The `PYTHONPATH` is set in `vercel.json`

### Common Issues:

- **Module Not Found**: Ensure all dependencies are in `requirements.txt`
- **Import Errors**: Check that `PYTHONPATH` is correctly set in `vercel.json`
- **Timeout**: Vercel has execution time limits for serverless functions

## Environment Variables:

To set environment variables in Vercel:

1. Go to your project in Vercel dashboard
2. Navigate to Settings → Environment Variables
3. Add your variables (e.g., API keys, database URLs)
4. Redeploy your application

## Continuous Deployment:

Once connected to GitHub, Vercel will automatically:
- Deploy on every push to the main branch
- Create preview deployments for pull requests
- Show deployment status in GitHub

## API Testing:

After deployment, test your endpoints:

```bash
# Health check
curl https://your-app.vercel.app/health

# Pricing recommendation
curl -X POST https://your-app.vercel.app/api/v1/pricing/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": "test-123",
    "cost_price": 100.0,
    "competitor_price": 120.0,
    "demand_level": "High",
    "min_margin": 0.1
  }'
```

## Differences from Railway:

- **Serverless vs Container**: Vercel uses serverless functions, Railway uses containers
- **Cold Starts**: Vercel functions may have cold starts, Railway containers are always running
- **Scaling**: Vercel auto-scales, Railway requires manual scaling configuration
- **Cost**: Vercel has a generous free tier for serverless functions

