# Online Exam System — v1, v2, v3

A small Flask-based Online Exam project for the lab requirement.

## Features by version
- **v1**: Displays an MCQ quiz and accepts answers.
- **v2**: Adds automatic scoring and displays the score.
- **v3**: Adds a dedicated result screen with final score and answer review.

## Ports
- v1: http://localhost:5001
- v2: http://localhost:5002
- v3: http://localhost:5003

## Run locally
1. Open this folder in VS Code.
2. Open Terminal > New Terminal.
3. Create a virtual environment (optional but recommended):
   - Windows: `py -m venv .venv`
   - Activate: `.\.venv\Scripts\Activate.ps1`
4. Install dependencies: `py -m pip install -r requirements.txt`
5. Start one version:
   - `py app_v1.py`
   - `py app_v2.py`
   - `py app_v3.py`
6. Open the matching localhost URL above.

If `py` is unavailable, use `python` instead.

## Docker
Build and run each image:
```powershell
docker build -f Dockerfile.v1 -t YOUR_DOCKERHUB_USERNAME/online-exam:v1 .
docker run --rm -p 5001:5000 YOUR_DOCKERHUB_USERNAME/online-exam:v1

docker build -f Dockerfile.v2 -t YOUR_DOCKERHUB_USERNAME/online-exam:v2 .
docker run --rm -p 5002:5000 YOUR_DOCKERHUB_USERNAME/online-exam:v2

docker build -f Dockerfile.v3 -t YOUR_DOCKERHUB_USERNAME/online-exam:v3 .
docker run --rm -p 5003:5000 YOUR_DOCKERHUB_USERNAME/online-exam:v3
```
Replace `YOUR_DOCKERHUB_USERNAME` with your Docker Hub username. Stop a running container with Ctrl+C, or use `docker ps` and `docker stop CONTAINER_ID`.

## Git branches
A straightforward way to show separate versions is to use three branches:
```bash
git init
git add .
git commit -m "Add Online Exam v1 MCQ quiz"
git branch v1
git checkout -b v2
git add .
git commit -m "Add v2 automatic scoring"
git checkout -b v3
git add .
git commit -m "Add v3 final result page"
```
For a clean history, create the v1 commit first, then add the v2 and v3 changes before making each later commit. See `STEP_BY_STEP_GUIDE.pdf` for a careful sequence.

## Kubernetes
The manifests in `k8s/` create three deployments and services. They use the Docker Hub images tagged `v1`, `v2`, and `v3` and expose them locally on ports 5001, 5002, and 5003. Edit the image names in each YAML file first.
```powershell
kubectl apply -f k8s/
kubectl get deployments
kubectl get services
```
With Docker Desktop Kubernetes enabled, use `http://localhost:5001`, `:5002`, and `:5003`. If your Kubernetes setup does not expose NodePort on localhost, use `kubectl port-forward service/online-exam-v1 5001:5000` in one terminal, and similarly for v2 and v3 in separate terminals.

## Jenkins
`Jenkinsfile` is a starter pipeline. It checks out the repository, installs dependencies, and runs basic syntax checks. Docker build/push stages are included as an example and require Jenkins to have Docker access and valid Docker Hub credentials configured under the credential ID `dockerhub-creds`. Do not put passwords or tokens directly in this file.
