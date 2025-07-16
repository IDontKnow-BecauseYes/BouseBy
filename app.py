import streamlit as st
import google.generativeai as genai

# Configurar chave da API via secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Criar modelo
model = genai.GenerativeModel("gemini-pro")

# Função para gerar perfil
def gerar_perfil(nome, opiniao):
    prompt = f"""
    Crie um perfil criativo e fictício com base nos dados abaixo.

    Nome: {nome}
    Característica marcante / opinião forte: {opiniao}

    Gere um pequeno parágrafo (3 a 5 linhas) descrevendo:
    - Nome completo
    - Idade estimada
    - Profissão ou área de atuação
    - Comportamento ou visão de mundo relacionada à opinião
    - Um fato curioso ou destaque da vida dessa pessoa

    Mantenha um tom leve, realista e criativo.
    """

    response = model.generate_content(prompt)
    return response.text.strip()

# Interface Streamlit
st.title("📝 Gerador de Perfis Criativos")
st.write("Digite o nome de uma pessoa e uma opinião ou característica para gerar um perfil fictício.")

nome = st.text_input("Nome completo")
opiniao = st.text_area("Opinião ou característica marcante")

if st.button("Gerar perfil"):
    if nome and opiniao:
        resultado = gerar_perfil(nome, opiniao)
        st.success("Perfil gerado:")
        st.code(resultado)
    else:
        st.warning("Preencha todos os campos.")
