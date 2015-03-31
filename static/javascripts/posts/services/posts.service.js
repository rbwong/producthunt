/**
* Posts
* @namespace thinkster.posts.services
*/
(function () {
  'use strict';

  angular
    .module('thinkster.posts.services')
    .factory('Posts', Posts);

  Posts.$inject = ['$http'];

  /**
  * @namespace Posts
  * @returns {Factory}
  */
  function Posts($http) {

    var Posts = function() {
        this.items = [];
        this.busy = false;
        this.after = 0;
      };

    Posts.prototype.nextPage = function() {
      if (this.busy) return;
      this.busy = true;

      var url = "/api/v1/posts?days_ago=" + this.after;
      $http.get(url).success(function(data) {
        var items = data;

        for (var i = 0; i < items.length; i++) {
          //add header
          if (i == 0) {
            items[i].header = true;
          }
          else {
            items[i].header = false;
          }
          this.items.push(items[i]);
        }
        this.after++;
        this.busy = false;
      }.bind(this));
    };

    ////////////////////

    /**
    * @name all
    * @desc Get all Posts
    * @returns {Promise}
    * @memberOf thinkster.posts.services.Posts
    */
    Posts.all = function() {
      return $http.get('/api/v1/posts/all');
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {string} content The content of the new Post
    * @returns {Promise}
    * @memberOf thinkster.posts.services.Posts
    */
     Posts.create = function(name) {
      return $http.post('/api/v1/posts', {
        name: name
      });
    };

    /**
     * @name get
     * @desc Get the Posts of a given user
     * @param {string} username The username to get Posts for
     * @returns {Promise}
     * @memberOf thinkster.posts.services.Posts
     */
    Posts.get = function (username) {
      return $http.get('/api/v1/accounts/' + username + '/posts');
    }

    return Posts;
  }
})();
