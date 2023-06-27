all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username]=all_users.setdefault(username,[albums,age,city])
    # for album in albums:
    #     all_users[username].append(album)


    pass


def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name]=all_albums.setdefault(name,[artist_name,tracks,genre])
    
    pass


def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    counter=0
    for album in all_users[username][0]:
        if all_albums[album][0]==artist_name:

            counter+=all_albums[album][1]
    return counter

    pass


def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    counter=0
    for album in all_users[username][0]:
        if all_albums[album][2]==genre:
            counter+=all_albums[album][1]
    
    return counter


    pass


def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    counter=0
    for user in all_users:
        if all_users[user][1]==age:
            for album in all_users[user][0]:
                if all_albums[album][0]==artist_name:
                    counter+=all_albums[album][1]

    return counter    


    pass


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    counter=0
    for user in all_users:
        if all_users[user][1]==age:
            for album in all_users[user][0]:
                if all_albums[album][2]==genre:
                    counter+=all_albums[album][1]

    return counter

    pass


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    counter=0
    for user in all_users:
        if all_users[user][2]==city:
            for album in all_users[user][0]:
                if all_albums[album][0]==artist_name:
                    counter+=all_albums[album][1]

    return counter
    pass


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    counter=0
    for user in all_users:
        if all_users[user][2]==city:
            for album in all_users[user][0]:
                if all_albums[album][2]==genre:
                    counter+=all_albums[album][1]

    return counter

    pass

# DO NOT USE YOUR OWN TESTS HERE, USE SAMPLE TEST INSTEAD
