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

  /* lightbox for project imagery */
  var lb = d.getElementById('lightbox'), lbFigs = [].slice.call(d.querySelectorAll('figure.lb'));
  if (lb && lbFigs.length) {
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('figcaption'), lbCount = lb.querySelector('.lb-count'), cur = 0, lastFocus = null;
    var largest = function (fig) {
      var src = fig.querySelector('source[type="image/avif"]'), img = fig.querySelector('img');
      var set = (src && src.srcset) || img.srcset || '';
      var best = null, bw = 0;
      set.split(',').forEach(function (e) { var m = e.trim().split(/\s+/); var w = parseInt(m[1] || '0', 10); if (w > bw) { bw = w; best = m[0]; } });
      return best || img.currentSrc || img.src;
    };
    var show = function (i) {
      cur = (i + lbFigs.length) % lbFigs.length;
      var fig = lbFigs[cur], img = fig.querySelector('img'), cap = fig.querySelector('figcaption');
      lbImg.src = largest(fig); lbImg.alt = img.alt || '';
      lbCap.textContent = cap ? cap.textContent : (img.alt || '');
      lbCount.textContent = (cur + 1) + ' / ' + lbFigs.length;
      [1, -1].forEach(function (k) { var n = lbFigs[(cur + k + lbFigs.length) % lbFigs.length]; if (n) { var pre = new Image(); pre.src = largest(n); } });
    };
    var openLb = function (i) { lastFocus = d.activeElement; show(i); lb.hidden = false; b.classList.add('lb-open'); lb.querySelector('.lb-close').focus(); };
    var closeLb = function () { lb.hidden = true; b.classList.remove('lb-open'); if (lastFocus && lastFocus.focus) lastFocus.focus(); };
    lbFigs.forEach(function (fig, i) {
      var fr = fig.querySelector('.frame'); if (!fr) return;
      fr.setAttribute('role', 'button'); fr.setAttribute('tabindex', '0');
      fr.addEventListener('click', function () { openLb(i); });
      fr.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLb(i); } });
    });
    lb.querySelector('.lb-close').addEventListener('click', closeLb);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(cur - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(cur + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    d.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'Escape') closeLb();
      else if (e.key === 'ArrowRight') show(cur + 1);
      else if (e.key === 'ArrowLeft') show(cur - 1);
    });
    var tx = null;
    lb.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) { if (tx === null) return; var dx = e.changedTouches[0].clientX - tx; tx = null; if (Math.abs(dx) > 40) show(dx < 0 ? cur + 1 : cur - 1); });
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
