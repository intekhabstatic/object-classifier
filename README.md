# MobileNetV2 Image Classifier

A small image classification project with a Streamlit front end and a Jupyter notebook. It uses the ImageNet-pretrained MobileNetV2 model, so no training step is required. The first run downloads the pretrained weights.

## Features

- Upload JPG, PNG, or WebP images in a browser interface
- See the top 1–10 ImageNet predictions with confidence scores
- Explore the same model workflow in `mobilenetv2_image_classifier.ipynb`

## Run locally

Python 3.10 or 3.11 is recommended.

```bash
git clone https://github.com/intekhabstatic/object-detection.git
cd object-detection
python -m venv .venv
```

Activate the environment, then install dependencies and launch the app:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Notebook

Start Jupyter with `jupyter notebook` and open `mobilenetv2_image_classifier.ipynb`. Upload or enter the path to an image when prompted. In Google Colab, the notebook uses the Colab upload widget automatically.

## Model notes

Despite the repository name, this version performs whole-image classification. It does not locate objects or draw bounding boxes.

The project uses `tf.keras.applications.MobileNetV2(weights="imagenet", include_top=True)`. It predicts 1,000 ImageNet classes and is intended as a general-purpose demo. It has not been fine-tuned on a custom dataset. Predictions can be inaccurate for specialized domains.




