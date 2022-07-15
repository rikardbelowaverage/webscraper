try:
    from scrape import storeScrape
    from scrape import scrape
    from gui import startGui
    import json
    import pandas as pd
    from io import StringIO

except ModuleNotFoundError:
    print('Please download dependencies from requirement.txt')
except Exception as ex:
    print(ex)

if __name__ == '__main__':
    startGui()