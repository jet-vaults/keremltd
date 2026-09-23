/* Kerem: minimal progressive enhancement, no dependencies */
(function () {
  'use strict';
  var d = document, b = d.body, EN = d.documentElement.lang === 'en';

  /* mobile menu */
  var burger = d.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = b.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && b.classList.contains('menu-open')) burger.click(); });
    d.querySelectorAll('.menu a').forEach(function (a) { a.addEventListener('click', function () { if (b.classList.contains('menu-open')) burger.click(); }); });
  }

  /* scroll reveal */
  var rv = d.querySelectorAll('.rv,.rv-img');
  if ('IntersectionObserver' in window && rv.length) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  /* virtual tours: load the embed only when asked */
  d.querySelectorAll('.tour[data-embed]').forEach(function (tour) {
    var btn = tour.querySelector('.tour-open');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var frame = tour.querySelector('.frame');
      var f = d.createElement('iframe');
      f.src = tour.dataset.embed; f.title = tour.dataset.title || ''; f.loading = 'eager';
      f.setAttribute('allow', 'fullscreen; gyroscope; accelerometer'); f.setAttribute('allowfullscreen', '');
      frame.innerHTML = ''; frame.appendChild(f); tour.classList.add('is-open'); f.focus();
    });
  });

  /* contact page: preselect a project from ?project=, show success after a no-JS redirect */
  var params = new URLSearchParams(location.search);
  var preselect = params.get('project'), sel = d.getElementById('f-project');
  if (preselect && sel) { var opt = sel.querySelector('option[data-slug="' + preselect.replace(/[^a-z0-9-]/g, '') + '"]'); if (opt) opt.selected = true; }
  if (params.get('sent') === '1') { var m0 = d.querySelector('.form__msg'); if (m0) { m0.textContent = m0.dataset.sent || ''; m0.className = 'form__msg ok'; } }

  /* sticky contact bar: show unless dismissed this session */
  var stick = d.getElementById('stick');
  if (stick) {
    var dismissed = false;
    try { dismissed = sessionStorage.getItem('kerem-stick') === '1'; } catch (e) {}
    var fit = function () { if (!stick.hidden) d.documentElement.style.setProperty('--stick-h', stick.offsetHeight + 'px'); };
    if (!dismissed) { stick.hidden = false; b.classList.add('has-stick'); fit(); window.addEventListener('resize', fit); }
    var closeBtn = stick.querySelector('.stick-close');
    if (closeBtn) closeBtn.addEventListener('click', function () {
      stick.hidden = true; b.classList.remove('has-stick'); d.documentElement.style.removeProperty('--stick-h');
      try { sessionStorage.setItem('kerem-stick', '1'); } catch (e) {}
    });
  }

  /* forms (Web3Forms JSON endpoint) */
  d.querySelectorAll('form.form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form__msg'), btn = form.querySelector('button[type=submit]');
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var fd = new FormData(form);
      if (fd.get('botcheck')) return;
      btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = EN ? 'Sending…' : 'שולח…';
      msg.className = 'form__msg';
      fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(Object.fromEntries(fd)) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok && j.success, j: j }; }); })
        .then(function (r) {
          if (r.ok) { form.reset(); msg.textContent = EN ? 'Thank you, your enquiry has been received. We will get back to you shortly.' : 'תודה, פנייתכם התקבלה. נציג יחזור אליכם בהקדם.'; msg.className = 'form__msg ok'; msg.focus(); }
          else throw new Error(r.j && r.j.message);
        })
        .catch(function () {
          msg.innerHTML = (EN ? 'We could not send the form right now. Call us at <a href="tel:+97236121314" dir="ltr">03-6121314</a> or write to ' : 'לא הצלחנו לשלוח את הטופס כרגע. ניתן להתקשר אלינו: <a href="tel:+97236121314" dir="ltr">03-6121314</a> או לכתוב ל-') + '<a href="mailto:office@keremltd.co.il">office@keremltd.co.il</a>';
          msg.className = 'form__msg err'; msg.focus();
        })
        .finally(function () { btn.disabled = false; btn.textContent = btn.dataset.t; });
    });
  });
})();
