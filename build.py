#!/usr/bin/env python3
"""Generates the Muse site pages from shared chrome + per-page bodies."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))
BOOK = "https://www.sevenrooms.com/reservations/musebytomaikens"
VOUCH = "https://musebytomaikens.vouchable.co.uk"
NAV = [("about.html","About"),("christmas.html","Christmas"),("menus.html","Menus"),("whats-on.html","What's On"),("private-hire.html","Private Hire"),("suppliers.html","Suppliers"),("gallery.html","Gallery"),("press.html","Press"),("contact.html","Contact")]

BASE = "https://musebytomaikens.co.uk"
PDF10 = "https://musebytomaikens.co.uk/wp-content/uploads/2026/10/A5-10-Courses-Tasting-14.10.26.pdf"
SCHEMA = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"Restaurant","name":"Muse by Tom Aikens","url":"https://musebytomaikens.co.uk/","image":"https://musebytomaikens.co.uk/img/kitchen-counter.jpg","telephone":"+44 20 3301 2903","email":"info@musebytomaikens.co.uk","priceRange":"££££","servesCuisine":"Modern British","address":{"@type":"PostalAddress","streetAddress":"38 Groom Place","addressLocality":"London","addressRegion":"Belgravia","postalCode":"SW1X 7BA","addressCountry":"GB"},"geo":{"@type":"GeoCoordinates","latitude":51.4997,"longitude":-0.1509},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Wednesday","Thursday","Friday","Saturday"],"opens":"12:30","closes":"13:30"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"18:00","closes":"20:00"}],"acceptsReservations":"https://www.sevenrooms.com/reservations/musebytomaikens","founder":{"@type":"Person","name":"Tom Aikens"},"award":["Michelin star","Five AA Rosettes"],"sameAs":["https://www.instagram.com/musebytomaikens","https://www.facebook.com/Muse-by-Tom-Aikens-106260100800055"]}</script>"""
def head(title, desc, fname="index.html", image="img/kitchen-counter.jpg", schema=False):
    url = BASE + "/" + ("" if fname=="index.html" else fname)
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Muse by Tom Aikens">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FAF8F4">
{SCHEMA if schema else ""}
<link rel="icon" href="img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css?v=24">
</head>
<body>
<a class="sr" href="#main">Skip to content</a>
'''

def header(current):
    links = "".join(f'<a href="{h}"{" class=on" if h==current else ""}>{t}</a>' for h,t in NAV if h in ("about.html","menus.html","whats-on.html","christmas.html","contact.html"))
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
    <a href="christmas.html" data-img="img/dining-area.jpg">Christmas</a>
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
      <nav><a href="about.html">About</a><a href="christmas.html">Christmas</a><a href="suppliers.html">Suppliers</a><a href="whats-on.html">What's on</a><a href="press.html">Press</a><a href="careers.html">Careers</a></nav>
    </div>
    <div>
      <h4>News and new dates</h4>
      <form class="news"><label class="sr" for="em">Email</label><input id="em" type="email" placeholder="Your email" required><button type="submit">Subscribe</button></form>
      <nav style="margin-top:22px"><a href="https://www.instagram.com/musebytomaikens" target="_blank" rel="noopener">Instagram</a><a href="https://www.facebook.com/Muse-by-Tom-Aikens-106260100800055" target="_blank" rel="noopener">Facebook</a></nav>
    </div>
  </div>
  <div class="foot-bot">
    <div>© Muse by Tom Aikens</div>
    <nav><a href="privacy.html">Privacy</a><a href="careers.html">Careers</a></nav>
  </div>
</footer>
<script src="js/site.js?v=21"></script>
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
    <p class="thesis"><span class="fixed">Every dish here began as</span> <span class="memories" aria-live="polite"><a class="memory" href="menus.html#tasting">a memory.</a><a class="memory" href="menus.html#c1">a morning baking with my mother.</a><a class="memory" href="menus.html#c1">fruit picked with my brother Robert.</a><a class="memory" href="menus.html#c7">a bottle my father opened.</a><a class="memory" href="menus.html#c6">shellfish landing in a Paris kitchen.</a><a class="memory" href="menus.html#c3">two stars at twenty-six.</a><a class="memory" href="menus.html#c8">wild grouse from the Pennine moors.</a></span></p>
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
    <a class="mcard" href="menus.html#tasting"><div class="flip">
      <div class="face">
        <div class="ph"><img src="img/onion.jpg" alt="Onion, truffle, egg yolk" loading="lazy"></div>
        <div class="mc-body"><div class="mc-k">Ten courses</div><h3>The Tasting Menu</h3><p>The full story, from the garden in Norfolk to the moors of Yorkshire. Lunch and dinner, Tuesday to Saturday.</p><div class="mc-foot"><span class="mc-price">£195</span><span class="mc-link">View menu</span></div></div>
      </div>
      <div class="face back"><div><div class="mc-k">From the ten courses</div><ol><li><i>From a Humble Beginning</i>Onion, Truffle, Egg Yolk</li><li><i>French Jealousy!</i>Scallop, Artichoke, Apple</li><li><i>Made in Great Britain</i>Grouse, Turnip, Elderberries</li><li><i>Life Has Never Been So Sweet</i>Plum, Cardamom, Grains</li></ol></div><span class="mc-link">All ten courses</span></div>
    </div></a>
    <a class="mcard" href="menus.html#lunch"><div class="flip">
      <div class="face">
        <div class="ph"><img src="img/turbot.jpg" alt="Turbot in a gold-rimmed bowl" loading="lazy"></div>
        <div class="mc-body"><div class="mc-k">Six courses</div><h3>Lunch Tasting</h3><p>The shorter telling, for a long lunch. Thursday to Saturday.</p><div class="mc-foot"><span class="mc-price">£105</span><span class="mc-link">View menu</span></div></div>
      </div>
      <div class="face back"><div><div class="mc-k">From the six courses</div><ol><li><i>Forever Picking</i>Snacks of the season</li><li><i>Making &amp; Breaking</i>Sourdough, cultured butter</li><li><i>The Love Affair Continues</i>Turbot, Duck Confit, Mash</li><li><i>Life Has Never Been So Sweet</i>Plum, Cardamom, Grains</li></ol></div><span class="mc-link">The six courses</span></div>
    </div></a>
    <a class="mcard" href="menus.html#alacarte"><div class="flip">
      <div class="face">
        <div class="ph"><img src="img/venison.jpg" alt="Venison, beetroot, blackberry" loading="lazy"></div>
        <div class="mc-body"><div class="mc-k">Two or three courses</div><h3>À la Carte</h3><p>Choose your own way through the season. Lunch and dinner, Tuesday to Friday.</p><div class="mc-foot"><span class="mc-price">£160 / £195</span><span class="mc-link">View menu</span></div></div>
      </div>
      <div class="face back"><div><div class="mc-k">Choose from</div><ol><li><i>To begin</i>Onion, Truffle, Egg Yolk <em style="color:var(--copper)">or</em> Crab, Celeriac, Pear</li><li><i>Then</i>Turbot, Duck Confit, Mash <em style="color:var(--copper)">or</em> Grouse, Turnip, Elderberries</li><li><i>To finish</i>Figs &amp; Leaves <em style="color:var(--copper)">or</em> Plum, Cardamom, Grains</li></ol></div><span class="mc-link">The à la carte</span></div>
    </div></a>
  </div>
  <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a table</a></div>
</section>

<section class="bleed-row">
  {ph("tartare.jpg","Venison tartare, hazelnut tuile","plx",'data-plx="12"')}{ph("spread.jpg","The autumn table","plx",'data-plx="18"')}{ph("scallop.jpg","Scallop, celeriac, hen of the woods","plx",'data-plx="12"')}
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

<section class="dark" id="press" style="padding-top:0">
  <div class="reel"><span><q>Opening of the year</q><cite>Grace Dent, The Guardian</cite><q>Childhood memories on a plate</q><cite>Metro</cite><q>One of the best chef's tables in London</q><cite>Square Meal</cite><q>Dining gets personal</q><cite>Elite Traveler</cite><q>Among London's most romantic restaurants</q><cite>ELLE</cite></span><span aria-hidden="true"><q>Opening of the year</q><cite>Grace Dent, The Guardian</cite><q>Childhood memories on a plate</q><cite>Metro</cite><q>One of the best chef's tables in London</q><cite>Square Meal</cite><q>Dining gets personal</q><cite>Elite Traveler</cite><q>Among London's most romantic restaurants</q><cite>ELLE</cite></span></div>
  <div class="grid g-2" style="grid-template-columns:1fr 1fr;margin-top:clamp(60px,8vw,120px)">
    <blockquote class="quote">“Opening of the year.”<cite>Grace Dent, The Guardian</cite></blockquote>
    <blockquote class="quote">One Michelin star, awarded in the restaurant's first year.<cite>Michelin Guide Great Britain &amp; Ireland</cite></blockquote>
  </div>
  <div class="awards"><div>Michelin star<small>Since 2021</small></div><div>Five AA Rosettes<small>AA Hospitality Awards</small></div><div>Harden's Top 100<small>UK Restaurants</small></div><div>Restaurant &amp; Bar Design Awards<small>Winner, 2021</small></div></div>
</section>

<section class="tint" id="christmas" style="padding-top:clamp(60px,7vw,100px);padding-bottom:clamp(60px,7vw,100px)">
  <div class="grid g-2" style="align-items:center">
    <div><div class="chapter">December</div><h2>Christmas, told the Muse way.</h2></div>
    <div><p class="lede">A festive tasting menu written as stories, parties for six to twenty-five, the Muse Christmas Hamper, and vouchers for the people who are hard to buy for.</p><div class="cta"><a class="btn solid" href="christmas.html">Christmas at Muse</a><a class="btn" href="{VOUCH}" target="_blank" rel="noopener">Gift vouchers</a></div></div>
  </div>
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
 page_head("About","Tom Aikens, and the house he built from memory.",img="img2.jpg",alt="Tom Aikens at the pass",lede="The youngest British chef to hold two Michelin stars, back at the pass in a 25-cover mews house where every menu traces the moments and people that made him.") + f'''
