(function () {
  var key = 'va-disable';

  function isDisabled() {
    try {
      return Boolean(localStorage.getItem(key));
    } catch (error) {
      return false;
    }
  }

  try {
    var url = new URL(window.location.href);
    var notrack = url.searchParams.get('notrack');

    if (notrack === '1' || notrack === '0') {
      try {
        if (notrack === '1') localStorage.setItem(key, '1');
        else localStorage.removeItem(key);
      } catch (error) {}

      url.searchParams.delete('notrack');
      history.replaceState(history.state, '', url.pathname + url.search + url.hash);
    }
  } catch (error) {}

  window.va = window.va || function () {
    (window.vaq = window.vaq || []).push(arguments);
  };

  window.va('beforeSend', function (event) {
    return isDisabled() ? null : event;
  });

  window.biAnalytics = {
    track: function (name, data) {
      if (!isDisabled()) window.va('event', { name: name, data: data });
    },
  };
})();
