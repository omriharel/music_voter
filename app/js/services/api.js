function apiService($http) {
  'ngInject';

  const service = {};

  service.get = function() {
    return new Promise((resolve, reject) => {
      $http.get('apiPath').success((data) => {
        resolve(data);
      }).error((err, status) => {
        reject(err, status);
      });
    });
  };

  service.getSongs = function() {
    return [
    {title: 'Everybody Talks', votes: 3, videoId: '', thumbnail: 'http://i.imgur.com/Zd9zKCC.jpg'},
    {title: 'The Wrath of Code', votes: 0, videoId: '', thumbnail: 'http://i.imgur.com/boiOxG9.jpg'},
    {title: 'Bohemian Rhapsody', votes: 4, videoId: '', thumbnail: 'http://i.imgur.com/4HgFCsT.jpg'},
    {title: 'Teardrop', votes: 1, videoId: '', thumbnail: 'http://i.imgur.com/5NW4pbx.jpg'},
    {title: 'San Francisco', votes: 2, videoId: '', thumbnail: 'http://i.imgur.com/uJgikKu.jpg'},
    {title: 'Chelsea Dagger', votes: 3, videoId: '', thumbnail: 'http://i.imgur.com/wVGjPzH.jpg'},
    {title: 'The Seeker', votes: 5, videoId: '', thumbnail: 'http://i.imgur.com/AypRTE3.jpg'}
    ];
  };

  return service;

}

export default {
  name: 'apiService',
  fn: apiService
};
