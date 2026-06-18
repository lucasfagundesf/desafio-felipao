vitorias = input("Digite o número de vitórias do Héroi: ");
derrotas= input("Digite o número de derrotas do Héroi: ");

def calcularRank(vitorias):
    if vitorias < 10:
        return "Ferro";
    elif vitorias < 20:
        return "Bronze";
    elif vitorias < 50:
        return "Prata";
    elif vitorias < 80:
        return "Ouro";
    elif vitorias < 90:
        return "Diamante";   
    elif vitorias < 100:
        return "Lendário";
    elif vitorias > 100:
        return "Imortal";   

def calcularSaldoVitorias(vitorias, derrotas):
    saldo = vitorias - derrotas;
    if saldo < 0:
        return "Negativo";
    elif saldo == 0:
        return "Neutro";
    else:
        return "Positivo";

rank = calcularRank(int(vitorias));
saldoVitorias = calcularSaldoVitorias(int(vitorias), int(derrotas));

print(f"O Héroi tem saldo de {saldoVitorias} e está no nível {rank}.")