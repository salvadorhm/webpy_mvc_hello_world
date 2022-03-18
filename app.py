import web  # web.py library

# Define the URL mappings
urls = (
    '/', 'mvc.controllers.public.index.Index'
)

# web.py application
app = web.application(urls, globals())

# Run the application
if __name__ == "__main__":
    web.config.debug = False
    app.run()
