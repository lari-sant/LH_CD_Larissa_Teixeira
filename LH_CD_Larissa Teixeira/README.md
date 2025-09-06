# Lighthouse | Desafio Ciência de Dados — IMDb

## Estrutura

- `LH_CD_Notebook.ipynb` — Notebook Jupyter com toda a análise (EDA, modelagem, respostas às perguntas).
- `model_imdb_rating.pkl` — Modelo final treinado para prever nota do IMDb.
- `requirements.txt` — Dependências do projeto (versões fixas).
- `predict_shawshank.py` — Script CLI que carrega o modelo salvo e imprime a previsão de nota do IMDb para o filme *The Shawshank Redemption*.

## Instalação e Uso
## Como executar

1. Clone este repositório e entre na pasta do projeto.

```bash
git clone https://github.com/lari-sant/desafio_cd.git
cd desafio_cd
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

3. Abra o notebook:

```bash
jupyter notebook LH_CD_Notebook.ipynb
```

4. Rodar o script de previsão:

```bash
python predict_shawshank.py
```



  ## Perguntas respondidas no desafio

Qual filme recomendar a uma pessoa desconhecida?
Equilibrando qualidade (nota IMDB alta) e popularidade (número de votos)
Pelos resultados da análise exploratória, filmes como “The Dark Knight” (2008) ou “Inception” (2010) aparecem entre os mais votados e com notas acima de 8,5.

Principais fatores de alta bilheteria
A análise de correlação e distribuições mostrou que:
- Número de votos (No_of_Votes) tem forte correlação com receita bruta (Gross), indicando que filmes muito comentados como populares tendem a arrecadar mais.
- Ano de lançamento também influencia: produções mais recentes apresentam receitas maiores, possivelmente devido a preços de ingresso mais altos e maior alcance global.
- Gêneros de ação/aventura aparecem frequentemente no topo de arrecadação.
- Elenco/diretor de renome, também impactam positivamente.

Insights da coluna Overview (inferência de gênero)
Utilizando (TF-IDF + Logistic Regression) para prever o gênero principal a partir da sinopse (Overview).
- Com os 6 gêneros mais frequentes, obtive uma acurácia em torno de 65–70% no conjunto de teste.
- Palavras-chave em sinopses ajudam a identificar bem gêneros mais distintos
- Gêneros próximos (como Drama e Thriller) têm maior confusão.
Conclusão: é possível inferir o gênero, mas para alta precisão seria necessário usar técnicas mais avançadas (como embeddings de linguagem).

Predição da nota IMDB
Treinado dois modelos para prever a nota IMDB (IMDB_Rating):
Linear Regression (baseline)
RandomForestRegressor 

Métricas no conjunto de teste:
RandomForest: RMSE ≈ 0.35 | R² ≈ 0.65
LinearRegression: RMSE ≈ 0.45 | R² ≈ 0.45

## Próximos Passos / Melhorias

Usar embeddings de texto (BERT, Word2Vec) para melhorar/enriquecer a classificação por Overview

Importar dados externos (ex.: orçamento, data de lançamento, premios)

Avaliar modelos de boosting (XGBoost, LightGBM)

👩‍💻 Autor
Larissa Teixeira
