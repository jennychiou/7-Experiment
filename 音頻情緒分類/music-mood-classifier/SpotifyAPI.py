import spotipy
import spotipy.util as util

username = 'o7dgqfjas82wkfhhwljkw7w7b'
scope = 'user-library-read'
util.prompt_for_user_token(username,scope,client_id='56585547a2104e1bac19f149e1e3db0f',client_secret='a13333899bd14cbc895eed52e9cf6484',redirect_uri='http://localhost/')
