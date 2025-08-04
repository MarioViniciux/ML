import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

STRIDE_EXPLANATIONS = {
    "Spoofing": "Ameaça de um ator malicioso se passar por outro usuário, componente ou sistema.",
    "Tampering": "Ameaça de modificação não autorizada de dados em trânsito ou armazenados.",
    "Repudiation": "Ameaça relacionada à incapacidade de rastrear uma ação até seu autor.",
    "Information Disclosure": "Ameaça de exposição de informações sensíveis a indivíduos não autorizados.",
    "Denial of Service": "Ameaça de tornar um sistema ou recurso indisponível para seus usuários.",
    "Elevation of Privilege": "Ameaça de um usuário obter permissões mais altas do que as que deveria ter."
}

st.set_page_config(page_title="Análise STRIDE com Transformer", layout="wide")
st.title("🚀 Análise de Ameaças STRIDE com Transformer (IA Avançada)")
st.markdown("Descreva uma funcionalidade. A IA usará um modelo de linguagem avançado para identificar ameaças.")

system_description = st.text_area("Descrição do Sistema ou Funcionalidade:", height=150, placeholder="Ex: Um usuário pode ver o extrato de outro usuário apenas mudando o ID na URL.")

prediction_threshold = st.slider(
    "Limiar de Confiança para Ameaças", 
    min_value=0.0, max_value=1.0, value=0.6, step=0.05
)

if st.button("Analisar Ameaças"):
    if system_description:
        with st.spinner('Analisando com o modelo Transformer... Isso pode levar alguns segundos.'):
            try:
                payload = {"description": system_description}
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()
                
                results = response.json()
                probabilities = results.get("probabilities", {})

                st.subheader("Resultados da Análise:")
                
                cols = st.columns(len(STRIDE_EXPLANATIONS))
                found_any_threat = False
                
                sorted_probs = sorted(probabilities.items(), key=lambda item: item[1], reverse=True)
                
                for category, prob in sorted_probs:
                    if category == "Benign":
                        continue

                    col_index = list(STRIDE_EXPLANATIONS.keys()).index(category)

                    with cols[col_index]:
                        is_threat = prob >= prediction_threshold
                        st.metric(label=category, value=f"{prob:.2%}")

                        if is_threat:
                            found_any_threat = True
                            st.error(f"Ameaça Detectada", icon="🚨")
                            with st.expander("Detalhes"):
                                st.write(STRIDE_EXPLANATIONS[category])
                        else:
                            st.success("OK", icon="✅")

                if not found_any_threat:
                    st.info("Nenhuma ameaça identificada com o limiar de confiança atual.")

            except requests.exceptions.RequestException as e:
                st.error(f"Erro ao conectar com a API: {e}")
                st.error("Verifique se o backend (servidor FastAPI) está rodando.")
    else:
        st.warning("Por favor, insira uma descrição para ser analisada.")