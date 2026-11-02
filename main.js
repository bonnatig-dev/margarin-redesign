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
/* v3: supporting motion — reveals, masked headings, image masks, subtle hero parallax. Lead motion stays the marquee. */
(()=>{if(matchMedia('(prefers-reduced-motion: reduce)').matches||!('IntersectionObserver'in window))return;
const root=document.documentElement;root.classList.add('js-anim');
const $$=(s)=>[...document.querySelectorAll(s)];
// заголовки по словам на маске
$$('h2, .crow .cname, .prow h3, .ch h3').forEach(h=>{if(h.closest('.grad'))return;const words=[];
 [...h.childNodes].forEach(n=>{if(n.nodeType!==3)return;const f=document.createDocumentFragment();
  n.textContent.split(/(\s+)/).forEach(w=>{if(!w)return;if(/^\s+$/.test(w)){f.append(w);return}
   const o=document.createElement('span');o.className='ln';const i=document.createElement('span');i.textContent=w;o.append(i);f.append(o);words.push(i)});n.replaceWith(f)});
 words.forEach((w,i)=>w.style.setProperty('--d',Math.min(i*.04,.3)+'s'));h.classList.add('obs')});
$$('.grad').forEach(g=>g.classList.add('gm','obs'));
// блоки
const RV='.hero-col p, .hero-col .btns, .hero-facts, .lead, .chips, .spec, .recipe-tx p, .recipe-tx .pill, .p-l p, .p-l .pill, .countries li, .plead, .crumbs, .crow .cdesc, .pmeta, .spec-d, .rlist li, .ch p, .steps li, .ingbox, .prodlink, .rform, .timeline li, .deps li, .facts li, .tags, .big, .req, .ct-main .btns, .fcard, .fcol, .kick';
$$(RV).forEach(e=>{if(e.closest('.track'))return;e.classList.add('rv','obs');const sib=[...e.parentElement.children].indexOf(e);e.style.setProperty('--d',(sib%4)*.06+'s')});
$$('.recipe-ph, .rbig, .rec-ph, .prod-ph, .zavod').forEach(e=>e.classList.add('im','obs'));
const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{rootMargin:'0px 0px -8% 0px'});
$$('.obs').forEach(e=>io.observe(e));
// первый экран: кадр раскрывается из скруглённой маски + лёгкий параллакс фото (0.12)
const hero=document.querySelector('.hero');
if(hero){const bg=hero.querySelector('.hero-bg');requestAnimationFrame(()=>requestAnimationFrame(()=>hero.classList.add('in')));
 let tk=false;const upd=()=>{tk=false;const y=scrollY;if(y<innerHeight*1.2)bg.style.setProperty('--py',(y*.12).toFixed(1)+'px')};
 addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(upd)}},{passive:true})}
// шапка внутренних страниц: стеклянная подложка после прокрутки
const bar=document.querySelector('.top.inner .bar');if(bar){const s=()=>bar.classList.toggle('scrolled',scrollY>80);addEventListener('scroll',s,{passive:true});s()}
})();
