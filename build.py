#!/usr/bin/env python3
"""Generates the Muse site pages from shared chrome + per-page bodies."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))
BOOK = "https://www.sevenrooms.com/reservations/musebytomaikens"
VOUCH = "https://musebytomaikens.vouchable.co.uk"
NAV = [("about.html","About"),("menus.html","Menus"),("whats-on.html","What's On"),("private-hire.html","Private Hire"),("suppliers.html","Suppliers"),("gallery.html","Gallery"),("press.html","Press"),("contact.html","Contact")]

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#FAF8F4">
<link rel="icon" href="img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css?v=12">
</head>
<body>
<a class="sr" href="#main">Skip to content</a>
'''

def header(current):
    links = "".join(f'<a href="{h}"{" class=on" if h==current else ""}>{t}</a>' for h,t in NAV if h in ("menus.html","whats-on.html","private-hire.html","contact.html"))
    dlinks = "".join(f'<a href="{h}">{t}</a>' for h,t in NAV)
    return f'''<header class="nav" id="nav">
  <a href="index.html" class="brand"><img src="img/logo.png" alt="Muse by Tom Aikens" class="logo"><img src="img/michelin.png" alt="One Michelin star" class="star-mark" title="One Michelin star"></a>
  <nav class="navlinks" aria-label="Main">{links}</nav>
  <div class="nav-right">
    <a class="book" href="{BOOK}" target="_blank" rel="noopener">Book a table</a>
    <button class="burger" id="open" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="drawer" id="drawer">
  <button class="close" id="close">Close</button>
  <div class="dr-links">
    <a href="index.html" data-img="img/kitchen-counter.jpg">Home</a>
    <a href="about.html" data-img="img/tom.jpg">About</a>
    <a href="menus.html" data-img="img/img1.jpg">Menus</a>
    <a href="whats-on.html" data-img="img/culinary-creators.jpg">What's On</a>
    <a href="private-hire.html" data-img="img/private-party-1.jpg">Private Hire</a>
    <a href="suppliers.html" data-img="img/our-suppliers.jpg">Suppliers</a>
    <a href="gallery.html" data-img="img/dining-area.jpg">Gallery</a>
    <a href="press.html" data-img="img/drinks-cab.jpg">Press</a>
    <a href="contact.html" data-img="img/muse-building.jpg">Contact</a>
    <a href="{VOUCH}" target="_blank" rel="noopener" data-img="img/img2.jpg">Gift vouchers</a>
    <a class="book" href="{BOOK}" target="_blank" rel="noopener">Book a table</a>
  </div>
  <div class="dr-side">
    <div class="dr-pic"><img src="img/kitchen-counter.jpg" alt="" id="drimg"></div>
    <div class="dr-meta">
      <div><h4>Find us</h4>38 Groom Place, Belgravia<br>London SW1X 7BA<br><a href="tel:+442033012903">+44 (0)20 3301 2903</a></div>
      <div><h4>Hours</h4>Lunch Wed – Sat, 12.30 – 1.30pm<br>Dinner Tue – Sat, 6.00 – 8.00pm<br>Closed Sunday and Monday</div>
      <div><h4>Follow</h4><a href="https://www.instagram.com/musebytomaikens" target="_blank" rel="noopener">Instagram</a><br><a href="https://www.facebook.com/Muse-by-Tom-Aikens-106260100800055" target="_blank" rel="noopener">Facebook</a></div>
    </div>
  </div>
  <div class="foot">38 Groom Place, Belgravia &nbsp;·&nbsp; +44 (0)20 3301 2903</div>
</div>
<main id="main">
'''

FOOTER = f'''</main>
<footer>
  <div class="foot-grid">
    <div>
      <img src="img/logo.png" alt="Muse by Tom Aikens" class="logo" style="height:40px;margin-bottom:18px">
      <address>38 Groom Place, Belgravia<br>London SW1X 7BA<br><a href="tel:+442033012903">+44 (0)20 3301 2903</a><br><a href="mailto:info@musebytomaikens.co.uk">info@musebytomaikens.co.uk</a></address>
    </div>
    <div>
      <h4>Visit</h4>
      <nav><a href="{BOOK}" target="_blank" rel="noopener">Book a table</a><a href="menus.html">Menus</a><a href="private-hire.html">Private hire</a><a href="{VOUCH}" target="_blank" rel="noopener">Gift vouchers</a><a href="contact.html">Find us</a></nav>
    </div>
    <div>
      <h4>Muse</h4>
      <nav><a href="about.html">About</a><a href="suppliers.html">Suppliers</a><a href="whats-on.html">What's on</a><a href="press.html">Press</a><a href="https://musebytomaikens.co.uk/careers" target="_blank" rel="noopener">Careers</a></nav>
    </div>
    <div>
      <h4>News and new dates</h4>
      <form class="news"><label class="sr" for="em">Email</label><input id="em" type="email" placeholder="Your email" required><button type="submit">Subscribe</button></form>
      <nav style="margin-top:22px"><a href="https://www.instagram.com/musebytomaikens" target="_blank" rel="noopener">Instagram</a><a href="https://www.facebook.com/Muse-by-Tom-Aikens-106260100800055" target="_blank" rel="noopener">Facebook</a></nav>
    </div>
  </div>
  <div class="foot-bot">
    <div>© Muse by Tom Aikens</div>
    <nav><a href="https://musebytomaikens.co.uk/privacy-policy" target="_blank" rel="noopener">Privacy</a></nav>
  </div>
</footer>
<script src="js/site.js?v=11"></script>
</body>
</html>
'''

def ph(src, alt, cls="", extra=""):
    return f'<div class="ph reveal {cls}" {extra}><img src="img/{src}" alt="{alt}" loading="lazy"></div>'

def page_head(chapter, title, lede, img="kitchen-counter.jpg", alt=""):
    return f'''<section class="page-hero">
  <div class="ph plx" data-plx="20"><img src="img/{img}" alt="{alt}"></div>
  <div class="inner">
    <div class="chapter">{chapter}</div>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>
'''


COURSES = [
 ("Forever Picking","Snacks of the season","The garden at home, and everything in it that could be eaten."),
 ("The Rule of Three","Three snacks","Three is always better than two."),
 ("From a Humble Beginning","Onion, Truffle, Egg Yolk","The onion, peeled ten thousand times for other dishes, finally takes the lead."),
 ("Making &amp; Breaking","Sourdough, cultured butter","Bread: comfort, sharing, and every memory kneaded into it."),
 ("Pause for a Minute","Crab, Celeriac, Pear","Hours of picking crab for a dish eaten in minutes. Pause first."),
 ("French Jealousy!","Scallop, Artichoke, Apple","Live British shellfish, landing in a Paris kitchen."),
 ("The Love Affair Continues","Turbot, Duck Confit, Mash","France, and the chefs who turned it into a love affair."),
 ("Made in Great Britain","Grouse, Turnip, Elderberries","Wild grouse from the North Pennines moors. Never reared."),
 ("It's All in the Leaves","Figs &amp; Leaves, Pinenut, Puff Pastry","Fig leaves, foraged. Mind the sap."),
 ("Life Has Never Been So Sweet","Plum, Cardamom, Grains","Sweet meets salt, through fermentation and patience."),
]
COURSE_IMGS = {2:"img/img1.jpg",4:"img/img3.jpg",6:"img/img4.jpg",8:"img/img2.jpg"}
def courses_html(limit=None):
    out=[]
    for i,(t,d,m) in enumerate(COURSES[:limit] if limit else COURSES):
        img = f' data-img="{COURSE_IMGS[i]}"' if i in COURSE_IMGS else ""
        out.append(f'<li class="course menu-row-hover"{img}><span class="n">{i+1:02d}</span><div><div class="ct">{t}</div><div class="cd">{d}</div><div class="cm">{m}</div></div></li>')
    return '<ol class="courses">'+"".join(out)+'</ol>'

MENU_ROWS = f'''<div class="float" id="float" aria-hidden="true"><img alt=""></div>
<div class="menu-list">
  <div class="menu-row" data-img="img/img1.jpg"><h3>Ten-course tasting</h3><div class="when">Lunch and dinner, Tuesday to Saturday</div><div class="price">£195<small>per person</small></div></div>
  <div class="menu-row" data-img="img/img4.jpg"><h3>Six-course tasting</h3><div class="when">Lunch, Thursday to Saturday</div><div class="price">£105<small>per person</small></div></div>
  <div class="menu-row" data-img="img/img2.jpg"><h3>À la carte</h3><div class="when">Lunch and dinner, Tuesday to Friday</div><div class="price">£160 / £195<small>two or three courses</small></div></div>
</div>'''

PAGES = {}

# ---------------- HOME ----------------
PAGES["index.html"] = ("Muse by Tom Aikens — Michelin-starred restaurant, Belgravia",
 "Muse is Tom Aikens' 25-cover Michelin-starred restaurant in a converted mews house in Belgravia. Seasonal tasting menus drawn from the memories that made him a chef.",
 f'''<div class="hero-pin"><section class="hero" aria-label="Introduction">
  <div class="grain"></div>
  <img class="lady" id="lady" src="img/muse-lady.png" alt="" aria-hidden="true">
  <div class="bg" id="herobg"><video id="herovid" muted loop playsinline preload="auto" poster="img/hero-poster.jpg" aria-hidden="true"><source src="img/hero.mp4" type="video/mp4"></video></div>
  <div class="hero-title" id="title">
    <h1 class="raw"><img src="img/logo.png" alt="Muse" class="script"></h1>
    <div class="by"><span class="by-pre">by</span> <span class="by-name">Tom Aikens</span><span class="by-place">Belgravia, London</span></div>
    <p class="thesis">Every dish here began as a memory.</p>
    <div class="memories" aria-live="polite">
      <p class="memory">Baking with my mother, Tania. Norfolk, aged eight.</p>
      <p class="memory">Picking fruit with my brother Robert for the jam pan.</p>
      <p class="memory">A bottle my father opened, and a France I hadn't seen yet.</p>
      <p class="memory">Live British shellfish, landing in a Paris kitchen.</p>
      <p class="memory">Two stars at twenty-six. The quietest I have ever been.</p>
      <p class="memory">Wild grouse from the North Pennines moors.</p>
    </div>
  </div>
</section></div>

<section class="statement">
  <p>A converted mews house in Belgravia, twenty-five seats, and a menu written from the memories that made Tom Aikens a chef.</p>
  <div class="rule"></div>
</section>

<section id="chef" style="padding-top:0">
  <div class="overlap flip">
    <div class="text">
      <div class="chapter">Tom Aikens</div>
      <h2>Back at the pass, every service.</h2>
      <p style="margin-top:20px">Trained under Pierre Koffmann and Joël Robuchon, Tom earned his second star at twenty-six. At Muse he is back at the pass every service, cooking a menu drawn from his own life — and telling you why.</p>
      <div class="cta"><a class="btn" href="about.html">Tom's story</a></div>
    </div>
    {ph("img2.jpg","Tom Aikens plating at the pass","big plx",'data-plx="14"')}
  </div>
</section>

<section id="house" class="tint">
  <div class="overlap">
    {ph("muse-building.jpg","The Muse mews house on Groom Place","big plx",'data-plx="14"')}
    <div class="text">
      <div class="chapter">The house</div>
      <h2>A Georgian mews, with room for twenty-five.</h2>
      <p style="margin-top:20px">Muse opened in January 2020 and earned its Michelin star within the year. Two floors, an open kitchen, and a dining room that feels closer to a dinner party than a restaurant.</p>
      <div class="facts"><div>25<small>covers</small></div><div>2020<small>opened</small></div><div>1<small>Michelin star</small></div></div>
      <div class="cta"><a class="btn" href="about.html">About Muse</a></div>
    </div>
  </div>
</section>

<section class="dark" id="menus">
  <div class="grid g-2" style="align-items:end;margin-bottom:56px">
    <div><div class="chapter">The menus</div><h2>Each course is a memory, cooked.</h2></div>
    <p class="lede">Tom's menus trace the moments and people that made him a chef. They change with the seasons; this is autumn.</p>
  </div>
  <div class="menu-cards">
    <a class="mcard" href="menus.html#tasting">
      <div class="ph"><img src="img/img1.jpg" alt="A course from the tasting menu" loading="lazy"></div>
      <div class="mc-body">
        <div class="mc-k">Ten courses</div>
        <h3>The Tasting Menu</h3>
        <p>The full story, from the garden in Norfolk to the moors of Yorkshire. Lunch and dinner, Tuesday to Saturday.</p>
        <div class="mc-foot"><span class="mc-price">£195</span><span class="mc-link">View menu</span></div>
      </div>
    </a>
    <a class="mcard" href="menus.html#lunch">
      <div class="ph"><img src="img/img3.jpg" alt="A course at lunch" loading="lazy"></div>
      <div class="mc-body">
        <div class="mc-k">Six courses</div>
        <h3>Lunch Tasting</h3>
        <p>The shorter telling, for a long lunch. Thursday to Saturday.</p>
        <div class="mc-foot"><span class="mc-price">£105</span><span class="mc-link">View menu</span></div>
      </div>
    </a>
    <a class="mcard" href="menus.html#alacarte">
      <div class="ph"><img src="img/img4.jpg" alt="Sauce poured at the table" loading="lazy"></div>
      <div class="mc-body">
        <div class="mc-k">Two or three courses</div>
        <h3>À la Carte</h3>
        <p>Choose your own way through the season. Lunch and dinner, Tuesday to Friday.</p>
        <div class="mc-foot"><span class="mc-price">£160 / £195</span><span class="mc-link">View menu</span></div>
      </div>
    </a>
  </div>
  <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a table</a></div>
</section>

<section class="bleed-row">
  {ph("img4.jpg","Sauce poured at the table","plx",'data-plx="12"')}{ph("img1.jpg","A course from the tasting menu","plx",'data-plx="18"')}{ph("img3.jpg","A course","plx",'data-plx="12"')}
</section>

<section id="tom">
  <div class="overlap flip">
    <div class="text">
      <div class="chapter">Tom Aikens</div>
      <h2>Raised in Norfolk. Trained in the hardest kitchens in Europe.</h2>
      <p style="margin-top:20px">David Cavalier's, La Tante Claire, Pied-à-Terre, Robuchon in Paris. Muse is his return to cooking for a room small enough to know every guest.</p>
      <blockquote class="quote-card" style="margin:34px 0"><p class="pull" style="margin:0">“My mother taught me to bake when I was eight. My father taught me that a bottle of wine could be a map of somewhere. Everything else followed.”</p></blockquote>
      <a class="tl" href="about.html">Tom's story and the team</a>
    </div>
    {ph("tom.jpg","Tom Aikens at Muse","big plx",'data-plx="16"')}
  </div>
</section>

<section class="tint" id="provenance">
  <div class="grid g-2">
    <div><div class="chapter">Provenance</div><h2>We cook with people who care as much as we do.</h2></div>
    <div><p class="lede">Almost everything at Muse comes from British farmers, fishermen, millers and makers we know by name. Many have supplied the kitchen since the day it opened.</p><div class="cta"><a class="btn" href="suppliers.html">Meet the suppliers</a></div></div>
  </div>
  <div class="ticker" style="margin-top:70px"><span>HG Walter <i>✦</i> Lake District Farmers <i>✦</i> Flying Fish <i>✦</i> Kernow Sashimi <i>✦</i> Keltic Seafare <i>✦</i> Hodmedod's <i>✦</i> Shipton Mill <i>✦</i> Shrub <i>✦</i> Nurtured in Norfolk <i>✦</i> Old Hall Farm <i>✦</i> Barsham Brewery <i>✦</i> Pump Street Chocolate <i>✦</i> Rare Tea Company <i>✦</i> Blenheim Forge <i>✦</i> HG Walter <i>✦</i> Lake District Farmers <i>✦</i> Flying Fish <i>✦</i> Kernow Sashimi <i>✦</i> Keltic Seafare <i>✦</i> Hodmedod's <i>✦</i> Shipton Mill <i>✦</i> Shrub <i>✦</i> Nurtured in Norfolk <i>✦</i> Old Hall Farm <i>✦</i> Barsham Brewery <i>✦</i> Pump Street Chocolate <i>✦</i> Rare Tea Company <i>✦</i> Blenheim Forge <i>✦</i> </span></div>
  <div class="bleed-row" style="margin-top:0;gap:14px">{ph("gallery-1.jpg","Hand-thrown bowls")}{ph("our-suppliers.jpg","A hen at one of our farms")}{ph("gallery-3.jpg","The counter stools")}</div>
</section>

<section class="split" id="on">
  <div class="ph"><img src="img/kitchen-counter.jpg" alt="The counter at Muse" loading="lazy"></div>
  <div class="panel">
    <div class="chapter">What's on</div>
    <h2>One night. Two chefs. Eight courses at the counter.</h2>
    <p style="margin-top:20px">The Culinary Creators series brings a guest chef to the counter for a single evening alongside Tom. Every Tuesday, the Wine Cellar Series opens the cellar.</p>
    <div class="cta"><a class="btn" href="whats-on.html">See the dates</a><a class="btn" href="private-hire.html">Private hire</a></div>
  </div>
</section>

<section class="dark" id="press">
  <div class="grid g-2" style="grid-template-columns:1fr 1fr">
    <blockquote class="quote">“Opening of the year.”<cite>Grace Dent, The Guardian</cite></blockquote>
    <blockquote class="quote">One Michelin star, awarded in the restaurant's first year.<cite>Michelin Guide Great Britain &amp; Ireland</cite></blockquote>
  </div>
  <div class="awards"><div>Michelin star<small>Since 2021</small></div><div>Five AA Rosettes<small>AA Hospitality Awards</small></div><div>Harden's Top 100<small>UK Restaurants</small></div><div>Restaurant &amp; Bar Design Awards<small>Winner, 2021</small></div></div>
</section>

<section id="visit">
  <div class="grid g-2">
    {ph("dining-area.jpg","The dining room at Muse","wide plx",'data-plx="14"')}
    <div>
      <div class="chapter">Visit</div>
      <h2>Find us at the end of the mews.</h2>
      <div class="grid" style="grid-template-columns:1fr 1fr;gap:30px;margin-top:30px">
        <dl class="spec" style="grid-template-columns:1fr"><dt>Lunch</dt><dd>Wed – Sat, 12.30 – 1.30pm</dd><dt style="margin-top:8px">Dinner</dt><dd>Tue – Sat, 6.00 – 8.00pm</dd><dt style="margin-top:8px">Closed</dt><dd>Sunday and Monday</dd></dl>
        <address style="font-style:normal;line-height:1.7">38 Groom Place<br>Belgravia<br>London SW1X 7BA<br><a href="tel:+442033012903">+44 (0)20 3301 2903</a></address>
      </div>
      <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a table</a><a class="btn" href="contact.html">Contact</a></div>
    </div>
  </div>
</section>
''')

# ---------------- ABOUT ----------------
PAGES["about.html"] = ("About — Muse by Tom Aikens",
 "The story of Muse: a 25-cover converted mews house in Belgravia, Tom Aikens' return to experience-led fine dining, and the team who run it.",
 page_head("About","A restaurant built from memory.",img="dining-area.jpg",alt="The dining room at Muse",lede="Muse is Tom Aikens' return to experience-led fine dining: an intimate, 25-cover converted mews house where every menu traces the moments and people that shaped his life and his cooking.") + f'''
<section>
  <div class="grid g-2">
    {ph("drinks-cab.jpg","The drinks cabinet at Muse","tall plx",'data-plx="16"')}
    <div>
      <div class="chapter">The house</div>
      <h2>A Georgian mews on Groom Place.</h2>
      <p class="lede" style="margin:20px 0 24px">Muse opened in January 2020 and was awarded its Michelin star within the year. Grace Dent named it her opening of the year.</p>
      <p>Two floors of a converted mews house, with an open kitchen and counter on the ground floor, a lounge, and a private dining room upstairs. Interiors are by Rebecca Korner of Körner Interiors, blending the classic and the avant-garde; the room won at the Restaurant &amp; Bar Design Awards in 2021.</p>
      <div class="facts"><div>25<small>covers</small></div><div>2<small>floors</small></div><div>5<small>AA Rosettes</small></div></div>
    </div>
  </div>
</section>

<section class="tint">
  <div class="grid g-21">
    <div>
      <div class="chapter">Tom Aikens</div>
      <h2>Raised in Norfolk. Trained in the hardest kitchens in Europe.</h2>
      <p class="lede" style="margin:24px 0 30px">Tom Aikens is one of the most acclaimed British chefs of his generation. At twenty-six he became the youngest British chef to hold two Michelin stars.</p>
      <p>His training ran through David Cavalier's in Battersea, Pierre Koffmann's La Tante Claire, Pied-à-Terre, and Joël Robuchon in Paris — kitchens that taught precision, and the discipline to let an ingredient speak. Raised in Norfolk, he has always cooked with fresh, local and sustainable produce at the centre.</p>
      <p style="margin-top:1.2em">Muse is his return to experience-led fine dining: a room small enough that he can cook for every guest, and a menu personal enough that he can tell them why.</p>
      <blockquote class="pull">“My mother taught me to bake when I was eight. My father taught me that a bottle of wine could be a map of somewhere. Everything else followed.”<cite>Tom Aikens</cite></blockquote>
    </div>
    <div>{ph("tom.jpg","Tom Aikens","tall plx",'data-plx="18"')}<div class="grid" style="grid-template-columns:1fr 1fr;gap:16px;margin-top:16px">{ph("mom-dad.jpg","Tom and Robert with their mother, Tania","square")}{ph("img4.jpg","Tom plating at the pass","square")}</div></div>
  </div>
</section>

<section>
  <div class="grid g-2">
    <div><div class="chapter">Tania and his father</div><h2>Where the menu begins.</h2></div>
    <div>
      <p class="lede">Tom's mother, Tania, introduced him to the pleasures of food and taught him to bake from the age of eight. He and his twin brother Robert spent long afternoons picking fruit with her for jams and chutneys.</p>
      <p style="margin-top:1.2em">His father, who advised him in his early years in the kitchen, had built a life in the wine trade — and through it gave Tom an insight into the food heritage of France that first made him want to be a chef. Those two threads, the Norfolk kitchen and the French table, still run through every menu at Muse.</p>
    </div>
  </div>
</section>

<section class="tint">
  <div class="chapter">The team</div>
  <h2>The people in the room.</h2>
  <div class="team">
    <div><h3>Andrei Avrinte</h3><div class="role">Head Chef</div><p>Trained in the French tradition and in one- and two-Michelin-starred kitchens — contemporary cooking with Guillaume Sanchez, classical fine dining at La Chèvre d'Or, and a beginning under Thierry Breton in Paris.</p></div>
    <div><h3>Sébastien Pé</h3><div class="role">General Manager</div><p>Trained in Belgium, then Paris from 2004 — the Four Seasons George V, Pavillon Ledoyen and Le Bristol — before eight years at The Five Fields in Chelsea. Your host from the first enquiry to the last glass.</p></div>
    <div><h3>Elisa Marchini</h3><div class="role">Restaurant Manager &amp; Head Sommelier</div><p>Grew up on her family's vineyard on the Tuscan coast. A protégée of Pierre Koffmann, with time at L'Atelier Robuchon. She writes the pairings and keeps the cellar.</p></div>
  </div>
</section>
''')

# ---------------- MENUS ----------------
SIX = [0,3,2,6,7,9]
ALC = [("From a Humble Beginning",["Onion, Truffle, Egg Yolk","Crab, Celeriac, Pear"]),("The Love Affair Continues",["Turbot, Duck Confit, Mash","Grouse, Turnip, Elderberries"]),("It's All in the Leaves",["Figs &amp; Leaves, Pinenut, Puff Pastry","Plum, Cardamom, Grains"])]
def alc_html():
    out=[]
    for i,(t,ds) in enumerate(ALC):
        out.append(f'<li class="course"><span class="n">{i+1:02d}</span><div><div class="ct">{t}</div><div class="cd">{ds[0]}</div><div class="or">or</div><div class="cd">{ds[1]}</div></div></li>')
    return '<ol class="courses">'+"".join(out)+'</ol>'
def six_html():
    out=[]
    for n,i in enumerate(SIX):
        t,d,m=COURSES[i]
        out.append(f'<li class="course"><span class="n">{n+1:02d}</span><div><div class="ct">{t}</div><div class="cd">{d}</div><div class="cm">{m}</div></div></li>')
    return '<ol class="courses">'+"".join(out)+'</ol>'
NOTE='<p class="small mute" style="margin-top:16px">Cooked fresh to order in a kitchen where nuts and shellfish are present — please tell us about any allergies when you book. A discretionary 15% service charge is added to the bill.</p>'
PAGES["menus.html"] = ("Menus — Muse by Tom Aikens",
 "Autumn menus at Muse: the ten-course tasting menu £195, six-course lunch tasting £105, à la carte two or three courses. Wine pairings by our sommelier.",
 page_head("Menus","Each course is a memory, cooked.",img="img1.jpg",alt="A dish from the tasting menu",lede="Tom's menus trace the moments and people that made him a chef — a childhood kitchen in Norfolk, the great Paris and London kitchens, the produce of a small island. Every course carries the title of the memory it comes from.") + f"""