<section>
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

<section class="tint">
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

<section class="statement">
  <p><i style="color:var(--copper)">muse</i> <span style="font-family:var(--sans);font-size:.6em;letter-spacing:.1em;color:var(--mist)">n.</span> A person or personified force who is the source of creative inspiration for a creative artist.</p>
  <div class="rule"></div>
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
 page_head("Menus","Each course is a memory, cooked.",img="spread.jpg",alt="A dish from the tasting menu",lede="Tom's menus trace the moments and people that made him a chef — a childhood kitchen in Norfolk, the great Paris and London kitchens, the produce of a small island. Every course carries the title of the memory it comes from.") + f"""
<nav class="subnav" aria-label="Menus"><a href="#tasting">Ten-course tasting</a><a href="#lunch">Six-course lunch</a><a href="#alacarte">À la carte</a><a href="#wine">Wine</a><a href="#creators">Culinary Creators</a></nav>

<section class="dark" id="tasting" style="padding-bottom:0">
  <div class="grid g-2" style="align-items:end;margin-bottom:8vh">
    <div><div class="chapter">Autumn · ten courses · £195</div><h2>The Tasting Menu, chapter by chapter.</h2></div>
    <div><p class="lede">Scroll slowly. Each course carries the title of the memory it comes from; the dishes move as the season does. Lunch and dinner, Tuesday to Saturday.</p><div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a table</a><a class="btn" href="{PDF10}" target="_blank" rel="noopener">Download (PDF)</a></div></div>
  </div>
  <div class="chapters">
    <div class="stage"><div class="ph"><div class="cnum">01</div><div class="frame">{"".join(f'<img src="img/{im}" alt="" loading="lazy">' for im in ["spread.jpg","gallery-1.jpg","onion.jpg","culinary-creators.jpg","tartare.jpg","scallop.jpg","turbot.jpg","venison.jpg","trifle.jpg","img1.jpg"])}</div></div></div>
    <ol class="chapter-list">{"".join(f'<li class="chp" id="c{i+1}"><div class="n">Course {i+1:02d} of 10</div><div class="ct">{t}</div><div class="cd">{d}</div><div class="cm">{m}</div></li>' for i,(t,d,m) in enumerate(COURSES))}</ol>
  </div>
  <div style="padding:60px 0 clamp(80px,10vw,150px)">{NOTE}</div>
</section>

<section id="lunch">
  <div class="grid g-2" style="align-items:start">
    <div class="sticky">
      <div class="chapter">Autumn · six courses</div>
      <h2>Lunch Tasting</h2>
      <div class="facts"><div>£105<small>per person</small></div><div>Thu – Sat<small>lunch only</small></div></div>
      <p style="margin-top:28px">The shorter telling: six chapters from the ten, for a long lunch in the mews.</p>
      {NOTE}
      <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book lunch</a><a class="btn" href="https://musebytomaikens.co.uk/wp-content/uploads/2026/10/A5-6-Courses-Tasting-14.10.26.pdf" target="_blank" rel="noopener">Download (PDF)</a></div>
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
      <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a table</a><a class="btn" href="https://musebytomaikens.co.uk/wp-content/uploads/2026/10/A-la-carte-Menu-14.10.26.pdf" target="_blank" rel="noopener">Download (PDF)</a></div>
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
      <div class="cta"><a class="btn" href="https://musebytomaikens.co.uk/wp-content/uploads/2026/11/Winelist-31.10.26.pdf" target="_blank" rel="noopener">Wine list (PDF)</a><a class="btn" href="whats-on.html">Wine Cellar Series</a></div>
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
 "The Culinary Creators series with Jackson Boxer, the Wine Cellar Series every Tuesday, and Women in Wine at Muse by Tom Aikens, Belgravia.",
 page_head("What's on","Nights that only happen once.",img="kitchen-counter.jpg",alt="The counter at Muse",lede="The Culinary Creators series brings some of Britain's most acclaimed chefs to the counter for a single evening alongside Tom. Then there is the cellar, which opens every Tuesday.") + f"""
