(function () {
  'use strict';

  angular
    .module('thinkster.config')
    .config(config);

  config.$inject = ['$locationProvider', '$translateProvider'];

  /**
  * @name config
  * @desc Enable HTML5 routing
  */
  function config($locationProvider, $translateProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');

    $translateProvider.translations('en', {
        a_day_ago: 'Yesterday',
        just_now: 'Today',
        a_minute_ago: 'Today',
        minutes_ago: 'Today',
        an_hour_ago: 'Today',
        hours_ago: 'Today',
        seconds_ago: 'Today',
        days_ago: '{{time}} days ago'
    });
    $translateProvider.preferredLanguage('en');
  }
})();
