#!/usr/bin/env python3

def eh_par(int_num):
    eh_num_par = False
    if int_num % 2 == 0:
        eh_num_par = True
    return eh_num_par

def multiplica_por_dois(int_num):
    return int_num * 2

def multiplica_por_dois_se_for_par(int_num):
    if eh_par(int_num):
        return multiplica_por_dois(int_num)
    else:
        return int_num

def subtrai_cinco(int_num):
    print(int_num)
    return int_num - 5


def print_all(nome, idade, resultado_multiplicacao):
    print("### Olá {}, sua idade é {}, e o resultado da multiplicação se for par é {} ###".format(nome, idade, str(resultado_multiplicacao)))


def complexa(idade, int_num):
    if eh_par(int_num) and int(idade) >= 18:
        return multiplica_por_dois(int_num)
    return int_num


def main():
    name = input('Qual o seu Nome? ')
    print('O seu nome é {}.'.format(name))
    idade = input('Qual é a sua Idade {}? '.format(name))
    print('Oi {}! Sua idade é {} anos.'.format(name, idade))
    int_number = int(input('Digite um numero: '))
    print(eh_par(int_number))
    resultado_multiplica = multiplica_por_dois_se_for_par(int_number)
    print(resultado_multiplica)
    print_all(name, idade, resultado_multiplica)
    print_all("João Pedro", "12", 7)
    resultado_subitrai_cinco = subtrai_cinco(int_number)
    print(multiplica_por_dois(resultado_subitrai_cinco))
    print(complexa(idade, int_number))

if __name__ == "__main__":
    main()