<section>
  <div class="chapter">Coming up</div>
  <div class="event-rows">
    <article class="event-row" id="jackson-boxer">
      <div class="ph"><img src="img/culinary-creators.jpg" alt="The counter at Muse" loading="lazy"></div>
      <div class="ev-body">
        <div class="ev-k">Culinary Creators · 13 January</div>
        <h2>Tom Aikens × Jackson Boxer</h2>
        <p>Eight courses, cooked live at the counter and split evenly between the two chefs. Jackson Boxer is the self-taught chef-restaurateur behind Brunswick House in Vauxhall, Orasay and now Dove in Notting Hill, and Vesper on Exmouth Market — produce-first, seasonal, and with an eye for a room.</p>
        <div class="ev-foot"><span class="ev-price">£225<small>per person</small></span><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Reserve a seat</a></div>
      </div>
    </article>
    <article class="event-row" id="wine-cellar">
      <div class="ph"><img src="img/grapes.jpg" alt="Grapes on the vine" loading="lazy"></div>
      <div class="ev-body">
        <div class="ev-k">Wine Cellar Series · Every Tuesday</div>
        <h2>An evening built around the cellar.</h2>
        <p>Each Tuesday, Tom and head sommelier Elisa Marchini pair wines to the evening's seasonal dishes. The opening run is devoted to the Languedoc — warm-climate Grenache, Syrah and Carignan — with new regions to follow. Small numbers, around the counter.</p>
        <div class="ev-foot"><span class="ev-price">£65<small>wine pairing, per person, booked in advance</small></span><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book a Tuesday</a></div>
      </div>
    </article>
  </div>
