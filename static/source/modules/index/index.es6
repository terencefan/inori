function indexCtrl($scope) {

  $scope.inori = {
    'image': 'http://www.gravatar.com/avatar/0e7b8e5815e9993efcd1db2b90ed228c?s=300',
    'nickname': '风之小祈',
  };

  $scope.links = [
    {
      'title': "Python 魔术方法指南 — PyCoder's Weelky CN",
      'icon': 'http://pycoders-weekly-chinese.readthedocs.org/favicon.ico',
      'url': 'http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue6/a-guide-to-pythons-magic-methods.html',
    },
  ];

  $scope.addLink = function() {
    console.log($scope.url);
  };

}

inori
.controller('indexCtrl', indexCtrl)
;
