"""
Script simples para avaliar modelo otimizado
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar modelo
model = load_model('../notebooks/cnn_alimentos_modelo_base.h5')

# Configurar gerador de dados de validação
validation_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_directory(
    '../processed_data/dataset_1_split/validation',
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

# Obter nomes das classes
class_names = list(validation_generator.class_indices.keys())

# Fazer predições
Y_pred = model.predict(validation_generator)
y_pred = np.argmax(Y_pred, axis=1)
y_true = validation_generator.classes

# Relatório de classificação
print('Relatório de Classificação\n')
print(classification_report(y_true, y_pred, target_names=class_names))

# Matriz de confusão
print('\nMatriz de Confusão\n')
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.title('Matriz de Confusão - Modelo Otimizado')
plt.ylabel('Classe Verdadeira')
plt.xlabel('Classe Prevista')
plt.show()
