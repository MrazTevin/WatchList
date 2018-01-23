class Config:
    '''
    General configuration parent class
    '''

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/550?api_key=d440519c73b9358520adf910ad906846'

    pass


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
    pass

    DEBUG = True
