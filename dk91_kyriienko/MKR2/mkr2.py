def super_func(rating, times):
	return f'Тимофій Андрійович, посавте будь ласка {rating} :)'

if __name__ == '__main__':
    from colorama import init
    from termcolor import colored
	
    init()

    print(colored(super_func(60), 'white', 'on_green'))