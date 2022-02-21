def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo mars.jpg")


if __name__ == '__main__':
    main()
