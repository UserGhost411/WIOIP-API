import lib.model as model
class Router:
    @staticmethod
    def run(app):
        @app.route('/')
        def root():
            return model.getRootData()
        @app.route('/weather')
        @app.route('/weather/<type>/<region>')
        def weather_info(type="all",region=""):
            return model.getWeather(type,region)
        @app.route('/region/<page>')
        def region_search(page="surabaya"):
            return model.region(page)
