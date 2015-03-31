(function () {
  'use strict';

  angular
    .module('thinkster.posts', [
      'thinkster.posts.controllers',
      'thinkster.posts.directives',
      'thinkster.posts.services',
      'infinite-scroll',
      'relativeDate'
    ]);

  angular
    .module('thinkster.posts.controllers', []);

  angular
    .module('thinkster.posts.directives', ['ngDialog']);

  angular
    .module('thinkster.posts.services', []);
})();
