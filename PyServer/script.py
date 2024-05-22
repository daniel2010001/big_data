import sys

def main():
    print("Manden el .py v:!")
    if len(sys.argv) > 1:
        print(f"Argumentos recibidos: {sys.argv[1:]}")

if __name__ == "__main__":
    main()