#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  // 1. Fetch movie data
  request(`${API_URL}/films/${process.argv[2]}/`, (error, response, body) => {
    if (error) {
      console.error(error);
      return; // Exit if error occurs
    }

    // 2. Extract character URLs
    const characters = JSON.parse(body).characters;

    // 3. Function to fetch and print character names
    const getCharacterName = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (err, _, characterBody) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(characterBody).name);
          }
        });
      });
    };

    // 4. Promise.all for parallel character fetches
    Promise.all(characters.map(getCharacterName))
      .then(names => console.log(names.join('\n')))
      .catch(error => console.error(error));
  });
}
