from captiongram import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

def start_ngrok():
    from pyngrok import ngrok

    url = ngrok.connect(5000)
    print(' * Tunnel URL:', url)

if app.config['START_NGROK']:
    start_ngrok()