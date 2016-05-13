function OnConfig($stateProvider, $locationProvider, $urlRouterProvider, $mdThemingProvider) {
  'ngInject';

  $locationProvider.html5Mode(true);

  $mdThemingProvider.theme('default').dark();

  $stateProvider
  .state('Home', {
    url: '/',
    controller: 'HomeController as home',
    templateUrl: 'home.html',
    title: 'Home'
  });

  $urlRouterProvider.otherwise('/');
}

export default OnConfig;
