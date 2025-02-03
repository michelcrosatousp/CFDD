import streamlit as st

# Funções discriminantes para o sexo feminino
def funcao_discriminante_feminino(dentes):
    if dentes == "13 e 23":
        return (
            -282.282
            + (MD_13 * 1.441) + (AL_13 * 2.703) + (VL_13 * 18.045)
            + (MD_23 * 14.480) + (AL_23 * 1.188) + (VL_23 * 3.515)
            + (IC_13 * 4.807) + (CERV_13 * 1.810) + (CERL_13_23 * 3.773)
            + (PM_13_23 * -0.626) + (PD_13_23 * 0.498)
        )
    elif dentes == "33 e 43":
        return (
            -267.77
            + (MD_33 * 23.545) + (AL_33 * 5.474) + (VL_33 * 5.647)
            + (MD_43 * 1.631) + (AL_43 * 1.595) + (VL_43 * 25.715)
            + (IC_33_43 * 8.393) + (CERV_33 * 0.502) + (CERL_33_43 * 7.127)
            + (PM_33_43 * 9.063) + (PD_33_43 * 1.618)
        )

# Funções discriminantes para o sexo masculino
def funcao_discriminante_masculino(dentes):
    if dentes == "13 e 23":
        return (
            -318.746
            + (MD_13 * 1.758) + (AL_13 * 2.818) + (VL_13 * 17.227)
            + (MD_23 * 15.774) + (VL_23 * 3.737) + (AL_23 * 2.894)
            + (IC_13 * 5.713) + (CERV_13 * 3.831) + (CERL_13_23 * 3.831)
            + (PM_13_23 * -1.209) + (PD_13_23 * 0.709)
        )
    elif dentes == "33 e 43":
        return (
            -305.383
            + (MD_33 * 27.150) + (AL_33 * 5.540) + (VL_33 * 3.919)
            + (MD_43 * 2.969) + (AL_43 * 1.397) + (VL_43 * 30.012)
            + (IC_33_43 * 8.958) + (CERV_33 * 0.165) + (CERL_33_43 * 7.628)
            + (PM_33_43 * 9.447) + (PD_33_43 * 1.936)
        )

# Interface do usuário
st.title("CFDD_2005.1")
st.write('')
st.write('Calculadora de Funções Discriminantes Dentárias')
st.write('Título da Tese: "Determinação do sexo a partir da morfometria geométrica e mensurações em imagens tridimensionais de dentes caninos."')
st.write('Autores do app: Bento MIC, Biazevic MGH, Michel-Crosato E.')
st.write('PRPG - Ciências Odontológicas - FOUSP')
st.write('')

# Entrada das variáveis odontométricas
MD_13 = st.number_input("MD (dente 13):", format="%.3f")
AL_13 = st.number_input("AL (dente 13):", format="%.3f")
VL_13 = st.number_input("VL (dente 13):", format="%.3f")
MD_23 = st.number_input("MD (dente 23):", format="%.3f")
AL_23 = st.number_input("AL (dente 23):", format="%.3f")
VL_23 = st.number_input("VL (dente 23):", format="%.3f")
IC_13 = st.number_input("IC (dente 13):", format="%.3f")
CERV_13 = st.number_input("CERV (dente 13):", format="%.3f")
CERL_13_23 = st.number_input("CERL (dentes 13 e 23):", format="%.3f")
PM_13_23 = st.number_input("PM (dentes 13 e 23):", format="%.3f")
PD_13_23 = st.number_input("PD (dentes 13 e 23):", format="%.3f")

# Entrada de variáveis para os dentes 33 e 43
MD_33 = st.number_input("MD (dente 33):", format="%.3f")
AL_33 = st.number_input("AL (dente 33):", format="%.3f")
VL_33 = st.number_input("VL (dente 33):", format="%.3f")
MD_43 = st.number_input("MD (dente 43):", format="%.3f")
AL_43 = st.number_input("AL (dente 43):", format="%.3f")
VL_43 = st.number_input("VL (dente 43):", format="%.3f")
IC_33_43 = st.number_input("IC (dentes 33 e 43):", format="%.3f")
CERV_33 = st.number_input("CERV (dente 33):", format="%.3f")
CERL_33_43 = st.number_input("CERL (dentes 33 e 43):", format="%.3f")
PM_33_43 = st.number_input("PM (dentes 33 e 43):", format="%.3f")
PD_33_43 = st.number_input("PD (dentes 33 e 43):", format="%.3f")

# Escolha dos dentes
dentes = st.radio("Escolha os dentes:", ("13 e 23", "33 e 43"))

# Cálculo e comparação das funções discriminantes
if st.button("Calcular"):
    valor_feminino = funcao_discriminante_feminino(dentes)
    valor_masculino = funcao_discriminante_masculino(dentes)

    st.write(f"Valor discriminante para o sexo feminino: {valor_feminino:.3f}")
    st.write(f"Valor discriminante para o sexo masculino: {valor_masculino:.3f}")

    if valor_feminino > valor_masculino:
        st.success("Classificação: Sexo Feminino")
    else:
        st.success("Classificação: Sexo Masculino")

# Tese

st.write('Verificar método na tese disponivel em:')
st.write('https://www.teses.usp.br/teses/disponiveis/23/23158/tde-31012023-093731/publico/MariaIzabelCardosoBentoVersaoCorrigida.pdf')