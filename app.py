import os
import pandas as pd

arquivo_csv = "banco_biblioteca.csv"

print("==========================================")
print("     SISTEMA SMARTLIBRARY - v1.0          ")
print("==========================================\n")

# 1. Carga inicial (ETL Pandas)
if os.path.exists(arquivo_csv):
    df_banco = pd.read_csv(arquivo_csv)
    minha_biblioteca = df_banco.to_dict('records')
    print(f"📚 Banco de dados carregado: {len(minha_biblioteca)} livro(s) encontrado(s).")
else:
    minha_biblioteca = []
    print("✨ Criando novo banco de dados local...")

# 2. Loop Principal
while True:
    print("\n------------------------------------------")
    novo_livro = input("Título do livro que gostou (ou 'sair'): ").strip()
    
    if novo_livro.lower() == 'sair':
        print("\nEncerrando o SmartLibrary. Boas leituras!")
        break
        
    novo_autor = input("Nome do autor: ").strip()
    minha_biblioteca.append({"titulo": novo_livro, "autor": novo_autor})

    # Mensagem de processamento da versão 1.0
    print("\n⏳ Processando dados do livro...")
    print(f"\n🤖 Status do Recomendador: Livro '{novo_livro}' registrado com sucesso.")
    print("💡 (Módulo de Recomendação Generativa via LLM em fase de homologação no roadmap v2.0)")

    # Persistência em CSV via Pandas
    df_atualizado = pd.DataFrame(minha_biblioteca)
    df_atualizado.to_csv(arquivo_csv, index=False)
    print(f"\n💾 Dados salvos em '{arquivo_csv}'.")