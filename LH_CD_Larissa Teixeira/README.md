# Lighthouse | Desafio Ciência de Dados — IMDb

Este repositório contém a solução do desafio de Ciência de Dados da Indicium (Lighthouse).

## Estrutura

- `LH_CD_Notebook.ipynb` — Notebook Jupyter com toda a análise (EDA, modelagem, respostas às perguntas).
- `model_imdb_rating.pkl` — Modelo final treinado para prever nota do IMDb.
- `requirements.txt` — Dependências do projeto (versões fixas).
- `predict_shawshank.py` — Script CLI que carrega o modelo salvo e imprime a previsão de nota do IMDb para o filme *The Shawshank Redemption*.

## Como executar

1. Clone este repositório e entre na pasta do projeto.

```bash
git clone <URL_DO_REPO>
cd <PASTA_DO_REPO>
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

## Observações

- O projeto usa **scikit-learn** e **pipelines** para pré-processamento de texto, categorias e variáveis numéricas.
- Métrica escolhida: **MAE** (Mean Absolute Error), por ser intuitiva em termos de pontos na escala IMDb.
- Arquivos `.pkl` podem ser carregados com `joblib.load` para reutilizar o modelo.
