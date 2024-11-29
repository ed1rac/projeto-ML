import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# para rodar: streamlit run .\app.py

df = pd.read_csv('imoveis.csv')

# criando o modelo
# modelo = linear_model.LinearRegression()
modelo = LinearRegression()

# treinando o modelo (passando o tamanho e o preço dos imoveis)
x = df[["tamanho"]]  # usando dois colchetes para retornar em formato de lista/df
y = df[["preco"]]
modelo.fit(x, y)


st.title("Prevendo o valor de um imóvel em João Pessoa")
st.divider()
st.subheader("Usando o modelo de regressão linear")
tamanho = st.number_input("Digite o tamanho do apartamento: ", min_value=45.77)

if tamanho:
    preco_previsto = modelo.predict([[tamanho]])[0][0]
    st.write(f"O valor do imóvel com tamanho {
             tamanho:.2f} é de R$ {preco_previsto:,.2f}.")
    st.balloons()


# Criando o modelo de regressão polinomial
grau = 2  # Grau do polinômio (ajustar conforme necessário)
poly = PolynomialFeatures(degree=grau)  # Transformação para termos polinomiais
x_poly = poly.fit_transform(x)  # Transformando os dados
modelo_polinomial = LinearRegression()
modelo_polinomial.fit(x_poly, y)  # Treinando o modelo polinomial

# Adicionando outro divisor para separar os modelos
st.divider()

# Interface para o modelo polinomial
st.subheader("Usando o modelo de regressão polinomial")

if tamanho:
    # Transformar o tamanho fornecido pelo usuário para o formato polinomial
    tamanho_poly = poly.transform([[tamanho]])
    preco_polinomial = modelo_polinomial.predict(
        tamanho_poly)[0][0]  # Prevendo o preço polinomial

    # Mostrando o resultado
    st.write(f"O valor do imóvel com tamanho {
             tamanho:.2f} (regressão polinomial) é de R$ {preco_polinomial:,.2f}.")
