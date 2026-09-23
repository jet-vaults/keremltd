/* Kerem — minimal progressive enhancement, no dependencies */
(function () {
  'use strict';
  var d = document, b = d.body;

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

  /* forms (Web3Forms JSON endpoint) */
  d.querySelectorAll('form.form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form__msg'), btn = form.querySelector('button[type=submit]');
      var fd = new FormData(form);
      if (fd.get('botcheck')) return;
      btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = 'שולח…';
      msg.className = 'form__msg';
      fetch(form.action, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(Object.fromEntries(fd)) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok && j.success, j: j }; }); })
        .then(function (r) {
          if (r.ok) { form.reset(); msg.textContent = 'תודה, פנייתכם התקבלה. נציג יחזור אליכם בהקדם.'; msg.className = 'form__msg ok'; }
          else throw new Error(r.j && r.j.message);
        })
        .catch(function () {
          msg.innerHTML = 'לא הצלחנו לשלוח את הטופס כרגע. ניתן להתקשר אלינו: <a href="tel:+97236121314" dir="ltr">03-6121314</a> או לכתוב ל-<a href="mailto:office@keremltd.co.il">office@keremltd.co.il</a>';
          msg.className = 'form__msg err';
        })
        .finally(function () { btn.disabled = false; btn.textContent = btn.dataset.t; });
    });
  });
})();
