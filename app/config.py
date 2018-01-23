class Config:
    '''
    General configuration parent class
    '''

    MOVIE_API_BASE_URL = 'http://api.themoviedb.org/3/movie/{}?api_key={}'


class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
    Config: The parent configuration class with general configuration settings
    '''

    DEBUG = True
