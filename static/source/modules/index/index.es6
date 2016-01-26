
function indexSvc($http) {
  return {
    linkList: function() {
      return $http.get('/api/link');
    },
    addLink: function(url) {
      let data = {'url': url};
      return $http.put('/api/link/', data);
    },
  };
}

function indexCtrl($scope, indexSvc) {

  $scope.inori = {
    'image': 'http://www.gravatar.com/avatar/0e7b8e5815e9993efcd1db2b90ed228c?s=300',
    'nickname': '风之小祈',
  };

  function reload() {
    indexSvc.linkList().success(function(data) {
      $scope.links = data.data.links;
    });
  }
  reload();

  $scope.link = {
    add: function() {
      indexSvc.addLink(this.url).success(function(data) {
        reload();
      });
    },
  };

}

inori
.factory('indexSvc', indexSvc)
.controller('indexCtrl', indexCtrl)
;
