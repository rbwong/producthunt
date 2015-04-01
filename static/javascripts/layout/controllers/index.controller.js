/**
* IndexController
* @namespace thinkster.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Authentication', 'Posts', 'Snackbar', 'Facebook', 'Restangular'];

  /**
  * @namespace IndexController
  */
  function IndexController($scope, Authentication, Posts, Snackbar, Facebook, Restangular) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.posts = new Posts();
    vm.login_fb = login_fb;

    /**
    * @name logout
    * @desc Log the user out
    * @memberOf thinkster.layout.controllers.NavbarController
    */
    function login_fb() {
      Facebook.login().then(function(response){
           //we come here only if JS sdk login was successful so lets
           //make a request to our new view. I use Restangular, one can
           //use regular http request as well.
           var reqObj = {"access_token": response.authResponse.accessToken,
                      "backend": "facebook"};
           var u_b = Restangular.all('sociallogin/');
           u_b.post(reqObj).then(function(response) {
              $location.path('/home');
           }, function(response) { /*error*/
               console.log("There was an error", response);
               //deal with error here.
           });
       });
    }

  }
})();
