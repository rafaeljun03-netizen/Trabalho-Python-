import random
saldo=100
simbolos=["🍒","🍋","⭐","🔔"]
while saldo > 0:
    print(f"\nSaldo: {saldo}")
    aposta=int(input("Digite o valor da aposta: "))
    if aposta>saldo:
        print("Tá pobre !Saldo insuficiente!")
        continue
    s1=random.choice(simbolos)
    s2=random.choice(simbolos)
    s3=random.choice(simbolos)
    print(f"|{s1}|{s2}|{s3}|")
    if s1==s2==s3:
        ganho=aposta*3
        saldo+=ganho
        print(f"JACKPOT! Você ganhou {ganho}, tá ricão my friend")
    if s1==s2 or s2==s3 or s1==s3:
        ganho=aposta*2
        saldo+=ganho
        print(f"Ganhou {ganho}, tá cagado hein")
    else:
        saldo-=aposta
        print("Se Ferrou! Perdeu playboy!")
    continuar=input("Quer continuar? (s/n): ")
    if continuar.lower() !="s":
        break
print("Fim de jogo!")