import logging

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, UnidentifiedImageError

st.set_page_config(
    page_title="Object Classifier",
    page_icon=":material/image_search:",
    layout="centered",
)


@st.cache_resource(show_spinner="Preparing the image classifier…")
def load_model():
    return tf.keras.applications.MobileNetV2(
        weights="imagenet",
        include_top=True,
        input_shape=(224, 224, 3),
    )


def classify_image(image: Image.Image, top_k: int):
    resized = image.resize((224, 224))
    image_array = np.asarray(resized, dtype=np.float32)
    batch = np.expand_dims(image_array, axis=0)
    batch = tf.keras.applications.mobilenet_v2.preprocess_input(batch)
    predictions = load_model().predict(batch, verbose=0)
    return tf.keras.applications.mobilenet_v2.decode_predictions(
        predictions, top=top_k
    )[0]


st.markdown(":material/image_search: &nbsp; **IMAGE CLASSIFICATION**")
st.title("Object Classifier")
st.write(
    "Upload a photo to see what it most likely contains. "
    "You’ll get a ranked list of possible categories with confidence scores."
)
st.caption(
    "This demo classifies the full image. It does not draw boxes around objects."
)

with st.container(border=True):
    st.subheader("Choose a photo")
    uploaded_file = st.file_uploader(
        "Upload a JPG, PNG, or WebP image",
        type=["jpg", "jpeg", "png", "webp"],
        max_upload_size=10,
        help="For best results, use a clear image under 10 MB.",
    )

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
    except (UnidentifiedImageError, OSError):
        st.error("That file could not be opened as an image. Try a JPG or PNG file.")
    else:
        with st.container(border=True):
            st.image(image, caption=uploaded_file.name, width="stretch")
            with st.form("classification_form", border=False):
                top_k = st.slider(
                    "Show possible matches",
                    min_value=1,
                    max_value=5,
                    value=3,
                )
                submitted = st.form_submit_button(
                    "Classify image",
                    type="primary",
                    icon=":material/search:",
                    width="stretch",
                )

        if submitted:
            try:
                with st.spinner("Analyzing your image…"):
                    results = classify_image(image, top_k)
            except Exception:
                logging.exception("Image classification failed")
                st.error("The classifier could not process this image. Please try again.")
            else:
                st.subheader("Results")
                best_label = results[0][1].replace("_", " ").title()
                best_score = float(results[0][2])

                with st.container(border=True):
                    st.metric(
                        "Top match",
                        best_label,
                        delta=f"{best_score:.1%} confidence",
                        delta_color="off",
                    )

                for rank, (_, label, score) in enumerate(results, start=1):
                    clean_label = label.replace("_", " ").title()
                    st.write(f"**{rank}. {clean_label}** · {score:.1%}")
                    st.progress(float(score))

                st.caption(
                    "Confidence scores show how strongly the model favors each category; "
                    "they are not guarantees of accuracy."
                )
else:
    st.info("Add a photo above to get started.", icon=":material/upload:")

with st.expander("About this demo", icon=":material/info:"):
    st.write(
        "The classifier uses pretrained image-recognition weights and returns "
        "categories for the whole photo. It has not been fine-tuned on a custom dataset."
    )
    st.caption("Credit is given in the project README to the original model creators and data contributors.")

