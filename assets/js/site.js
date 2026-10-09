/* The theme button and the guides that open from a link. Everything works without this file: the page follows the phone's theme. */
(function () {
  var root = document.documentElement;
  var colors = { light: "#faf3e3", dark: "#1f0f0c" };

  function effective() {
    var chosen = root.getAttribute("data-theme");
    if (chosen === "light" || chosen === "dark") return chosen;
    return window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function label(button) {
    var next = effective() === "dark" ? "light" : "dark";
    button.setAttribute("aria-label", button.getAttribute(next === "dark" ? "data-to-dark" : "data-to-light"));
    var tag = document.querySelectorAll('meta[name="theme-color"]');
    for (var i = 0; i < tag.length; i++) tag[i].setAttribute("content", colors[effective()]);
  }

  var button = document.querySelector(".theme-toggle");
  if (button) {
    label(button);
    button.addEventListener("click", function () {
      var next = effective() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
      label(button);
    });
    if (window.matchMedia) {
      var query = matchMedia("(prefers-color-scheme: dark)");
      var follow = function () { label(button); };
      if (query.addEventListener) query.addEventListener("change", follow);
    }
  }

  function openTarget() {
    var el = location.hash && document.getElementById(location.hash.slice(1));
    if (el && el.tagName === "DETAILS") { el.open = true; el.scrollIntoView(); }
  }
  addEventListener("hashchange", openTarget);
  openTarget();
})();
