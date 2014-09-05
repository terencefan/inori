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
