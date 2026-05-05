from pathlib import Path

def criar_pasta_aula():
    # 1. Define o caminho base onde tudo será criado
    diretorio_base = Path(r"C:\Users\51446093840\Desktop\Leonardo Barbosa [Castello]\1° Termo")
    
    # 2. Pede o número da aula
    numero = input("Digite o número da aula: ").strip()
    
    # 3. Define os nomes da pasta e do arquivo
    nome_pasta = f"Aula {numero}"
    nome_arquivo = f"Aula{numero}.py"
    
    # 4. Monta os caminhos completos
    caminho_pasta = diretorio_base / nome_pasta
    caminho_arquivo = caminho_pasta / nome_arquivo

    try:
        # Cria a pasta (parents=True permite criar pastas intermediárias se necessário)
        caminho_pasta.mkdir(parents=True, exist_ok=True)
        
        # Cria o arquivo .py
        if not caminho_arquivo.exists():
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                f.write(f"# Código da Aula {numero}\n")
            print(f"✅ Sucesso! Pasta e arquivo criados em:\n{caminho_arquivo}")
        else:
            print(f"⚠️ O arquivo '{nome_arquivo}' já existe nessa pasta.")
            
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

if __name__ == "__main__":
    criar_pasta_aula()