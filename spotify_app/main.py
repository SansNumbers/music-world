import base64
import json
import os

from django.http import JsonResponse
from requests import post, get

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')


def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token/'
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    result = post(
        url,
        headers=headers,
        data=data
    )
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token


def search_for_artist(request):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
    }
    url = 'https://api.spotify.com/v1/search'
    query = f"?q={request.GET['artist_name']}&type=artist&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['artists']['items']
    if len(json_result) == 0:
        print('No artists with this name exists.')
        return None
    return JsonResponse(json_result[0])


def search_for_album(request):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
    }
    url = 'https://api.spotify.com/v1/search'
    query = f"?q={request.GET['album_name']}&type=album&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['albums']['items']
    if len(json_result) == 0:
        print('No albums with this name exists.')
        return None
    return JsonResponse(json_result[0])


def search_for_track(request):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
    }
    url = 'https://api.spotify.com/v1/search'
    query = f"?q={request.GET['track_name']}&type=track&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['tracks']['items']
    if len(json_result) == 0:
        print('No tracks with this name exists.')
        return None
    return JsonResponse(json_result[0])


def get_songs_by_artist(request):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
    }
    url = f'https://api.spotify.com/v1/artists/41X1TR6hrK8Q2ZCpp2EqCz/top-tracks/?country=UA'
    result = get(url, headers=headers)
    json_result = json.loads(result.content)

    for idx, song in enumerate(json_result['tracks']):
        print(f"{idx + 1}. {song['name']}")

    return JsonResponse(json_result)
