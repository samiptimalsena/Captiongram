from captiongram import create_app

app = create_app()

def start_ngrok():
    from pyngrok import ngrok

    url = ngrok.connect(5000)
    print(' * Tunnel URL:', url)

if __name__ == '__main__':
    app.run()


if app.config['START_NGROK']:
    start_ngrok()


    
