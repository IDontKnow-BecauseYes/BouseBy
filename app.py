import streamlit as st
import google.generativeai as genai

# Configurar chave da API via secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Criar modelo
model = genai.GenerativeModel("gemini-pro")

# Função para gerar relatório
def gerar_relatorio(nome, opiniao):
    prompt = f"""
    Gere um relatório fictício e criativo, em tom policial/jornalístico, com base no seguinte:

    Nome: {nome}
    Opinião polêmica: {opiniao}

    O relatório deve conter:
    - Nome completo
    - Data da prisão (entre 2023 e 2030)
    - Motivo da prisão (relacionado à opinião polêmica)
    - Data da morte (entre a data da prisão e 2040)
    - Local da morte (na prisão ou na rua)

    Exemplo de estilo:
    Nome: João Silva
    Preso em: 14/09/2026
    Motivo: incitação ao ódio em rede social
    Morreu em: 03/12/2029 (prisão)

    Seja criativo, mas realista e direto. No máximo 5 linhas.
    """

    response = model.generate_content(prompt)
    return response.text.strip()

# Interface Streamlit
st.title("🧠 Gerador de Relatórios Fictícios")
st.write("Digite o nome de uma pessoa e uma opinião polêmica para gerar um relatório policial/jornalístico fictício.")

nome = st.text_input("Nome completo")
opiniao = st.text_area("Opinião polêmica")

if st.button("Gerar relatório"):
    if nome and opiniao:
        resultado = gerar_relatorio(nome, opiniao)
        st.success("Relatório gerado:")
        st.code(resultado)
    else:
        st.warning("Preencha todos os campos.")