</section>

<section class="dark" id="series">
  <div class="grid g-2" style="align-items:start">
    <div class="sticky">
      <div class="chapter">The Culinary Creators series</div>
      <h2>Two chefs, eight dishes, one night.</h2>
      <p style="margin-top:20px">A run of one-off evenings with the chefs and hospitality figures shaping the industry now — from classical fine-dining veterans to cooks who came up outside it. Tom and the guest cook eight dishes between them, live, in a room relaxed enough to watch it happen.</p>
      <p class="small mute" style="margin-top:16px">Menus are written for each night and released closer to the date. To hear about new dates first, join the newsletter at the foot of the page.</p>
    </div>
    <div>
      <div class="chapter">The series so far</div>
      <div class="index" style="columns:1">
        <div><b>Daniel Clifford</b><i>19 May</i></div>
        <div><b>Ruth Hansom</b><i>2 June</i></div>
        <div><b>Alberto Landgraf</b><i>17 June</i></div>
        <div><b>Ben Marks</b><i>8 July</i></div>
        <div><b>Jonny Drain</b><i>9 September</i></div>
        <div><b>Merlin Labron-Johnson</b><i>23 September</i></div>
        <div><b>Jackson Boxer</b><i>13 January</i></div>
      </div>
      <div class="chapter" style="margin-top:50px">Also cooking in the series</div>
      <p class="mute" style="font-size:16px">Emily English, Sam Black, Thomas Straker, Matthew Ryle, John Williams, Ruthie Rogers, Jim Ainsworth, Max Coen, Tyler Butt, Adip Adhikari, Andy Hearnden, Joseph Lidgerwood, Agnar Sverrisson.</p>
    </div>
  </div>
