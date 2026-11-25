import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(page_title="Image Classifier", page_icon="🖼️", layout="centered")

@st.cache_resource(show_spinner="Loading MobileNetV2 ImageNet model…")
def load_model():
    return tf.keras.applications.MobileNetV2(
        weights="imagenet", include_top=True, input_shape=(224, 224, 3)
    )

st.title("🖼️ Image Classifier")
st.write("Upload an image to classify it with pretrained **MobileNetV2**. The model predicts among the 1,000 ImageNet classes.")

uploaded = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "webp"])
top_k = st.slider("Number of predictions", min_value=1, max_value=10, value=5)

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)
    if st.button("Classify image", type="primary"):
        with st.spinner("Analyzing image…"):
            model = load_model()
            resized = image.resize((224, 224))
            array = np.asarray(resized, dtype=np.float32)
            batch = np.expand_dims(array, axis=0)
            batch = tf.keras.applications.mobilenet_v2.preprocess_input(batch)
            scores = model.predict(batch, verbose=0)
            results = tf.keras.applications.mobilenet_v2.decode_predictions(scores, top=top_k)[0]
        st.subheader("Predictions")
        for rank, (_, label, score) in enumerate(results, start=1):
            st.write(f"**{rank}. {label.replace('_', ' ').title()}** — {score:.1%}")
            st.progress(float(score))
        st.caption("Scores are model confidence scores; they are not a guarantee of correctness.")
else:
    st.info("Upload a JPG, PNG, or WebP image to get started.")

