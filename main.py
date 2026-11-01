from input.User import escolher_personagem

if __name__ == '__main__':
    usr_input = input("Com quem você quer conversar?")
    conversando = escolher_personagem(usr_input)
    print(conversando)