</section>

<section class="tint" id="women-in-wine">
  <div class="grid g-2">
    <div><div class="chapter">Women in Wine · 14 October</div><h2>Four winemakers, four estates, one table.</h2><p style="margin-top:20px">An evening of wine with food from the kitchen, the makers in the room to talk through their estates and the thinking behind each pour.</p></div>
    <div class="index" style="columns:1">
      <div style="display:block"><b>Beatriz Cabral Almeida</b><p style="font-size:15px;color:var(--ink-2)">Quinta dos Carvalhais, Dão, Portugal — a winemaker who came to the cellar through microbiology.</p></div>
      <div style="display:block"><b>Sofia Ricasoli</b><p style="font-size:15px;color:var(--ink-2)">Fifth generation of the Ricasoli family, and founder of Innesto, making her own Tuscan wines.</p></div>
      <div style="display:block"><b>Sophie Cossy</b><p style="font-size:15px;color:var(--ink-2)">Took over her family's Champagne house in the Montagne de Reims at twenty-five; vines there since 1764.</p></div>
      <div style="display:block"><b>Laura Iverson</b><p style="font-size:15px;color:var(--ink-2)">Partner and Director at Chêne Bleu, a Provence estate restored from a medieval priory.</p></div>
    </div>
  </div>
</section>
""")

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
      <div class="cta"><a class="btn solid" href="mailto:info@musebytomaikens.co.uk?subject=Private%20dining%20enquiry">Enquire by email</a><a class="btn" href="https://www.dropbox.com/scl/fi/wp0vfcxkwxbc31bhx0jwh/Group-Dining-at-Muse.pdf?rlkey=ujyde62gvma5txxepxyfa2egi&dl=0" target="_blank" rel="noopener">Download the brochure</a></div>
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
<section class="dark">
  <div class="grid g-2" style="align-items:center">
    <div class="ph tall vid"><video controls playsinline preload="metadata" poster="img/producers-poster.jpg"><source src="img/producers.mp4" type="video/mp4"></video></div>
    <div><div class="chapter">A film</div><h2>Tom, with the people who feed the kitchen.</h2><p style="margin-top:20px">To HG Walter in Barons Court, and the farms, boats and mills behind the menu — a short film with Tom on why provenance is the whole story.</p></div>
  </div>
</section>
<section class="sage" style="padding-top:clamp(60px,7vw,100px)">
  <div class="index">{sup_html}</div>
</section>
''')

# ---------------- GALLERY ----------------
GAL = [("kitchen-counter.jpg","The counter"),("img1.jpg","Plating at the pass"),("muse-building.jpg","Groom Place"),("img2.jpg","Sauce at the table"),("gallery-1.jpg","Bowls"),("dining-area.jpg","The dining room"),("drinks-cab.jpg","The drinks cabinet"),("img3.jpg","A course"),("private-party-1.jpg","Set for a private dinner"),("gallery-3.jpg","Stacked bowls"),("img4.jpg","Tom plating"),("culinary-creators.jpg","Sourdough and preserves"),("tom.jpg","Tom Aikens")]
GALCAP=[("xmas-table.jpg","The Christmas table","wide"),("onion.jpg","Onion, truffle, egg yolk","tall"),("kitchen-counter.jpg","The counter","wide"),("venison.jpg","Venison, beetroot, blackberry","tall"),("spread.jpg","The autumn table","wide"),("turbot.jpg","Turbot","tall"),("tartare.jpg","Venison tartare","tall"),("scallop.jpg","Scallop, hen of the woods","tall"),("trifle.jpg","Blackberry trifle","tall"),("img1.jpg","Cod, courgette, nasturtium","wide"),("muse-building.jpg","Groom Place","tall"),("img2.jpg","Tom at the pass","wide"),("tom.jpg","Tom Aikens","tall"),("dining-area.jpg","The dining room","wide"),("drinks-cab.jpg","The drinks cabinet","tall"),("img3.jpg","A course","tall"),("private-party-1.jpg","Set for a private dinner","wide"),("gallery-3.jpg","The counter stools","tall"),("img4.jpg","Sauce at the table","wide"),("gallery-1.jpg","Hand-thrown bowls","tall"),("culinary-creators.jpg","Sourdough and preserves","wide")]
PAGES["gallery.html"] = ("Gallery — Muse by Tom Aikens","Photographs of Muse by Tom Aikens: the mews house, the counter, the dining room and the food.",
 page_head("Gallery","The house, the counter, the plates.",img="img2.jpg",alt="Sauce at the table",lede="Drag, or scroll sideways.") + '<section class="strip-wrap"><div class="film-hint"><span>Drag to move</span><span>' + str(len(GALCAP)) + ' photographs</span></div><div class="filmstrip">' + "".join(f'<div class="ph {c}"><img src="img/{f}" alt="{a}" draggable="false"><span class="hshade"></span><span class="hc">{a}</span></div>' for f,a,c in GALCAP) + '</div></section>')

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
<section class="dark" style="padding-top:0">
  <div class="reel"><span><q>Opening of the year</q><cite>Grace Dent, The Guardian</cite><q>Childhood memories on a plate</q><cite>Metro</cite><q>One of the best chef's tables in London</q><cite>Square Meal</cite><q>Dining gets personal</q><cite>Elite Traveler</cite><q>Among London's most romantic restaurants</q><cite>ELLE</cite></span><span aria-hidden="true"><q>Opening of the year</q><cite>Grace Dent, The Guardian</cite><q>Childhood memories on a plate</q><cite>Metro</cite><q>One of the best chef's tables in London</q><cite>Square Meal</cite><q>Dining gets personal</q><cite>Elite Traveler</cite><q>Among London's most romantic restaurants</q><cite>ELLE</cite></span></div>
  <div class="chapter" style="margin-top:clamp(60px,8vw,110px)">Selected press</div>
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


PAGES["careers.html"] = ("Careers — Muse by Tom Aikens","Join the team at Muse by Tom Aikens, a Michelin-starred 25-cover restaurant in Belgravia. Send your CV to info@musebytomaikens.co.uk.",
 page_head("Careers","Twenty-five covers. Every detail.",img="img2.jpg",alt="Tom Aikens plating at the pass",lede="A room this small has nowhere to hide, which is exactly why people choose to work here.") + f"""
