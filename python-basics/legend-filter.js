// Interactive legend: click to highlight matching syntax tokens
(function () {
  var filterMap = {
    '关键字': 'filter-kw',
    '函数':   'filter-fn',
    '字符串': 'filter-st',
    '数字':   'filter-nm',
    '参数':   'filter-pa',
    '变量':   'filter-vr',
    '运算符': 'filter-op',
    '注释':   'filter-cm'
  };

  var lines = document.querySelector('.lines');
  if (!lines) return;

  document.querySelectorAll('.legend-item').forEach(function (item) {
    item.addEventListener('click', function () {
      var label = item.textContent.trim();
      var cls = filterMap[label];
      if (!cls) return;

      // Toggle off if already active
      if (item.classList.contains('active')) {
        item.classList.remove('active');
        lines.classList.remove('filter-active', cls);
        return;
      }

      // Clear previous
      document.querySelectorAll('.legend-item.active').forEach(function (el) {
        el.classList.remove('active');
      });
      lines.className = 'lines';

      // Activate
      item.classList.add('active');
      lines.classList.add('filter-active', cls);
    });
  });
})();
