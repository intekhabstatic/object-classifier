# Object Classifier

A simple image classification demo with a Streamlit browser interface and a Jupyter notebook. Upload a photo to view likely categories and their confidence scores.

> This app classifies the full image. It does not locate objects or draw bounding boxes.

## Run the app on your computer

Clone the private GitHub repository and install the app dependencies:

```bash
git clone https://github.com/intekhabstatic/object-classifier.git
cd object-classifier
python -m venv .venv
```

Activate the environment, then start the app:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

```bash
# macOS or Linux
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local address Streamlit prints, usually `http://localhost:8501`. The first classification may take longer while the pretrained weights are downloaded.

## Deploy on Render

The repository includes `render.yaml` for a free Render web service. To deploy:

1. Sign in to Render and connect your GitHub account, granting access to this private repository.
2. In Render, create a **Blueprint** and select `intekhabstatic/object-classifier`.
3. Apply the blueprint. Render reads `render.yaml`, installs the dependencies, and starts the app.
4. Open the `onrender.com` address shown on the service page after the deploy succeeds.

Free Render web services sleep after 15 minutes without traffic, so the first visit after idle can take about a minute to load. The free plan also has limited memory; if the service restarts while loading the image model, a higher-memory plan may be needed. No paid plan is configured by this project.

## Jupyter notebook

To run the notebook locally, install its optional dependencies with `pip install -r requirements-notebook.txt`, then open `mobilenetv2_image_classifier.ipynb` in Jupyter. In Google Colab, upload an image when prompted.

## Credits

Credit goes to the original creators of the pretrained image-recognition model and to the contributors who curated its training data. Their work makes this demonstration possible. This project uses their pretrained work and does not claim authorship of it.

