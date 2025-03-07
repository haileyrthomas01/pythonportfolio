document.addEventListener('DOMContentLoaded', function() {
    const accessToken = new URLSearchParams(window.location.search).get('access_token');
    if (!accessToken) {
        alert('No access token found. Please login.');
    }

    document.getElementById('song-form').addEventListener('submit', async function(event) {
        event.preventDefault();
        const songInput = document.getElementById('song');
        const songName = songInput.value.trim();

        if (songName) {
            const songData = await fetchSongData(songName, accessToken);
            if (songData) {
                const li = document.createElement('li');
                li.textContent = `${songData.name} by ${songData.artists[0].name}`;
                document.getElementById('playlist').appendChild(li);
                songInput.value = '';
            } else {
                alert('Song not found');
            }
        }
    });
});

async function fetchSongData(query, accessToken) {
    try {
        const response = await fetch(`https://api.spotify.com/v1/search?q=${encodeURIComponent(query)}&type=track`, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
        const data = await response.json();
        return data.tracks.items[0];
    } catch (error) {
        console.error('Error fetching song data:', error);
    }
}
