(function(){
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // nav: hide on scroll down, solid once off the top
  const nav = document.getElementById('nav'); let last = 0;
  const darkHead=document.querySelector('.hero, .page-hero');
  function navState(){ const y=scrollY; const hh=darkHead?darkHead.getBoundingClientRect().height:0; const over=!!darkHead && y<hh-70; nav.classList.toggle('hide', y>last && y>240); nav.classList.toggle('solid', !over && y>60); nav.classList.toggle('over', over); last=y; }
  addEventListener('scroll', navState, {passive:true}); navState();

  // drawer
  const drawer = document.getElementById('drawer');
  const openD=()=>{drawer.classList.add('open'); document.body.classList.add('locked');};
  const closeD=()=>{drawer.classList.remove('open'); document.body.classList.remove('locked');};
  document.getElementById('open').onclick = openD;
  document.getElementById('close').onclick = closeD;
  drawer.querySelectorAll('a').forEach(a=>a.addEventListener('click', closeD));
  const drimg=document.getElementById('drimg');
  if(drimg){ drawer.querySelectorAll('.dr-links a[data-img]').forEach(a=>a.addEventListener('mouseenter',()=>{ if(drimg.getAttribute('src')===a.dataset.img) return; drimg.classList.add('fade'); setTimeout(()=>{drimg.src=a.dataset.img; drimg.onload=()=>drimg.classList.remove('fade');},250); })); }
  addEventListener('keydown', e=>{ if(e.key==='Escape') closeD(); });

  // image reveals (clip lives on the img, so the observer sees the box)
  document.querySelectorAll('.reveal').forEach(el=>el.classList.add('in'));



  // floating dish on menu hover
  const fl=document.getElementById('float');
  if(fl){
    const fli=fl.querySelector('img'); let fx=0,fy=0,tx=0,ty=0,on=false;
    document.querySelectorAll('.menu-row[data-img], .course[data-img]').forEach(r=>{
      r.addEventListener('mouseenter',e=>{fli.src=r.dataset.img; fx=tx=e.clientX+150; fy=ty=e.clientY; on=true; fl.classList.add('on'); loop();});
      r.addEventListener('mousemove',e=>{tx=e.clientX+150; ty=e.clientY;});
      r.addEventListener('mouseleave',()=>{on=false; fl.classList.remove('on');});
    });
    function loop(){ fx+=(tx-fx)*.15; fy+=(ty-fy)*.15; fl.style.left=fx+'px'; fl.style.top=fy+'px'; if(on||Math.abs(tx-fx)>.5) requestAnimationFrame(loop); }
  }

  // newsletter (no backend yet)
  document.querySelectorAll('form.news').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault(); f.querySelector('input').value=''; f.querySelector('button').textContent='Thank you';}));

  // ---------- make every silent loop play, including iOS Low Power Mode ----------
  const loops=[...document.querySelectorAll('video[muted][autoplay]')];
  function kick(){ loops.forEach(v=>{ v.muted=true; const p=v.play(); if(p&&p.catch) p.catch(()=>{}); }); }
  kick();
  const vio=new IntersectionObserver(es=>es.forEach(e=>{ const v=e.target; if(e.isIntersecting){ v.muted=true; v.play().catch(()=>{}); } }),{threshold:.1});
  loops.forEach(v=>vio.observe(v));
  ['touchstart','pointerdown','scroll'].forEach(ev=>addEventListener(ev,function once(){ kick(); removeEventListener(ev,once); },{passive:true}));
  document.addEventListener('visibilitychange',()=>{ if(!document.hidden) kick(); });

  // ---------- page transitions ----------
  const veil=document.createElement('div'); veil.className='veil'; document.body.appendChild(veil);
  requestAnimationFrame(()=>requestAnimationFrame(()=>document.body.classList.add('ready')));
  document.addEventListener('click',e=>{
    const a=e.target.closest('a[href]'); if(!a) return;
    const href=a.getAttribute('href');
    if(!href||href.startsWith('#')||href.startsWith('mailto:')||href.startsWith('tel:')||a.target==='_blank'||/^https?:/.test(href)||e.metaKey||e.ctrlKey||e.shiftKey||reduce) return;
    e.preventDefault(); document.body.classList.add('leaving');
    setTimeout(()=>{ location.href=href; }, 650);
  });
  addEventListener('pageshow',e=>{ if(e.persisted) document.body.classList.remove('leaving'); });

  // ---------- cinematic layer ----------
  const ph1=document.querySelector('.page-hero h1');
  if(ph1){ ph1.innerHTML=ph1.textContent.split(' ').map((w,i)=>`<span class="w" style="transition-delay:${200+i*90}ms">${w}</span>`).join(' '); requestAnimationFrame(()=>requestAnimationFrame(()=>{ph1.classList.add('in'); ph1.closest('.page-hero').classList.add('in');})); }
  if(!reduce){ const pio=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.remove('pre'); pio.unobserve(e.target);} }),{threshold:.12});
    document.querySelectorAll('.ph').forEach(el=>{ if(el.closest('.page-hero,.dr-pic,.filmstrip,.chapters')) return; const r=el.getBoundingClientRect(); if(r.top>innerHeight){ el.classList.add('pre'); pio.observe(el);} }); }
  document.querySelectorAll('.ph img[alt]').forEach(img=>{ const el=img.closest('.ph'); if(!el||el.closest('.page-hero,.dr-pic,.mcard,.chapters,.filmstrip')||!img.alt) return; const sh=document.createElement('span'); sh.className='hshade'; const c=document.createElement('span'); c.className='hc'; c.textContent=img.alt; el.appendChild(sh); el.appendChild(c); });
  if(matchMedia('(hover:hover)').matches && innerWidth>860 && !reduce){
    const cur=document.createElement('div'); cur.className='cur'; document.body.appendChild(cur); document.body.classList.add('has-cur');
    let cx=0,cy=0,tx=0,ty=0,shown=false;
    addEventListener('mousemove',e=>{ tx=e.clientX; ty=e.clientY; if(!shown){shown=true; cx=tx; cy=ty; cur.classList.add('show');} },{passive:true});
    document.addEventListener('mouseleave',()=>cur.classList.remove('show')); document.addEventListener('mouseenter',()=>{ if(shown) cur.classList.add('show'); });
    (function loop(){ cx+=(tx-cx)*.2; cy+=(ty-cy)*.2; cur.style.transform=`translate(${cx}px,${cy}px) translate(-50%,-50%)`; requestAnimationFrame(loop); })();
    document.addEventListener('mouseover',e=>{ const t=e.target.closest('a,button,.ph,.mcard,.course,.menu-row,.filmstrip'); cur.classList.toggle('big',!!t); });
  }
  const stage=document.querySelector('.chapters .stage');
  if(stage){
    const imgs=[...stage.querySelectorAll('img')], num=stage.querySelector('.cnum'), chps=[...document.querySelectorAll('.chapter-list .chp')];
    function setLive(i){ chps.forEach((c,k)=>c.classList.toggle('live',k===i)); imgs.forEach((im,k)=>im.classList.toggle('live',k===(i%imgs.length))); if(num) num.textContent=String(i+1).padStart(2,'0'); }
    const cio=new IntersectionObserver(es=>{ es.forEach(e=>{ if(e.isIntersecting) setLive(chps.indexOf(e.target)); }); },{rootMargin:'-45% 0px -45% 0px'});
    chps.forEach(c=>cio.observe(c)); setLive(0);
  }
  document.querySelectorAll('.filmstrip').forEach(f=>{ let down=false,sx=0,sl=0;
    f.addEventListener('pointerdown',e=>{down=true;sx=e.clientX;sl=f.scrollLeft;f.classList.add('drag');});
    f.addEventListener('pointermove',e=>{ if(!down) return; f.scrollLeft=sl-(e.clientX-sx); });
    ['pointerup','pointercancel','pointerleave'].forEach(ev=>f.addEventListener(ev,()=>{down=false;f.classList.remove('drag');}));
    f.addEventListener('wheel',e=>{ if(Math.abs(e.deltaY)>Math.abs(e.deltaX)){ f.scrollLeft+=e.deltaY; e.preventDefault(); } },{passive:false});
  });

  // ---------- homepage hero ----------
  const hero=document.querySelector('.hero');
  if(!hero) return;
  const mems=[...document.querySelectorAll('.memory')], title=document.getElementById('title'), bg=document.getElementById('herobg'), vid=document.getElementById('herovid');
  mems.forEach(m=>{ m.innerHTML=m.innerHTML.trim().split(/\s+/).map((w,i)=>`<span class="w" style="--i:${i};transition-delay:${i*80}ms">${w}</span>`).join(' '); });
  bg.classList.add('on');
  if(vid && !reduce){ vid.playbackRate=0.9; vid.play().catch(()=>{}); }
  requestAnimationFrame(()=>title.classList.add('on'));
  const slot=document.querySelector('.memories');
  if(reduce){ mems[0].classList.add('on'); }
  else{
    let i=0;
    const HOLD=3200, GAP=700;
    function fit(m){ if(slot && innerWidth>700) slot.style.width=m.getBoundingClientRect().width+'px'; }
    function show(){ const m=mems[i]; fit(m); m.classList.remove('off'); m.classList.add('on');
      setTimeout(()=>{ m.classList.remove('on'); m.classList.add('off'); setTimeout(()=>{ m.classList.remove('off'); i=(i+1)%mems.length; show(); }, GAP); }, i===0?HOLD+1600:HOLD); }
    setTimeout(show, 2800);
  }
})();
