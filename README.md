# Image Recognition Demo

A small image recognition project with a browser interface and a Jupyter notebook. Upload an image to see the model’s five most likely ImageNet categories.

> **Note:** This project classifies the whole image. It does not locate objects or draw bounding boxes, despite the repository name.

## Open the project

The GitHub repository is [intekhabstatic/object-detection](https://github.com/intekhabstatic/object-detection). It is private, so sign in to GitHub with an account that has access.

The browser app is not hosted online. To run it on your computer, clone the repository and start the app:

```bash
git clone https://github.com/intekhabstatic/object-detection.git
cd object-detection
python -m venv .venv
```

Activate the environment, then install the requirements and launch the interface:

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

Open the local address printed by Streamlit, usually `http://localhost:8501`. The first run downloads the pretrained weights.

## Use the notebook

Open `mobilenetv2_image_classifier.ipynb` in Jupyter and run its cells. In Google Colab, upload an image when prompted; in local Jupyter, enter the image file path.

## Credits

Credit goes to the original creators of the pretrained image-recognition model and to the contributors who curated its training data. Their work makes this demonstration possible. This project uses their pretrained work and does not claim authorship of it.

