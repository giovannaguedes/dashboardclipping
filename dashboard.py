import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard de Clipping", layout="centered")

st.title("📊 Dashboard de Clipping e Stories por Empresa")

# Criando armazenamento simples
if "data" not in st.session_state:
    st.session_state["data"] = []

# Formulário de entrada
with st.form("clipping_form", clear_on_submit=True):
    empresa = st.text_input("Nome da empresa/cliente/marca:")
    stories = st.number_input("Quantos stories foram postados?", min_value=0, step=1)
    materias = st.number_input("Quantas matérias saíram no clipping?", min_value=0, step=1)
    sentimento = st.selectbox("Sentimento predominante das matérias:", ["Positivo", "Neutro", "Negativo"])
    submitted = st.form_submit_button("Adicionar")

    if submitted:
        if empresa.strip() == "":
            st.warning("⚠️ Digite o nome da empresa/cliente!")
        else:
            st.session_state["data"].append({
                "Empresa/Cliente": empresa,
                "Stories": stories,
                "Matérias": materias,
                "Sentimento": sentimento
            })
            st.success(f"✅ Registro adicionado para {empresa} com sucesso!")

# Mostrar dados já inseridos
if st.session_state["data"]:
    df = pd.DataFrame(st.session_state["data"])

    # Lista de empresas para filtrar + opção "Todas as empresas"
    empresas_para_filtro = list(df["Empresa/Cliente"].unique())
    empresas_para_filtro.sort()
    empresas_para_filtro.insert(0, "Todas as empresas")
    empresa_filtrada = st.selectbox("🔎 Filtrar por empresa:", empresas_para_filtro)

    if empresa_filtrada == "Todas as empresas":
        df_filtrado = df
    else:
        df_filtrado = df[df["Empresa/Cliente"] == empresa_filtrada]

    st.subheader(f"📌 Registros - {empresa_filtrada}")
    st.dataframe(df_filtrado, use_container_width=True)

    # Gráfico de evolução dos stories
    st.subheader("📈 Evolução de Stories Postados")
    st.line_chart(df_filtrado["Stories"])

    # Gráfico de matérias
    st.subheader("📰 Quantidade de Matérias")
    st.bar_chart(df_filtrado["Matérias"])

    # Gráfico de pizza por sentimento
    st.subheader("😊 Distribuição por Sentimento")
    fig, ax = plt.subplots()
    df_filtrado["Sentimento"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

    # Exportar para Excel/CSV
    st.subheader("💾 Exportar Dados")
    csv = df_filtrado.to_csv(index=False, sep=';', encoding='utf-8-sig').encode("utf-8-sig")
    st.download_button(
        label=f"⬇️ Baixar CSV - {empresa_filtrada}",
        data=csv,
        file_name=f"clipping_{empresa_filtrada}.csv",
        mime="text/csv"
    )
