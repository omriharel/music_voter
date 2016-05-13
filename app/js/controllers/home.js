function HomeController(apiService) {
  'ngInject';

  // ViewModel
  const vm = this;
  vm.songs = apiService.getSongs();
}

export default {
  name: 'HomeController',
  fn: HomeController
};
