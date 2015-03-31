(function () {
  'use strict';

  angular
    .module('thinkster', [
      'thinkster.config',
      'thinkster.routes',
      'thinkster.utils',
      'thinkster.authentication',
       'thinkster.layout',
       'thinkster.posts',
       'thinkster.profiles',
    ]);

  angular
    .module('thinkster.config', ['pascalprecht.translate']);

  angular
    .module('thinkster.routes', ['ngRoute']);

  angular
    .module('thinkster')
    .run(run);

  run.$inject = ['$http'];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
