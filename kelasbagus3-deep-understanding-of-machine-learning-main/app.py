import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import sklearn


# # st.title('Hello Streamlit 👋')

# # st.write('Ini adalah aplikasi Streamlit pertama kita!')

# # name = st.text_input('Masukkan nama kamu:')

# # age = st.number_input('Masukkan umur kamu: ', min_value=0, max_value=100)

# # if st.button("Sapa"):
# #     if age < 18:
# #         st.error(f"Maaf {name}, umur kamu {age}. Belum memenuhi syarat ❌")
# #     else:
# #         st.success(f"Halo {name}, umur kamu {age} tahun! 👏")





# # df = pd.DataFrame(
# #     np.random.randn(10, 2),
# #     columns=['x', 'y']
# # )

# # st.write('Contoh Tabel:')
# # st.dataframe(df)
# # st.line_chart(df)





# st.title("Level 2: EDA Sederhana 📊")

# uploaded_file = st.file_uploader("Upload file CSV", type="csv")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.write("✅ Dataset berhasil dimuat!")
#     st.dataframe(df.head())


# if uploaded_file is not None:
#     st.subheader("Ringkasan Data")
#     st.write("Jumlah baris & kolom:", df.shape)
#     st.write("Tipe data:", df.dtypes)
#     st.write("Statistik deskriptif:")
#     st.write(df.describe())


# if uploaded_file is not None:
#     st.subheader("Visualisasi Data")

#     # Pilih kolom numerik
#     num_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
#     col = st.selectbox("Pilih kolom numerik:", num_cols)

#     # Histogram
#     fig, ax = plt.subplots()
#     df[col].hist(bins=20, ax=ax)
#     st.pyplot(fig)

#     # Line chart interaktif
#     st.line_chart(df[num_cols])


# if uploaded_file is not None:
#     st.subheader("Filter Data")

#     col_filter = st.selectbox("Pilih kolom untuk filter:", df.columns)
#     unique_vals = df[col_filter].unique()
#     selected_val = st.selectbox("Pilih nilai:", unique_vals)

#     st.write("Data terfilter:")
#     st.dataframe(df[df[col_filter] == selected_val])


# model, target_names = joblib.load("iris_model.pkl")

# st.title("Prediksi Spesies Bunga Iris 🌸")

# st.markdown("""
# Aplikasi ini memprediksi spesies bunga **Iris** berdasarkan panjang & lebar sepal dan petal.
# Gunakan input di sidebar untuk mengubah nilai fitur
# """)

# # Input fitur iris
# st.sidebar.header("Input Fitur Bunga")
# sepal_length = st.sidebar.number_input("Sepal Length (cm)", 0.0, 10.0, 5.1)
# sepal_width = st.sidebar.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
# petal_length = st.sidebar.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
# petal_width = st.sidebar.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

# # Bungkus jadi array
# features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# # Prediksi
# if st.button("Prediksi"):
#     pred = model.predict(features)[0]
#     proba = model.predict_proba(features)[0]

#     st.subheader("Hasil Prediksi 🌼")
#     st.success(f"Spesies: {target_names[pred]}")

#     st.progress(int(proba[pred]*100))
#     st.write("Probabilitas detail:")
#     for cls, p in zip(target_names, proba):
#         st.write(f"- {cls}: {p:.2f}")

#     fig, ax = plt.subplots()
#     ax.bar(target_names, proba, color=["#FF9999","#66B2FF","#99FF99"])
#     ax.set_ylabel("Probabilitas")
#     st.pyplot(fig)

#     col1, col2 = st.columns(2)
#     col1.metric("Sepal Length", sepal_length)
#     col2.metric("Petal Length", petal_length)

import streamlit as st
import torch
import torch.nn.functional as F
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# === Load Model (full model, bukan state_dict) ===
@st.cache_resource
def load_model():
    model = torch.load("cnn_mnist.pth", map_location="cpu", weights_only=False)
    model.eval()
    return model

model = load_model()

# === Streamlit UI ===
st.title("✏️ Prediksi Angka Tulis Tangan (MNIST CNN)")

st.markdown("Gambarlah angka 0–9 di kanvas, lalu klik **Prediksi**")

# === Canvas untuk menggambar ===
canvas_result = st_canvas(
    fill_color="black",
    stroke_width=15,           # biar coretan lebih tebal
    stroke_color="white",
    background_color="black",
    width=280,                 # kanvas besar
    height=280,
    drawing_mode="freedraw",
    key="canvas",
)

def preprocess(img):
    # resize & grayscale
    img = img.resize((28, 28)).convert("L")
    img = np.array(img).astype("float32") / 255.0

    # --- TES: jangan di-invert dulu ---
    # MNIST asli: digit putih (1), background hitam (0)
    # Jadi coretan putih di canvas seharusnya sudah sesuai
    # img = 1.0 - img   <-- coba matikan dulu

    # Tambahkan threshold biar lebih jelas (optional)
    img = (img > 0.5).astype("float32")

    # Bentuk tensor [1,1,28,28]
    img = torch.tensor(img, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    return img


# === Prediksi ===
if st.button("Prediksi"):
    if canvas_result.image_data is not None:
        img = Image.fromarray((canvas_result.image_data[:, :, 0]).astype("uint8"))
        input_tensor = preprocess(img)

        # === PREVIEW INPUT 28x28 ===
        small_img = input_tensor.squeeze().numpy()  # [28,28]
        st.image(
            Image.fromarray((small_img * 255).astype("uint8")).resize((140, 140)),
            caption="Input 28x28 ke Model",
            width=140
        )

        # === PREDIKSI ===
        with torch.no_grad():
            output = model(input_tensor)
            pred = torch.argmax(output, dim=1).item()
            probs = torch.softmax(output, dim=1).numpy()[0]

        st.success(f"✅ Hasil Prediksi: {pred}")
        st.bar_chart(probs)
    else:
        st.warning("Silakan gambar angka dulu di kanvas!")
