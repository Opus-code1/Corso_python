while True:
    try:
        x = int(input(': '))
        print(x)
        break
    except Exception as e:
        print(f'errore: {e}')
        
    
