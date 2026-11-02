(()=>{const t=document.getElementById('track');if(!t)return;
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
[...t.children].forEach(n=>t.appendChild(n.cloneNode(true)));
if(reduce){t.parentElement.style.overflowX='auto';return}
let x=0,last=scrollY,boost=0,prev=performance.now();const base=40;// px/s
function f(now){const dt=Math.min((now-prev)/1000,.05);prev=now;const d=scrollY-last;last=scrollY;
boost+= (Math.abs(d)*0.3-boost)*0.1; // скролл добавляет скорость с коэффициентом 0.3
x-= base*dt + boost; const half=t.scrollWidth/2; if(-x>=half)x+=half;
t.style.transform=`translate3d(${x}px,0,0)`;requestAnimationFrame(f)}
requestAnimationFrame(f)})();
(()=>{const s=document.getElementById('caps');if(!s)return;s.style.display='inline-block';
function fit(){s.style.fontSize='100px';const w=s.parentElement.clientWidth-8;s.style.fontSize=(100*w/s.offsetWidth)+'px'}
fit();addEventListener('resize',fit);document.fonts&&document.fonts.ready.then(fit)})();
(()=>{const b=document.querySelector('.burger'),m=document.getElementById('menu');if(!b||!m)return;
b.addEventListener('click',e=>{e.stopPropagation();const o=m.classList.toggle('open');b.setAttribute('aria-expanded',o);b.textContent=o?'Закрыть':'Меню'});
document.addEventListener('click',e=>{if(!m.contains(e.target)&&m.classList.contains('open')){m.classList.remove('open');b.setAttribute('aria-expanded',false);b.textContent='Меню'}});
if(matchMedia('(max-width:900px)').matches)document.querySelectorAll('.spec-d').forEach((d,i)=>{if(i>0)d.open=false})})();
