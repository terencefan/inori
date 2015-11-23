function indexCtrl($scope) {

  $scope.inori = {
    'image': 'http://www.gravatar.com/avatar/0e7b8e5815e9993efcd1db2b90ed228c?s=300',
    'nickname': '风之小祈',
  };

  $scope.links = [
    {
      'name': 'Github',
      'link': 'https://github.com/stdrickforce',
      'image': '/static/source/images/logo/github.png',
    },
    {
      'name': 'wow',
      'link': 'http://www.battlenet.com.cn/wow/zh/character/%E6%96%AF%E5%9D%A6%E7%B4%A2%E5%A7%86/%E9%A3%8E%E4%B9%8B%E5%B0%8F%E7%A5%88/advanced',
      'image': '/static/source/images/logo/wow.png',
    },
    {
      'name': '微博',
      'link': 'http://weibo.com/3752876962/profile?topnav=1&wvr=6',
      'image': '/static/source/images/logo/weibo.jpg',
    },
    {
      'name': '知乎',
      'link': 'http://www.zhihu.com/people/fan-teng-yuan',
      'image': '/static/source/images/logo/zhihu.jpg',
    },
  ];

}

inori
.controller('indexCtrl', indexCtrl)
;
