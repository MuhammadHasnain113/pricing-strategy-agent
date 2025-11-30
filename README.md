# Pricing Strategy Agent

Small reproducible ML project for pricing strategy experiments.

## Repo structure (key files)
- [requirements.txt](requirements.txt)
- [scripts/download_data.sh](scripts/download_data.sh)
- [scripts/preprocess.py](scripts/preprocess.py)
- [scripts/train_model.py](scripts/train_model.py)
- [src/main.py](src/main.py)
- [src/config.py](src/config.py)
- [src/agent/engine.py](src/agent/engine.py)
- [src/agent/model_interface.py](src/agent/model_interface.py)
- [src/agent/preprocessing.py](src/agent/preprocessing.py)
- [src/models/](src/models/)
- [data/raw/](data/raw/)
- [data/processed/](data/processed/)
- [notebooks/01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb)
- [notebooks/02_model_experiments.ipynb](notebooks/02_model_experiments.ipynb)
- [docker/Dockerfile](docker/Dockerfile)
- [docker/docker-compose.yml](docker/docker-compose.yml)
- [tests/](tests/)

## Prerequisites
- Python 3.8+
- pip
- (optional) Docker & docker-compose

## Quick start — Local (venv)
1. Create and activate a virtual environment
   - macOS / Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment
   - Copy `.env` if needed and add secrets/config values:
     ```
     cp .env.example .env
     ```
     (If `.env.example` is not present, create `.env` manually based on [src/config.py](src/config.py).)

4. Download raw data:
   ```
   bash scripts/download_data.sh
   ```
   or run the downloader script directly: `python scripts/download_data.sh`

5. Preprocess data:
   ```
   python scripts/preprocess.py --input data/raw --output data/processed
   ```
   See [src/agent/preprocessing.py](src/agent/preprocessing.py) for preprocessing details.

6. Train model:
   ```
   python scripts/train_model.py --data data/processed --output models/
   ```
   See [scripts/train_model.py](scripts/train_model.py) and [src/agent/model_interface.py](src/agent/model_interface.py).

7. Run the application / experiment entrypoint:
   ```
   python src/main.py
   ```
   Or:
   ```
   python -m src.main
   ```
   See [src/main.py](src/main.py) and [src/config.py](src/config.py).

## Quick start — Docker
Build and run with docker-compose:
```
docker-compose -f docker/docker-compose.yml up --build
```
See [docker/Dockerfile](docker/Dockerfile) and [docker/docker-compose.yml](docker/docker-compose.yml).

## Deployment — Railway

This project is configured for deployment on Railway. The deployment uses either:
- **Dockerfile** (in `docker/Dockerfile`) - Railway will automatically detect and use this
- **Procfile** - Alternative method if Dockerfile is not used

### Railway Deployment Steps:

1. **Connect your repository to Railway:**
   - Go to [Railway](https://railway.app)
   - Create a new project
   - Connect your GitHub/GitLab repository

2. **Configure the deployment:**
   - Railway will automatically detect the Dockerfile in `docker/Dockerfile`
   - Or it will use the `Procfile` if Dockerfile is not found
   - The `railway.json` file provides additional configuration

3. **Environment Variables (if needed):**
   - Add any required environment variables in Railway's dashboard
   - The app will use default values if not set

4. **Deploy:**
   - Railway will automatically build and deploy on every push to your main branch
   - Check the deployment logs in Railway dashboard for any issues

### Notes:
- The app will automatically bind to the `PORT` environment variable provided by Railway
- The model file (`src/models/psa_model_v1.pkl`) is optional - the app will work with a fallback if the model is not present
- Health check endpoint is available at `/health`

## Notebooks
Interactive exploration and model experiments:
- [notebooks/01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb)
- [notebooks/02_model_experiments.ipynb](notebooks/02_model_experiments.ipynb)

## Running tests
Run unit tests:
```
pytest -q
```
Tests live in [tests/](tests/).

## Contributing
- Follow existing code style in `src/`.
- Add tests for new features under [tests/](tests/).
- Update documentation in `docs/` when behavior changes (see [docs/architecture.md](docs/architecture.md), [docs/api_spec.md](docs/api_spec.md), [docs/user_guide.md](docs/user_guide.md)).

## Notes
- Data and models are ignored by `.gitignore` — see [.gitignore](.gitignore).
- Configuration values live in [src/config.py](src/config.py). Adjust or extend as needed.

If anything fails, check logs/output in the integrated terminal or output pane of your IDE and verify environment variables in `.env`.
