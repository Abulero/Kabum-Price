from KabumScraping import KabumScraping
import sys


if __name__ == '__main__':
    args_list = sys.argv.pop(0)
    product = ''

    if len(sys.argv) == 0:
        print('Please type the name of a product as an argument')
        sys.exit()

    for arg in sys.argv:
        product += arg

    Kabum_Scraping = KabumScraping(product)

    for i in range(10):
        name, price = Kabum_Scraping.get_price(i)

        if name == None:
            break

        print('-----{name}\n{price}\n'.format(name=name, price=price))
