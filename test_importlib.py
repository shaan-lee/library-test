
def tmp():
    logging = __import__('logging')
    click = __import__("click.py")

    logging.info("import logging succeced")
    click.sleep1()

