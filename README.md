# CNN Food Classification 🍽️

Um projeto de classificação de alimentos utilizando Redes Neurais Convolucionais (CNNs) para identificar diferentes tipos de comida em imagens.

## 📋 Descrição do Projeto

Este projeto implementa modelos de CNN para classificar 16 tipos diferentes de alimentos brasileiros, incluindo:
- Alface
- Almôndega
- Arroz
- Batata Frita
- Beterraba
- Bife Bovino na Chapa
- Carne Bovina na Panela
- Cenoura
- Feijão Carioca
- Macarrão
- Maionese
- Peito de Frango
- Purê de Batata
- Strogonoff de Carne
- Strogonoff de Frango
- Tomate

## 🚀 Estrutura do Projeto

```
cnn_food/
├── notebooks/
│   ├── part_1_basic_model.ipynb
│   ├── part_2_enhanced_model.ipynb
│   └── part_3_models_comparison.ipynb
├── scripts/
│   └── split_dataset_1.py
├── raw_data/
│   └── Imagens_um_Alimento/
├── processed_data/
│   └── dataset_1_split/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🛠️ Instalação e Configuração

### 1. Pré-requisitos

- Python 3.8+
- pip
- virtualenv (recomendado)

### 2. Clonando o Repositório

```bash
git clone <url-do-repositorio>
cd cnn_food
```

### 3. Criando Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
```

### 4. Instalando Dependências

```bash
pip install -r requirements.txt
```

## 📁 Preparação dos Dados

### 1. Estrutura de Dados Esperada

Certifique-se de que seus dados estão organizados na seguinte estrutura:

```
raw_data/
└── Imagens_um_Alimento/
    ├── Alface/
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   └── ...
    ├── Almondega/
    │   ├── img1.jpg
    │   └── ...
    └── ... (outras classes)
```

### 2. Executando o Script de Divisão

⚠️ **IMPORTANTE**: Antes de executar os notebooks, é necessário rodar o script de divisão dos dados:

```bash
cd scripts
python split_dataset_1.py
```

Este script irá:
- Dividir automaticamente os dados em 80% treino e 20% validação
- Criar a estrutura de pastas necessária em `processed_data/dataset_1_split/`
- Preservar a distribuição das classes

## 🔬 Executando os Modelos

### Ordem de Execução Recomendada:

1. **Primeiro**: Execute o script de divisão dos dados (passo anterior)

2. **Modelo Básico**:
   ```bash
   jupyter notebook notebooks/basic_model.ipynb
   ```
   - Implementa uma CNN simples
   - Serve como baseline para comparação

3. **Modelo Aprimorado**:
   ```bash
   jupyter notebook notebooks/enhanced_model.ipynb
   ```
   - Versão melhorada com técnicas avançadas
   - Inclui regularização e otimizações

4. **Report dos Modelos**:
   ```bash
   jupyter notebook notebooks/model_report_generator.ipynb
   ```
   - Gera um report do modelo selecionado
   - Gera uma matriz de confusão do modelo

5. **Feature Map dos Modelos**:
   ```bash
   jupyter notebook notebooks/feature_map_viewer.ipynb
   ```
   - Gera o feature map do modelo selecionado para uma imagem aleatória

6. **Comparação de Modelos**:
   ```bash
   jupyter notebook notebooks/models_comparison.ipynb
   ```
   - Compara os diferentes modelos
   - Análise de performance detalhada

7. **Demonstração prática dos modelos**:
   ```bash
   jupyter notebook notebooks/demonstration.ipynb
   ```
   - Faz a demonstração dos modelos para imagens em "test_images"

## 📊 Métricas de Avaliação

Os modelos são avaliados usando:
- **Acurácia**: Percentual de classificações corretas
- **Matriz de Confusão**: Visualização detalhada dos erros
- **Relatório de Classificação**: Precision, Recall e F1-Score por classe
- **Curvas de Aprendizado**: Evolução da acurácia e perda durante o treinamento


## 📈 Resultados Esperados

Com o modelo básico, espera-se:
- Acurácia de validação: ~50%
- Convergência em aproximadamente 15-20 épocas
- Baixa generalização das classes

Com o modelo otimizado, espera-se:
- Acurácia de validação: ~98%
- Convergência em aproximadamente 35 épocas (EarlyStopping atuando aqui)
- Boa generalização das classes

## 📋 Dependências Principais

- TensorFlow/Keras: Framework de deep learning
- Scikit-learn: Métricas de avaliação
- Matplotlib: Visualizações
- Seaborn: Gráficos estatísticos
- NumPy: Computação numérica
- Pandas: Manipulação de dados