<nav class="subnav" aria-label="Menus"><a href="#tasting">Ten-course tasting</a><a href="#lunch">Six-course lunch</a><a href="#alacarte">À la carte</a><a href="#wine">Wine</a><a href="#creators">Culinary Creators</a></nav>

<section class="dark" id="tasting">
  <div class="grid g-2" style="align-items:start">
    <div class="sticky">
      <div class="chapter">Autumn · ten courses</div>
      <h2>The Tasting Menu</h2>
      <div class="facts"><div>£195<small>per person</small></div><div>Tue – Sat<small>lunch and dinner</small></div></div>
      <p style="margin-top:28px">The full story in ten courses. The titles are Tom's; the dishes move as the season does.</p>
      {NOTE}
      <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a table</a><a class="btn" href="#">Download (PDF)</a></div>
    </div>
    {courses_html()}
  </div>
</section>

<section id="lunch">
  <div class="grid g-2" style="align-items:start">
    <div class="sticky">
      <div class="chapter">Autumn · six courses</div>
      <h2>Lunch Tasting</h2>
      <div class="facts"><div>£105<small>per person</small></div><div>Thu – Sat<small>lunch only</small></div></div>
      <p style="margin-top:28px">The shorter telling: six chapters from the ten, for a long lunch in the mews.</p>
      {NOTE}
      <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book lunch</a><a class="btn" href="#">Download (PDF)</a></div>
    </div>
    {six_html()}
  </div>
