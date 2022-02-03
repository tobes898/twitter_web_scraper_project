from time import sleep
import webscrapper

def main():
    #webscrapper.monitorTwitterAccount('Warcraft')
    users = ['Warcraft', 'towelthetank']
    webscrapper.getMultipleTimelines(users)

main()