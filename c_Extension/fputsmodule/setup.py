from distutils.core import setup, Extension

def main():
    setup(name="fputs",
          version="1",
          description="Python interface for the fputs C library function",
          author="Anshul Saraf",
          author_email="anshulsaraf3@gmail.com",
          ext_modules=[Extension("fputs", ["fputsmodule.c"])])

if __name__ == "__main__":
    main()