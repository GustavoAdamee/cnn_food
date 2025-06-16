import os
import shutil
import random

# --- CONFIGURAÇÃO ---
# 1. Caminho para a pasta original com todas as imagens separadas por classe.
#    Ajuste este caminho se você colocou sua pasta em outro lugar.
SOURCE_DIR = "../raw_data/Imagens_um_Alimento"

# 2. Caminho para a nova pasta onde o dataset dividido será salvo.
DEST_DIR = "../processed_data/dataset_1_split"

# 3. Proporção da divisão (ex: 0.8 para 80% de treino e 20% de validação).
SPLIT_RATIO = 0.8
# --------------------

classes = []

def split_dataset(source, dest, split_ratio):
    """
    Função para dividir um dataset em treino e validação.
    """
    print("Iniciando a divisão do dataset...")

    # Cria o diretório de destino principal, se não existir.
    if not os.path.exists(dest):
        os.makedirs(dest)
        print(f"Diretório de destino criado em: {dest}")

    # Lista todas as classes (que são as subpastas no diretório de origem)
    classes = [d for d in os.listdir(source) if os.path.isdir(os.path.join(source, d))]
    print(f"Classes encontradas: {classes}")

    for class_name in classes:
        print(f"\nProcessando classe: {class_name}")

        # Cria os diretórios de treino e validação para a classe atual
        train_class_dir = os.path.join(dest, 'train', class_name)
        validation_class_dir = os.path.join(dest, 'validation', class_name)
        
        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(validation_class_dir, exist_ok=True)

        # Caminho da pasta da classe de origem
        source_class_dir = os.path.join(source, class_name)

        # Lista e embaralha todos os arquivos da classe
        files = os.listdir(source_class_dir)
        random.shuffle(files)

        # Calcula o ponto de divisão
        split_point = int(len(files) * split_ratio)

        # Separa a lista de arquivos em treino e validação
        train_files = files[:split_point]
        validation_files = files[split_point:]

        # Copia os arquivos de treino
        for file_name in train_files:
            source_path = os.path.join(source_class_dir, file_name)
            dest_path = os.path.join(train_class_dir, file_name)
            shutil.copy(source_path, dest_path)
        
        # Copia os arquivos de validação
        for file_name in validation_files:
            source_path = os.path.join(source_class_dir, file_name)
            dest_path = os.path.join(validation_class_dir, file_name)
            shutil.copy(source_path, dest_path)
            
        print(f"Classe '{class_name}': {len(train_files)} imagens para treino, {len(validation_files)} para validação.")

    print("\nDivisão do dataset concluída com sucesso!")


# Executa a função
split_dataset(SOURCE_DIR, DEST_DIR, SPLIT_RATIO)

# Opcional: Verifica a contagem de arquivos para confirmar
print("\n--- Resumo da Divisão ---")
for folder in ['train', 'validation']:
    for class_name in classes:
        folder_path = os.path.join(DEST_DIR, folder, class_name)
        num_files = len(os.listdir(folder_path))
        print(f"Pasta: {folder_path} | Imagens: {num_files}")