import streamlit as st
import base64
import os

# CONFIGURAÇÃO
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO BASE64
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
        <div style="text-align:center; margin-bottom:40px;">
            <a href="https://www.netflix.com/br/" target="_blank">
                <img src="data:image/png;base64,{img_base64}"
                     width="350"
                     style="
                        border-radius:15px;
                        box-shadow:0px 0px 15px rgba(0,0,0,0.3);
                     ">
            </a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("empresa.png não encontrada")

# LINHA
st.markdown("---")

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3,1])

with col_left:

    # NOME
    st.markdown("""
    <h1 style="
        color:#222;
        margin-bottom:30px;
    ">
    Rayane
    </h1>
    """, unsafe_allow_html=True)

    # SUBCOLUNAS
    sub1, sub2 = st.columns([1,3])

    # FOTO PERFIL
    with sub1:

        if os.path.exists("foto 88.png"):
            st.image("foto 88.png", width=250)
        else:
            st.warning("foto 88.png não encontrada")

    # TEXTO
    with sub2:

        st.markdown("""
        <div style="
            font-size:20px;
            line-height:2;
            text-align:justify;
            margin-top:20px;
        ">

        <b>Sobre Rayane:</b><br><br>

        Rayane é estudante do Ensino Médio no IFPB Campus Itabaiana,
        dedicada aos estudos e interessada em tecnologia.
        Ama aprender coisas novas e desenvolver projetos criativos.

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # BOTÃO NETFLIX
    st.link_button(
        "🎬 Visitar Site da Netflix",
        "https://www.netflix.com/br/"
    )

# WHATSAPP
st.write("")
st.write("")

if zap_base64:
    st.markdown(f"""
    <div style="text-align:center; margin-top:30px;">

        <a href="https://wa.me/5581997471583" target="_blank">

            <img src="data:image/png;base64,{zap_base64}"
                 width="100">

        </a>

    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("zap.png não encontrada")
