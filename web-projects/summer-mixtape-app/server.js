const express = require('express');
const axios = require('axios');
const querystring = require('querystring');
const path = require('path');
const app = express();
const port = 3000;

const clientId = '5c0ce63c393f47ee9d4774ffca23d912'; // Replace with your Spotify Client ID
const clientSecret = '9d7e8613b590410a95617e8360ba99e3'; // Replace with your Spotify Client Secret
const redirectUri = 'http://localhost:3000/callback';

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Step 1: Direct users to the authorization page
app.get('/login', (req, res) => {
  const scopes = 'user-read-private user-read-email';
  res.redirect('https://accounts.spotify.com/authorize' +
    '?response_type=code' +
    '&client_id=' + clientId +
    (scopes ? '&scope=' + encodeURIComponent(scopes) : '') +
    '&redirect_uri=' + encodeURIComponent(redirectUri));
});

// Step 2: Handle the callback and exchange code for access token
app.get('/callback', (req, res) => {
  const code = req.query.code || null;
  const authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    form: {
      code: code,
      redirect_uri: redirectUri,
      grant_type: 'authorization_code'
    },
    headers: {
      'Authorization': 'Basic ' + (Buffer.from(clientId + ':' + clientSecret).toString('base64'))
    },
    json: true
  };

  axios.post(authOptions.url, querystring.stringify(authOptions.form), { headers: authOptions.headers })
    .then(response => {
      const accessToken = response.data.access_token;
      // Save the access token and use it for API requests
      res.redirect('/?access_token=' + accessToken);
    })
    .catch(error => {
      console.error(error);
      res.send('Error retrieving access token');
    });
});

// Add a route for the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
