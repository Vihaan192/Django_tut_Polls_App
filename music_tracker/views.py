from django.shortcuts import render
from .music_api import fetch_lastfm

# Create your views here.
def country_view(request):
    countries = ['United States', 'United Kingdom', 'Germany', 'France', 'Japan', 'Canada', 'Spain', 'India', 'Ireland']
    country = request.GET.get('country', 'India')
    artists= fetch_lastfm('geo.getTopArtists', {'country': country})
    tracks = fetch_lastfm('geo.getTopTracks', {'country': country})
    context = {
        'country': country,
        'countries': countries,
        'artists': artists.get('topartists', {}).get('artist', [])[:10] if artists else [],
        'tracks': tracks.get('tracks', {}).get('track', [])[:10] if tracks else [],
    }
    return render(request, 'music_tracker/country.html', context)

def search_view(request):
    artists, albums, tracks = [], [], []
    query = request.GET.get('q', '')
    if query:
        artist_data = fetch_lastfm('artist.search', {'artist': query})
        album_data = fetch_lastfm('album.search', {'album': query})
        track_data = fetch_lastfm('track.search', {'track': query})

        if artist_data:
            artists = artist_data.get('results', {}).get('artistmatches', {}).get('artist', [])[:10]
        if album_data:
            albums = album_data.get('results', {}).get('albummatches', {}).get('album', [])[:10]
        if track_data:
            tracks = track_data.get('results', {}).get('trackmatches', {}).get('track', [])[:10]
    context = {
        'query': query,
        'artists': artists,
        'albums': albums,
        'tracks': tracks,
    }
    return render(request, 'music_tracker/search.html', context)

def similar_view(request):
    query = request.GET.get('q', '')
    sim = []

    if query:
        sim_data = fetch_lastfm('artist.getSimilar',{'artist':query})

        if sim_data:
            sim = sim_data.get('similarartists',{}).get('artist',[])[:10]
    context = {
        'query' : query,
        'similar_artists': sim,
    }
    return render(request, 'music_tracker/sim.html',context)