</section>

<section class="tint" id="alacarte">
  <div class="grid g-2" style="align-items:start">
    <div class="sticky">
      <div class="chapter">Autumn · à la carte</div>
      <h2>À la Carte</h2>
      <div class="facts"><div>£160<small>two courses</small></div><div>£195<small>three courses</small></div><div>Tue – Fri<small>lunch and dinner</small></div></div>
      <p style="margin-top:28px">Choose your own way through the season — one dish from each chapter. Snacks and bread come to every table.</p>
      {NOTE}
      <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a table</a><a class="btn" href="#">Download (PDF)</a></div>
    </div>
    {alc_html()}
  </div>
</section>

<section id="wine">
  <div class="grid g-2">
    {ph("grapes.jpg","Grapes on the vine","wide")}
    <div>
      <div class="chapter">Wine</div>
      <h2>Pairings built for the table.</h2>
      <p class="lede" style="margin:20px 0 20px">Elisa, our head sommelier, designs pairings to suit all tastes — classic vintages through to organic and biodynamic growers.</p>
      <p>Choose a flight to follow the tasting menu, or go glass by glass. The cellar also opens for the Wine Cellar Series every Tuesday.</p>
      <div class="cta"><a class="btn" href="#">Wine list (PDF)</a><a class="btn" href="whats-on.html">Wine Cellar Series</a></div>
    </div>
  </div>