<section>
  <div class="grid g-2">
    <div><div class="chapter">Working at Muse</div><h2>Who we look for.</h2></div>
    <div>
      <p class="lede">Muse earned its Michelin star in its first year and has held it since. The room, the menu, the service and the team are what make it — and the team is the part that can't be bought.</p>
      <p style="margin-top:1.2em">We look for people who are dedicated, self-motivated and curious about food — front of house and kitchen — with a care for organisation that matches ours. If that's you, we'd like to hear from you whether or not a role is advertised.</p>
      <div class="cta"><a class="btn solid" href="mailto:info@musebytomaikens.co.uk?subject=Working%20at%20Muse">Send your CV</a></div>
      <p class="small mute" style="margin-top:18px">info@musebytomaikens.co.uk</p>
    </div>
  </div>
</section>
""")

PAGES["privacy.html"] = ("Privacy — Muse by Tom Aikens","How Muse by Tom Aikens collects and uses personal information, and the terms of use for this website.",
 page_head("Privacy","Privacy and terms.",img="dining-area.jpg",alt="The dining room at Muse",lede="How we handle your information when you book, write to us or use this site.") + """
<section class="legal">
  <h2>Privacy</h2>
  <p><b>Who we are.</b> This website is operated by Muse by Tom Aikens, 38 Groom Place, London SW1X 7BA. You can reach us at info@musebytomaikens.co.uk.</p>
  <p><b>What we collect.</b> When you book a table through SevenRooms, buy a voucher through Vouchable, email us, or join our newsletter, we receive the details you give — typically your name, contact details, the date and size of your booking, and any dietary or access requirements. This site sets no tracking cookies of its own.</p>
  <p><b>How we use it.</b> To take and manage your reservation, to contact you about it, to meet dietary and access needs, and — only where you have asked for it — to send news of menus and events. We do not sell or rent personal information.</p>
  <p><b>Who we share it with.</b> Our reservation, voucher and email providers process data on our behalf under their own privacy terms: SevenRooms (reservations), Vouchable (vouchers) and our email platform (newsletter). We share nothing else except where the law requires.</p>
  <p><b>How long we keep it.</b> Booking records for as long as we need them for accounting and guest history; newsletter details until you unsubscribe, which you can do from any email.</p>
  <p><b>Your rights.</b> You can ask to see, correct or delete the personal information we hold about you by emailing info@musebytomaikens.co.uk. You can also complain to the Information Commissioner's Office at ico.org.uk.</p>
  <h2 style="margin-top:60px">Terms of use</h2>
  <p>The text, photographs, film and design on this site belong to Muse by Tom Aikens or are used with permission, and may be viewed for personal, non-commercial purposes only. Menus and prices are a guide to the season and may change without notice. Links to other sites are provided for convenience; we are not responsible for their content. These terms are governed by the law of England and Wales.</p>
  <p class="small mute">Last reviewed November 2026.</p>
