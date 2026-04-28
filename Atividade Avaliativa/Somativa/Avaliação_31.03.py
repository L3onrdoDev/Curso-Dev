# ---------------------------------------------------------
# 1. Perfil de Gamer 🎮
# ---------------------------------------------------------
print("✨ Seja Bem-Vindo(a) à Revision Company ✨")
print("🚀 Vamos configurar seu perfil de jogador!")

nome = input("👤 Digite seu nick: ")
nivel = int(input("⚔️ Digite seu nível atual: "))

print(f"\n✅ O jogador {nome} está no nível {nivel} e pronto para a partida! 🔥")

# ---------------------------------------------------------
# 2. Calculadora de Mesada 💰
# ---------------------------------------------------------
print("\n💵 Calculadora De Mesada 💵")
print("Gerencie suas economias mensais de forma rápida.")

valor_recebido = float(input("💰 Quanto você ganha por semana? R$ "))
valor_final = valor_recebido * 4

print(f"📊 No final do mês, você terá um total de: R$ {valor_final} 🤑")

# ---------------------------------------------------------
# 3. Conversor de Internet 🌐
# ---------------------------------------------------------
print("\n⚡ Conversor De Internet (GB para MB) ⚡")

GB = int(input("💾 Digite a quantidade de GB: "))
valor_final = GB * 1024

print("✨ Convertendo dados...")
print(f"📡 Resultado: {GB}GB equivalem a {valor_final} MB! 🚀")

# ---------------------------------------------------------
# 4. Média de Notas 🎓
# ---------------------------------------------------------
print("\n📚 Calculadora de Média Escolar 📚")

nota_matematica = float(input("🔢 Nota de Matemática: "))
nota_portugues = float(input("📝 Nota de Português: "))

media = (nota_matematica + nota_portugues) / 2

print(f"🎯 Sua média final é: {media:.1f}")
if media >= 6:
    print("🎉 Parabéns! Você está indo muito bem!")

# ---------------------------------------------------------
# 5. Seguidores 📱
# ---------------------------------------------------------
print("\n📸 Status das Redes Sociais 📸")

seguidores_atual = int(input("👥 Quantos seguidores você já tem? "))
seguidores_novos = int(input("📈 Quantos seguidores ganhou hoje? "))

total = seguidores_atual + seguidores_novos

print(f"✨ Uhul! Você ganhou {seguidores_novos} novos amigos hoje!")
print(f"🌟 Seu perfil agora conta com {total} seguidores! 🚀")

# ---------------------------------------------------------
# 6. Idade em Dias ⏳
# ---------------------------------------------------------
print("\n🗓️ Linha do Tempo 🗓️")

idade = int(input("🎂 Digite sua idade: "))
dias_vividos = idade * 365

print(f"🕰️ Você já viveu aproximadamente {dias_vividos} dias na Terra! 🌍")

# ---------------------------------------------------------
# 7. Consumo de Lanche 🍔
# ---------------------------------------------------------
print("\n🍕 Hora do Lanche! 🥤")

salgado = float(input("🥐 Preço do salgado: R$ "))
suco = float(input("🧃 Preço do suco: R$ "))

total_conta = salgado + suco

print(f"💳 O valor total do seu lanche foi: R$ {total_conta:.2f} 😋")

# ---------------------------------------------------------
# 8. Ano de Nascimento 🎈
# ---------------------------------------------------------
print("\n🔍 Detector de Nascimento 🔍")

ano_atual = int(input("📅 Em que ano estamos? "))
idade_nasc = int(input("👤 Qual sua idade? "))

ano_nasc = ano_atual - idade_nasc

print(f"🎂 De acordo com meus cálculos, você nasceu em {ano_nasc}! ✨")

# ---------------------------------------------------------
# 9. Filtro de Idade (TikTok) 📱
# ---------------------------------------------------------
print("\n🔐 Verificação de Segurança (Filtro) 🔐")

idade_user = int(input("🔞 Digite sua idade para acessar: "))

if idade_user < 13:
    print("🚫 Acesso restrito! (Conteúdo Kids)")
elif idade_user <= 17:
    print("⚠️ Acesso moderado! (Conteúdo Teen)")
else:
    print("🔓 Acesso liberado! (Conteúdo Adulto)")

# ---------------------------------------------------------
# 10. Bateria do Celular 🔋
# ---------------------------------------------------------
print("\n🔋 Status da Bateria 🔋")

bateria = 100
while bateria > 10:
    bateria -= 10
    print(f"⚡ Descarregando... {bateria}%")

print("🛑 Bateria Crítica! Por favor, conecte o carregador! 🔌")

# ---------------------------------------------------------
# 11. Contagem de Curtidas ❤️
# ---------------------------------------------------------
print("\n❤️ Simulador de Engajamento ❤️")

limite = int(input("📸 Quantas curtidas você quer na sua foto? "))

for i in range(1, limite + 1):
    print(f"❤️ Curtida nº {i} recebida!")
    
print(f"✨ Sucesso! Sua foto alcançou {limite} curtidas! ⭐")

# ---------------------------------------------------------
# 12. Carrinho de Compras Online 🛒
# ---------------------------------------------------------
print("\n🛒 Carrinho de Compras 🛒")

contador_itens = 0
while True:
    produto = input("🛍️ Produto (ou digite 'sair' para fechar): ")

    if produto.lower() == "sair":
        break

    if produto.strip() == "":
        continue

    contador_itens += 1
    print(f"✅ '{produto}' adicionado com sucesso!")

print(f"\n📦 Checkout finalizado!")
print(f"🛒 Você adicionou {contador_itens} item(ns) ao seu carrinho. Volte sempre! 👋")
