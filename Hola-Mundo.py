import os


def main():
  userName = os.getenv("USERNAME")
  print(f'Hi there, this is {userName} from its Github account just saying hello World! Spread the love! Peace!')
  print(f'Hola Panda, soy {userName} desde mi cuenta de Github solo diciendo hola mundo! Viva el amor! Paz!')
  print(f"Bonjour, c'est {userName} de mon Github compte seleument je veux dire BONJOUR MONDE! VIVE L'AMOUR! PAIX!")

if __name__ == "__main__":
  main()
