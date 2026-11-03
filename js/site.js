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

  // ---------- homepage hero ----------
  const hero=document.querySelector('.hero');
  if(!hero) return;
  const mems=[...document.querySelectorAll('.memory')], title=document.getElementById('title'), bg=document.getElementById('herobg'), vid=document.getElementById('herovid');
  mems.forEach(m=>{ m.innerHTML=m.innerHTML.trim().split(/\s+/).map((w,i)=>`<span class="w" style="--i:${i};transition-delay:${i*80}ms">${w}</span>`).join(' '); });
  bg.classList.add('on');
  if(vid && !reduce){ vid.playbackRate=0.9; vid.play().catch(()=>{}); }
  requestAnimationFrame(()=>title.classList.add('on'));
  if(reduce){ mems[0].classList.add('on'); }
  else{
    let i=0;
    const HOLD=3200, GAP=700;
    function show(){ const m=mems[i]; m.classList.remove('off'); m.classList.add('on');
      setTimeout(()=>{ m.classList.remove('on'); m.classList.add('off'); setTimeout(()=>{ m.classList.remove('off'); i=(i+1)%mems.length; show(); }, GAP); }, i===0?HOLD+1600:HOLD); }
    setTimeout(show, 2800);
  }
})();