</section>
""")

PAGES["404.html"] = ("Page not found — Muse by Tom Aikens","That page isn't here.",
 f"""<section class="page-head" style="min-height:70vh;display:grid;align-content:center">
  <div class="chapter">404</div>
  <h1>That page has moved on, like the season.</h1>
  <p class="lede">Try the menus, what's on, or the front door.</p>
  <div class="cta"><a class="btn solid" href="index.html">Home</a><a class="btn" href="menus.html">Menus</a><a class="btn" href="contact.html">Contact</a></div>
</section>
""")

PAGES["christmas.html"] = ("Christmas at Muse — Muse by Tom Aikens","Christmas at Muse by Tom Aikens: a festive tasting menu told in stories, Christmas parties for 6 to 25 in a Belgravia mews house, the Muse Christmas Hamper, and gift vouchers.",
 page_head("Christmas","Christmas, told the Muse way.",img="xmas-table.jpg",alt="The Christmas table at Muse",lede="A festive tasting menu written as stories, a mews house dressed for December, parties for six to twenty-five, and a hamper of Tom's own making.") + f"""
<section>
  <div class="overlap">
    <div class="ph big vid"><video muted loop playsinline autoplay preload="metadata" poster="img/xmas-poster.jpg"><source src="img/xmas.mp4" type="video/mp4"></video></div>
    <div class="text">
      <div class="chapter">The Christmas tasting menu</div>
      <h2>Every course a Christmas story.</h2>
      <p style="margin-top:20px">Through December the tasting menu turns to the season, each course carrying a story of Christmas the way the autumn menu carries Tom's memories. It opens with <i>Just Around the Corner</i> — the first taste of Christmas: sprouts, bread sauce and bacon — and the room is dressed to match: enough to feel special, still elegant.</p>
      <p style="margin-top:1em">Lunch Wednesday to Saturday, dinner Tuesday to Saturday. December tables go first.</p>
      <div class="cta"><a class="btn solid" href="{BOOK}" target="_blank" rel="noopener">Book for December</a><a class="btn" href="menus.html">The menus</a></div>
    </div>
  </div>
