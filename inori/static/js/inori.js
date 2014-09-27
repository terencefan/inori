function showInfo(message) {
  $._messengerDefaults = {
    extraClasses: 'messenger-fixed messenger-theme-future messenger-on-bottom'
  }
  $.globalMessenger().post({
    message: message,
    type: 'info',
    showCloseButton: true,
  });
}

function showError(message) {
  $._messengerDefaults = {
    extraClasses: 'messenger-fixed messenger-theme-future messenger-on-top'
  }
  $.globalMessenger().post({
    message: message,
    type: 'error',
    showCloseButton: true,
  });
}

angular.module('inori', [])
.controller('navbarController', [
  '$scope',
  '$http',
  function($scope, $http) {
    console.log('navbarController');
  }
])
.controller('containerController', [
  '$scope',
  '$http',
  function($scope, $http) {
    console.log('containerController');
  }
])
.controller('indexController', [
  '$scope',
  '$http',
  function($scope, $http) {
    console.log('indexController');
  }
])
