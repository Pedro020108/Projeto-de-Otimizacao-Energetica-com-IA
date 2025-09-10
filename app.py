import random
import streamlit as st
import pandas as pd
import plotly.express as px
#streamlit run app.py



def dados_inversor_simulado():
    return {
        "geracao_solar": random.randint(0, 4000),  # em Watts
        "bateria": random.randint(0, 100)        # % de carga
    }

def dados_clima_simulado():
    return {
        "temperatura": random.randint(10, 35),

    }

def regras_inteligentes(dados_energia, dados_clima):
    consumo_total = random.randint(500, 2000)
    geracao = dados_energia["geracao_solar"]
    bateria = dados_energia["bateria"]

    decisao = ""
    if geracao > consumo_total and bateria < 80:
        decisao = "Excedente solar → Carregar bateria."
    elif bateria > 50 and geracao < consumo_total:
        decisao = "Usar energia da bateria para suprir consumo."
    elif bateria <= 20:
        decisao = "Ativar modo economia. Desligar aparelhos não essenciais."
    else:
        decisao = "Manter funcionamento normal."

    alerta = ""
    if dados_clima["temperatura"] > 18 and geracao < 500:
        alerta = "Alerta: Dia muito quente, baixa geração → possível problema nos painéis."

    return consumo_total, decisao, alerta

def modo_emergencial(dados_energia):
    bateria = dados_energia["bateria"]
    autonomia_horas = round(bateria / 10, 1)
    return f"MODO EMERGENCIAL ATIVADO\nMantendo apenas geladeira, iluminação básica e internet.\nAutonomia estimada: {autonomia_horas} horas."


st.set_page_config(page_title="Dashboard Energia Solar", layout="wide")
st.title("Projeto de Energia Solar - Dashboard Interativo")

# Coleta de dados simulados
energia = dados_inversor_simulado()
clima = dados_clima_simulado()
consumo_total, decisao, alerta = regras_inteligentes(energia, clima)


if energia["bateria"] <= 20 and energia["geracao_solar"] < consumo_total:
    energia_recebida_da_rede = True
else:
    energia_recebida_da_rede = False

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.header("Dados Coletados")
st.sidebar.write("Inversor:")
st.sidebar.json(energia)
st.sidebar.write("Clima:")
st.sidebar.json(clima)
st.sidebar.write(f"Decisão inteligente: {decisao}")
if alerta:
    st.sidebar.warning(alerta)

# Modo emergencial
if energia["bateria"] <= 20 and energia["geracao_solar"] < consumo_total:
    st.sidebar.error(modo_emergencial(energia))

# ----------------------------
# Visualização principal
# ----------------------------
st.header("Visualização de Dados")

# Métricas em colunas
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Geração Solar (W)", energia["geracao_solar"])
with col2:
    st.metric("Consumo Total (W)", consumo_total)
with col3:
    st.metric("Bateria (%)", energia["bateria"])
with col4:
    st.metric("Energia da rua?", "Sim" if energia_recebida_da_rede else "Não")

# Gráfico interativo
df = pd.DataFrame({
    "Categoria": ["Geração Solar", "Consumo Total", "Bateria"],
    "Valor": [energia["geracao_solar"], consumo_total, energia["bateria"]]
})

fig = px.bar(df, x="Categoria", y="Valor", color="Categoria",
             color_discrete_map={"Geração Solar":"orange", "Consumo Total":"red", "Bateria":"green"})
st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Modo Educacional (em branco)
# ----------------------------
st.header("Modo Educacional")
st.info("modo educacional")
