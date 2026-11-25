# Object Classifier

Object Classifier is an image classification app. Upload a photo to see its most likely categories and confidence scores.

**Live demo:** [object-classifier-voxq.onrender.com](https://object-classifier-voxq.onrender.com/)

## Features

- Upload JPG, PNG, or WebP images up to 10 MB
- View a ranked list of likely categories
- Choose how many results to display
- Use the responsive Streamlit interface or run the Jupyter notebook

## How classification works

The app resizes the photo and passes the full image to a pretrained image classification model. It returns up to five likely categories from a set of 1,000 classes with confidence scores. This is image classification: it does not locate objects or draw bounding boxes.

## Technology

- **App:** Python and Streamlit
- **Image processing:** Pillow and NumPy
- **Inference:** TensorFlow
- **Notebook:** Jupyter

## Run locally

Python 3.11 is recommended. Clone the repository, create a virtual environment, and install the app dependencies:

```bash
git clone https://github.com/intekhabstatic/object-classifier.git
cd object-classifier
python -m venv .venv
```

Activate the environment, then run:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

```bash
# macOS or Linux
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local address shown by Streamlit, usually <http://localhost:8501>. The first classification may take longer while the pretrained weights are downloaded.

## Run the notebook

Install the optional notebook dependencies and open `mobilenetv2_image_classifier.ipynb` in Jupyter:

```bash
python -m pip install -r requirements-notebook.txt
jupyter notebook
```

The notebook can also be opened in Google Colab. Upload an image when prompted.

## Deploy on Render

The repository includes `render.yaml` for a Render Blueprint. The live demo above is deployed on Render, and changes pushed to the connected GitHub branch can trigger a new deployment.

The service uses Render's free plan. Free instances can sleep when idle and have limited memory, so the first request after inactivity may be slower and large inference workloads may exceed the available memory.

## Credits

The pretrained model and its training data are the work of their original creators and contributors. This project uses their published weights and credits that work; the model name is omitted here as requested.

---

Created by **Intekhab Alam** · [GitHub](https://github.com/intekhabstatic)
