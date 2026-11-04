import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

arquivo_csv = "banco_biblioteca.csv"

if not os.path.exists(arquivo_csv):
    print("⚠️ O arquivo 'banco_biblioteca.csv' não foi encontrado. Execute o 'app.py' primeiro para cadastrar livros!")
else:
    # 1. Carga dos Dados
    df = pd.read_csv(arquivo_csv)
    
    # 2. Configuração do Estilo do Gráfico
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle('📊 Dashboard SmartLibrary - Análise de Acervo', fontsize=16, fontweight='bold', color='#1A2B4C')

    # Métricas Globais (KPIs)
    total_livros = len(df)
    total_autores = df['autor'].nunique()

    # Visual 1: Ranking de Autores (Gráfico de Barras)
    top_autores = df['autor'].value_counts().head(5)
    sns.barplot(x=top_autores.values, y=top_autores.index, ax=axes[0], palette="Blues_r")
    axes[0].set_title('Top Autores no Acervo', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Quantidade de Livros')
    axes[0].set_ylabel('Autor')

    # Visual 2: Cartões de Métricas (KPIs)
    axes[1].axis('off')
    axes[1].text(0.1, 0.75, f"📚 Total de Livros: {total_livros}", fontsize=18, fontweight='bold', color='#2B5C8F')
    axes[1].text(0.1, 0.45, f"👤 Autores Cadastrados: {total_autores}", fontsize=18, fontweight='bold', color='#2B5C8F')
    axes[1].text(0.1, 0.20, f"💾 Fonte de Dados: banco_biblioteca.csv", fontsize=12, style='italic', color='#555555')

    plt.tight_layout()
    
    # 3. Salvando a imagem do Dashboard
    nome_imagem = "dashboard.png"
    plt.savefig(nome_imagem, dpi=300, bbox_inches='tight')
    print(f"✅ Dashboard gerado com sucesso! A imagem '{nome_imagem}' foi salva na pasta do seu projeto.")