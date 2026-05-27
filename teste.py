import streamlit as st
import base64
import os

st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO
def get_base64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# IMAGENS
img_base64 = get_base64_image("empresa.png")
zap_base64 = get_base64_image("zap.png")

# TOPO
col1, col2, col3 = st.columns([1,2,1])

with col2:

    if img_base64:
        st.markdown(f"""
        <div style="text-align:center;">
            <a href="https://www.netflix.com/br/" target="_blank">
                <img src="data:image/png;base64,{img_base64}" width="320">
            </a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Imagem empresa.png não encontrada")

# PERFIL
st.title("Rayane")

colA, colB = st.columns([1,3])

with colA:

    if os.path.exists("foto88.png"):
        st.image("foto88.png", width=250)
    else:
        st.warning("foto88.png não encontrada")

with colB:
    st.write("""
    Rayane é estudante do Ensino Médio no IFPB Campus Itabaiana,
    dedicada aos estudos e interessada em tecnologia.
    """)

# BOTÃO
st.link_button(
    "Visitar Netflix",
    "https://www.netflix.com/br/"
)

# WHATSAPP
if zap_base64:
    st.markdown(f"""
    <div style="text-align:center; margin-top:30px;">
        <a href="https://wa.me/5581997471583" target="_blank">
            <img src="data:image/png;base64,{zap_base64}" width="100">
        </a>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("zap.png não encontrada")