</section>

<section class="dark">
  <div class="grid g-2">
    {ph("private-party-1.jpg","The dining room set for a Christmas party","wide")}
    <div>
      <div class="chapter">Christmas parties</div>
      <h2>The house, for your table only.</h2>
      <p style="margin-top:20px">From a counter for six to the whole townhouse for twenty-five. Groups of up to six take the full tasting menu; from seven, a six-course tasting or a seasonal three-course menu the host curates with Sébastien in advance.</p>
      <div class="facts"><div>6 – 25<small>guests</small></div><div>3<small>ways to take the house</small></div></div>
      <div class="cta"><a class="btn solid" href="mailto:info@musebytomaikens.co.uk?subject=Christmas%20party%20at%20Muse">Enquire for December</a><a class="btn" href="private-hire.html">Private hire</a></div>
    </div>
  </div>
</section>

<section class="tint">
  <div class="grid g-21">
    <div>
      <div class="chapter">The Muse Christmas Hamper</div>
      <h2>Christmas, in a box, from Tom.</h2>
      <p style="margin-top:20px">The spirit of Muse packed for home. Delivery or collection from the mews from 17 December.</p>
      <div class="index" style="columns:1;margin-top:34px">
        <div><b>Vintage sloe gin</b><i>wild sloes, slowly matured</i></div>
        <div><b>Elder &amp; blackberry cassis</b><i>foraged by Tom, infused and aged</i></div>
        <div><b>Muse mince pies</b><i>Tom's aged mincemeat</i></div>
        <div><b>Tom's whisky gummies</b><i>the classic</i></div>
        <div><b>Brandy butter</b><i>a Christmas essential</i></div>
        <div><b>Tom's tips &amp; tricks for Christmas</b><i>in the box</i></div>
      </div>
      <div class="cta"><a class="btn solid" href="https://tomaikens.co.uk/?p=20029" target="_blank" rel="noopener">Order the hamper</a></div>
    </div>
    {ph("trifle.jpg","Blackberry trifle in a coupe","tall")}
  </div>
</section>

<section>
  <div class="grid g-2" style="align-items:center">
    <div><div class="chapter">Gift vouchers</div><h2>Give someone a night at the counter.</h2></div>
    <div><p class="lede">A tasting menu, a lunch, or a sum towards either — sent by email, valid for a year. The present that arrives on time.</p><div class="cta"><a class="btn solid" href="{VOUCH}" target="_blank" rel="noopener">Buy a voucher</a></div></div>
  </div>
</section>
""")

OGIMG = {"index.html":"img/kitchen-counter.jpg","about.html":"img/tom.jpg","menus.html":"img/spread.jpg","whats-on.html":"img/kitchen-counter.jpg","private-hire.html":"img/private-party-1.jpg","suppliers.html":"img/provenance.jpg","gallery.html":"img/dining-area.jpg","press.html":"img/drinks-cab.jpg","contact.html":"img/muse-building.jpg","christmas.html":"img/xmas-table.jpg"}
for fname,(title,desc,body) in PAGES.items():
    with open(os.path.join(OUT,fname),"w") as f:
        f.write(head(title,desc,fname,OGIMG.get(fname,"img/kitchen-counter.jpg"),schema=fname in ("index.html","contact.html"))+header(fname)+body+FOOTER)
    print("wrote",fname)
with open(os.path.join(OUT,"sitemap.xml"),"w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'  <url><loc>{BASE}/{"" if n=="index.html" else n}</loc></url>\n' for n in PAGES if n!="404.html")+'</urlset>\n')
with open(os.path.join(OUT,"robots.txt"),"w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
