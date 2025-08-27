# dashboard clipping
Dashboard interativo de Clipping e Stories para empresas de RP. Registre matérias e posts, visualize gráficos de evolução e sentimento, e exporte relatórios em CSV. Facilita monitoramento de mídia e análise de percepção de marca de forma prática e visual.


                                     Passo a Passo do Projeto: Dashboard de Clipping e Stories
1. Planejamento do Projeto
Definição do objetivo: criar uma ferramenta para monitoramento de matérias (clipping) e stories para empresas de assessoria de imprensa e RP.
Levantamento das funcionalidades principais:
Registro de dados de clientes/empresas.
Armazenamento de número de stories e matérias.
Registro do sentimento predominante (positivo, neutro ou negativo).
Visualização gráfica dos dados.
Exportação em Excel/CSV.

2. Criação do Ambiente de Desenvolvimento
Criação de um ambiente virtual no Python para isolar as dependências:
python -m venv venv
source venv/bin/activate

Instalação das bibliotecas necessárias:
pip install streamlit pandas matplotlib

3. Estrutura do Código
Inicialização do projeto com Streamlit para interface web.
Definição da página com st.set_page_config() e título st.title().
Armazenamento dos dados usando Session State (st.session_state["data"]) para manter os registros ativos durante a sessão.

4. Formulário de Entrada de Dados
Criação do formulário com st.form():
Campo de nome da empresa/cliente/marca (st.text_input()).
Campo de quantidade de stories postados (st.number_input()).
Campo de quantidade de matérias de clipping (st.number_input()).
Campo de sentimento predominante (st.selectbox()).
Botão de envio com st.form_submit_button().
Validação para não permitir nome vazio e adição dos dados ao session state.

5. Visualização dos Dados
Transformação dos dados em DataFrame do Pandas (pd.DataFrame(st.session_state["data"])).
Filtro por empresa com st.selectbox(), incluindo opção “Todas as empresas”.
Visualização em tabela com st.dataframe().
Criação de gráficos:
Linha de evolução de stories (st.line_chart()).
Gráfico de barras para matérias (st.bar_chart()).
Gráfico de pizza para sentimento usando Matplotlib.

6. Exportação de Dados
Conversão do DataFrame para CSV:
csv = df_filtrado.to_csv(index=False).encode("utf-8")
Botão de download com st.download_button(), nomeando automaticamente o arquivo com o nome da empresa selecionada.

7. Ajustes Finais
Possibilidade de cadastrar novas empresas e continuar adicionando dados sem repetir o nome.
Filtro inteligente: quando uma empresa é selecionada, a caixa para nome novo só aparece se escolher "Nova Empresa".
Garantia de que os nomes das empresas aparecem corretamente no CSV (uma coluna para cada dado: Empresa/Cliente, Stories, Matérias, Sentimento).
Inclusão de opção de visualizar todas as empresas no select box.

8. Testes
Inserção de múltiplos registros para várias empresas.
Verificação de gráficos, tabelas e exportação.
Garantia de que os nomes aparecem corretamente, que o filtro funciona e que o CSV abre corretamente no Excel.

9. Resultado Final
Dashboard interativo, visual e fácil de usar.
Permite monitorar métricas de clipping e stories por cliente.

Exporta relatórios organizados em CSV para envio ou arquivamento.

Ferramenta útil para assessorias de imprensa e RP para análises rápidas de desempenho e sentimento.