</section>

<section class="photo-text" id="creators">
  {ph("kitchen-counter.jpg","The counter at Muse")}
  <div class="inner">
    <div><div class="chapter">Culinary Creators</div><h2>One-night collaborative tasting menus.</h2></div>
    <div><p>Eight courses, cooked live at the counter by Tom and a guest chef. Each menu is written for that evening alone and released closer to the date.</p><div class="cta"><a class="btn" href="whats-on.html">See the next dates</a></div></div>
  </div>
</section>
""")

# ---------------- WHAT'S ON ----------------
PAGES["whats-on.html"] = ("What's On — Muse by Tom Aikens",
 "Culinary Creators collaborative dinners, the Wine Cellar Series every Tuesday, and Women in Wine at Muse by Tom Aikens.",
 page_head("What's on","Nights that only happen once.",img="kitchen-counter.jpg",alt="The counter at Muse",lede="The Culinary Creators series brings some of Britain's most acclaimed chefs to the counter for a single evening alongside Tom. Then there is the cellar, which opens every Tuesday.") + f'''
<section>
  {ph("culinary-creators.jpg","The counter at Muse","pano plx",'data-plx="20"')}
  <div class="events">
    <div class="event"><h3>Wine Cellar Series</h3><div class="when">Every Tuesday</div><p>An evening built around the cellar: Elisa opens bottles that rarely reach the list, with dishes from the kitchen to match. Small numbers, around the counter.</p><a class="tl" href="{BOOK}" target="_blank" rel="noopener">Book a Tuesday</a></div>
    <div class="event"><h3>Culinary Creators × Jackson Boxer</h3><div class="when">13 January</div><p>Eight courses, two chefs, one night. Jackson Boxer joins Tom at the counter. The menu is released closer to the date.</p><a class="tl" href="{BOOK}" target="_blank" rel="noopener">Reserve a seat</a></div>
    <div class="event"><h3>Women in Wine</h3><div class="when">14 October</div><p>A dinner celebrating the women shaping wine today — growers, makers and sommeliers — with a menu written to their bottles.</p><a class="tl" href="{BOOK}" target="_blank" rel="noopener">Reserve a seat</a></div>
  </div>
</section>

<section class="tint">
  <div class="chapter">Past collaborations</div>
  <h2>Who has cooked at the counter.</h2>
  <div class="index" style="margin-top:40px">
    <div><b>Merlin Labron-Johnson</b><i>Culinary Creators, 23 September</i></div>
    <div><b>Ruth Hansom</b><i>Culinary Creators, 2 June</i></div>
    <div><b>Daniel Clifford</b><i>Culinary Creators, 19 May</i></div>
    <div><b>Endo Kazutoshi</b><i>Four-hands dinner, July 2024</i></div>
  </div>
  <p class="mute" style="margin-top:40px">To hear about new dates first, join the newsletter at the foot of the page.</p>
</section>
''')

# ---------------- PRIVATE HIRE ----------------
PAGES["private-hire.html"] = ("Private Hire — Muse by Tom Aikens",
 "Private and group dining at Muse for 6 to 25 guests: the counter, the upstairs private dining room, or exclusive hire of the whole townhouse.",
 page_head("Private hire","The house, for your table only.",img="private-party-1.jpg",alt="The dining room set for a private party",lede="From a counter for six to the whole townhouse for twenty-five, Muse hosts dinners that feel like a party at home — with a Michelin-starred kitchen downstairs.") + f'''
<section>
  <div class="grid g-2">
    {ph("private-party-1.jpg","The dining room set for a private party","tall plx",'data-plx="16"')}
    <div>
      <div class="chapter">Three ways to take the house</div>
      <h3>The counter</h3><p style="margin:8px 0 28px">Semi-private, on the ground floor. Front-row seats at the open kitchen, with the lounge to retire to.</p>
      <h3>The private dining room</h3><p style="margin:8px 0 28px">Upstairs, with its own character and a door that closes. For larger groups and anything you'd rather keep between you.</p>
      <h3>Exclusive townhouse hire</h3><p style="margin:8px 0 28px">The whole of Muse, for complete privacy and a fully bespoke evening.</p>
      <div class="facts"><div>6 – 25<small>guests</small></div></div>
    </div>
  </div>
</section>

<section class="tint">
  <div class="grid g-2">
    <div><div class="chapter">Menus for groups</div><h2>Written around your table.</h2></div>
    <div>
      <p class="lede">Groups of up to six can take the full ten-course tasting menu. From seven guests, choose the six-course tasting menu or a seasonal three-course à la carte, which the host curates with us in advance.</p>
      <p style="margin-top:1.2em">Sébastien, our General Manager, is your contact from the first enquiry — menu, pacing, wine and the feel of the room.</p>
      <div class="cta"><a class="btn solid" href="mailto:info@musebytomaikens.co.uk?subject=Private%20dining%20enquiry">Enquire by email</a><a class="btn" href="#">Download the brochure</a></div>
      <p class="small mute" style="margin-top:18px">info@musebytomaikens.co.uk &nbsp;·&nbsp; +44 (0)20 3301 2903</p>
    </div>
  </div>
</section>

<section>
  <div class="grid g-2">
    <div><div class="chapter">Beyond the mews</div><h2>Tom, at your event.</h2></div>
    <div><p class="lede">For dinners and events away from Muse, Tom's team caters privately. Enquiries go to Grace: <a class="tl" href="mailto:grace@tomaikens.co.uk">grace@tomaikens.co.uk</a> or 07921 335 922.</p></div>
  </div>
</section>
''')

# ---------------- SUPPLIERS ----------------
SUP = [
 ("HG Walter","Meat","A family-run London butcher since 1972, sourcing British meat from small free-range farms raising native breeds."),
 ("Lake District Farmers","Meat","Works with more than fifty Cumbrian farms for breed-specific meat, keeping traditional fell farming alive."),
 ("Flying Fish","Fish and shellfish","Wild, seasonal seafood from UK waters, bought from responsible day boats and with us within 48 hours."),
 ("Kernow Sashimi","Sustainable fish","A Cornish family business supplying small-day-boat fish, landed and delivered within twelve hours."),
 ("Keltic Seafare","Live shellfish","Hand-dived scallops, creel-caught langoustine and native lobster from Scotland, overnight to London."),
 ("Hodmedod's","Pulses and grains","Organic British pulses and heritage grains from East Anglia; they go into our sourdough."),
 ("Shipton Mill","Flour","A Cotswold mill of speciality flours from traditional and international grains — the flour in our bread."),
 ("Shrub","Seasonal produce","Fruit, edible flowers, herbs and leaves from more than forty-five organic and biodynamic farms."),
 ("Nurtured in Norfolk","Micro greens and flowers","Micro cress, pea shoots, edible flowers and sea vegetables grown in glasshouses — over 280 varieties."),
 ("Smith &amp; Brock","Fresh produce","Growers across the UK, Italy and Spain, and the markets of Rungis."),
 ("Old Hall Farm","Dairy","A Suffolk Jersey herd. We make our cultured butter from their cream, every day."),
 ("Barsham Brewery","Beer","A North Norfolk estate brewery using its own barley and water. Their Robin Stout goes into the sourdough."),
 ("Pump Street Chocolate","Chocolate","Suffolk bean-to-bar makers working directly with single-origin cacao farms."),
 ("Château de Panisse","Olive oil","Provençal estate oils — Fruité Vert and Noir d'Olives Maturées — from four local olive varieties."),
 ("Rare Tea Company","Tea","Teas bought directly from independent farms, with flavour, sustainability and fair pay to growers first."),
 ("Difference Coffee","Coffee","Specialty-grade Arabica from award-winning estates: Panama Geisha, Hawaii Kona, Jamaica Blue Mountain, Brazil Yellow Bourbon."),
 ("Bloodroot Blades","Knives","Everyday kitchen knives from recycled and local materials — handles from a fallen tree, steel from car springs."),
 ("Blenheim Forge","Knives","A Peckham bladesmith workshop that hand-forges our restaurant knives."),
 ("Körner Interiors","The room","Rebecca Korner designed Muse's interiors across both floors, blending the classic and the avant-garde."),
]
sup_html = "".join(f'<div style="display:block"><b>{n}</b><i style="display:block;text-align:left;color:var(--copper);font-size:13px;margin:4px 0 8px">{w}</i><p style="font-size:15px;color:var(--ink-2)">{d}</p></div>' for n,w,d in SUP)
PAGES["suppliers.html"] = ("Suppliers — Muse by Tom Aikens",
 "The farmers, fishermen, millers and makers who supply Muse by Tom Aikens — from HG Walter and Lake District Farmers to Blenheim Forge.",
 page_head("Provenance","We cook with people who care as much as we do.",img="provenance.jpg",alt="Wild trout",lede="Almost everything at Muse comes from British farmers, fishermen, millers and makers we know by name. Many have supplied the kitchen since the day it opened. The knives, the bowls and the room itself were made for us too.") + f'''
<section>
  <div class="strip">{ph("provenance.jpg","Wild trout, held by hand")}{ph("our-suppliers.jpg","A hen at one of our farms")}{ph("gallery-3.jpg","Hand-thrown bowls")}</div>
</section>
<section class="sage" style="padding-top:clamp(60px,7vw,100px)">
  <div class="index">{sup_html}</div>
</section>
''')

# ---------------- GALLERY ----------------
GAL = [("kitchen-counter.jpg","The counter"),("img1.jpg","Plating at the pass"),("muse-building.jpg","Groom Place"),("img2.jpg","Sauce at the table"),("gallery-1.jpg","Bowls"),("dining-area.jpg","The dining room"),("drinks-cab.jpg","The drinks cabinet"),("img3.jpg","A course"),("private-party-1.jpg","Set for a private dinner"),("gallery-3.jpg","Stacked bowls"),("img4.jpg","Tom plating"),("culinary-creators.jpg","Sourdough and preserves"),("tom.jpg","Tom Aikens")]
PAGES["gallery.html"] = ("Gallery — Muse by Tom Aikens","Photographs of Muse by Tom Aikens: the mews house, the counter, the dining room and the food.",
 page_head("Gallery","The house, the counter, the plates.",img="img2.jpg",alt="Sauce at the table",lede="A look inside the mews.") + '<section><div class="masonry">' + "".join(f'<div class="ph reveal{" wide" if s in ("kitchen-counter.jpg","dining-area.jpg","culinary-creators.jpg","private-party-1.jpg") else ""}"><img src="img/{s}" alt="{a}" loading="lazy"></div>' for s,a in GAL) + '</div></section>')

# ---------------- PRESS ----------------
PRESS = [
 ("14 May 2026","SUPPER","Tom Aikens","https://issuu.com/mondiale/docs/supper_-_issue_48/39"),
 ("11 May 2026","Square Meal","Best chef's tables in London","https://www.squaremeal.co.uk/restaurants/best-for/best-chefs-tables-london_10522"),
 ("17 Apr 2026","Square Meal","25 of the best luxury and Michelin-star private dining rooms in London","https://www.squaremeal.co.uk/private-group-dining/best-for/luxury-michelin-star-private-dining-rooms-london_10410"),
 ("9 Feb 2026","Citizen Femme","Top tables: 17 London restaurants to book in February","https://citizen-femme.com/2026/02/03/top-tables-london-restaurants-to-book-in-february-2026/"),
 ("26 Jan 2026","Luxury Lifestyle Magazine","Meet the chef: Tom Aikens","https://www.luxurylifestylemag.co.uk/food-and-drink/meet-the-chef-tom-aikens-owner-of-muse-by-tom-aikens-belgravia-in-london/"),
 ("13 Jan 2026","Sphere","5 minutes with Tom Aikens","https://www.spherelife.com/interviews/5-minutes-tom-aikens"),
 ("","The Rakish Gent","At the pass: Tom Aikens on Muse, memory and the future of fine dining","https://www.therakishgent.co.uk/pages/at-the-pass-tom-aikens-on-muse-memory-and-the-future-of-fine-dining"),
 ("","MSN","Muse to host new series with many of Britain's most acclaimed chefs","https://www.msn.com/en-gb/foodanddrink/other/muse-to-host-new-series-with-many-of-britain-s-most-acclaimed-chefs/ar-AA1WhnhA"),
 ("3 Dec 2025","Wallpaper*","The best Christmas hampers","https://www.wallpaper.com/entertaining/food-drink/best-christmas-hampers"),
 ("30 Jul 2024","Metro","Review: childhood memories on a plate","https://metro.co.uk/2024/07/30/muse-review-childhood-memories-a-plate-21177875/"),
 ("26 Sep 2023","Evening Standard","Muse awarded five AA Rosettes","https://www.standard.co.uk/reveller/restaurants/angela-hartnett-2023-aa-hospitality-awards-ben-mccormack-b1109547.html"),
 ("20 Jun 2023","The Nudge","Review","https://thenudge.com/london-restaurants/muse-by-tom-aikens/"),
 ("5 May 2023","Michelin Guide","Restaurants near the royal residences","https://guide.michelin.com/gb/en/article/features/michelin-guide-restaurants-near-the-royal-residences"),
 ("2 May 2023","Elite Traveler","Interview with Tom Aikens","https://elitetraveler.com/finest-dining/the-experts/michelin-star-chef-tom-aikens-interview"),
 ("8 Feb 2023","ELLE","Romantic restaurants in London","https://www.elle.com/uk/life-and-culture/culture/g30890495/romantic-restaurants-london/"),
 ("13 Jan 2023","Harden's","Top 100 UK restaurants","https://www.hardens.com/top-100-uk-restaurants/"),
 ("22 Sep 2021","The Independent","Review","https://www.independent.co.uk/life-style/food-and-drink/muse-restaurant-review-2021-tom-aikens-london-b1921442.html"),
 ("15 Oct 2021","Big Hospitality","Restaurant &amp; Bar Design Awards winner","https://www.bighospitality.co.uk/Article/2021/10/15/Muse-and-Maison-Francois-among-winners-at-Restaurant-Bar-Design-Awards"),
 ("10 Jan 2021","Michelin Guide","Muse","https://guide.michelin.com/gb/en/greater-london/london/restaurant/muse-1188132"),
 ("14 Feb 2020","The Guardian","Review by Grace Dent","https://www.theguardian.com/food/2020/feb/14/muse-sw1-the-sort-of-pretentious-i-live-for-restaurant-review"),
 ("","The Telegraph","Review","https://www.telegraph.co.uk/food-and-drink/restaurants/muse-tom-aikens-london-restaurant-review/"),
 ("22 Jan 2020","Evening Standard","Review by David Sexton","https://www.standard.co.uk/go/london/restaurants/david-sexton-muse-restaurant-review-tom-aikens-a4340966.html"),
 ("13 Jan 2020","Tatler","New restaurant openings, London 2020","https://www.tatler.com/article/new-restaurant-openings-london-2020"),
]
press_html = "".join(f'<a href="{u}" target="_blank" rel="noopener"><span class="pub">{p}</span><span class="hl">{h}</span><span class="dt">{d}</span></a>' for d,p,h,u in PRESS)
PAGES["press.html"] = ("Press — Muse by Tom Aikens","Reviews, awards and press for Muse by Tom Aikens: Michelin star, five AA Rosettes, Harden's and Restaurant & Bar Design Awards.",
 page_head("Press","What they said.",img="drinks-cab.jpg",alt="The drinks cabinet",lede="A Michelin star in the first year, five AA Rosettes, and a room that won its own award. Press enquiries to <a class=\"tl\" href=\"mailto:grace@tomaikens.co.uk\">grace@tomaikens.co.uk</a>.") + f'''
<section>
  <div class="grid g-2" style="grid-template-columns:1fr 1fr">
    <blockquote class="quote">“Opening of the year.”<cite>Grace Dent, The Guardian</cite></blockquote>
    <blockquote class="quote">One Michelin star, awarded in the restaurant's first year.<cite>Michelin Guide Great Britain &amp; Ireland</cite></blockquote>
  </div>
  <div class="awards">
    <div>Michelin star<small>Since 2021</small></div>
    <div>Five AA Rosettes<small>AA Hospitality Awards, 2023</small></div>
    <div>Harden's Top 100<small>UK Restaurants, 2023</small></div>
    <div>Restaurant &amp; Bar Design Awards<small>Winner, 2021</small></div>
  </div>
</section>
<section class="dark" style="padding-top:clamp(60px,7vw,100px)">
  <div class="chapter">Selected press</div>
  <div class="press-list">{press_html}</div>
  <p class="mute" style="margin-top:30px">A fuller archive is available on request.</p>
</section>
''')

# ---------------- CONTACT ----------------
PAGES["contact.html"] = ("Contact — Muse by Tom Aikens","Muse by Tom Aikens, 38 Groom Place, Belgravia, London SW1X 7BA. Open for lunch Wednesday to Saturday and dinner Tuesday to Saturday.",
 page_head("Contact","Find us at the end of the mews.",img="muse-building.jpg",alt="Groom Place",lede="Groom Place is a quiet cobbled mews a few minutes' walk from Hyde Park Corner and Victoria.") + f'''
<section>
  <div class="grid g-3">
    <div><h3 style="font-style:italic;color:var(--copper);font-size:20px;margin-bottom:14px">Where</h3><address style="font-style:normal;line-height:1.7">38 Groom Place<br>Belgravia<br>London SW1X 7BA</address></div>
    <div><h3 style="font-style:italic;color:var(--copper);font-size:20px;margin-bottom:14px">When</h3><dl class="spec"><dt>Lunch</dt><dd>Wed – Sat, 12.30 – 1.30pm</dd><dt>Dinner</dt><dd>Tue – Sat, 6.00 – 8.00pm</dd><dt>Closed</dt><dd>Sunday and Monday</dd></dl><p class="small mute" style="margin-top:12px">Times shown are last bookings.</p></div>
    <div><h3 style="font-style:italic;color:var(--copper);font-size:20px;margin-bottom:14px">Reach us</h3><dl class="spec"><dt>Call</dt><dd><a href="tel:+442033012903">+44 (0)20 3301 2903</a></dd><dt>Reservations and events</dt><dd><a href="mailto:info@musebytomaikens.co.uk">info@musebytomaikens.co.uk</a></dd><dt>Press</dt><dd><a href="mailto:grace@tomaikens.co.uk">grace@tomaikens.co.uk</a></dd></dl></div>
  </div>
  <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a table</a><a class="btn" href="{VOUCH}" target="_blank" rel="noopener">Gift vouchers</a><a class="btn" href="private-hire.html">Private hire</a></div>
  <div class="ph pano" style="margin-top:70px"><iframe title="Map of Muse, 38 Groom Place" src="https://www.google.com/maps?q=38+Groom+Place,+London+SW1X+7BA&output=embed" style="position:absolute;inset:0;width:100%;height:100%;border:0;filter:grayscale(1) contrast(.9)" loading="lazy"></iframe></div>
</section>
''')

for fname,(title,desc,body) in PAGES.items():
    with open(os.path.join(OUT,fname),"w") as f:
        f.write(head(title,desc)+header(fname)+body+FOOTER)
    print("wrote",fname)
