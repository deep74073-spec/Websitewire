from pathlib import Path
from html import escape
import json

ROOT = Path(".")
ROOT.mkdir(exist_ok=True)
LOGO = "/Website_wire.png"
ADSENSE = '''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9100998938332588" crossorigin="anonymous"></script>'''

css = """
:root{--blue:#155eef;--ink:#182230;--muted:#667085;--line:#e4e7ec;--bg:#f8faff;--green:#087443}
*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif;color:var(--ink);line-height:1.7;background:#fff}
a{color:var(--blue);text-decoration:none}a:hover{text-decoration:underline}
header{border-bottom:1px solid var(--line);background:white;position:sticky;top:0;z-index:5}
.nav{max-width:1120px;margin:auto;padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}
.brand{display:inline-flex;align-items:center;gap:9px;font-size:23px;font-weight:800;color:var(--ink)}
.brand img{width:42px;height:42px;object-fit:contain}.links{display:flex;gap:17px;flex-wrap:wrap;font-size:14px;font-weight:600}
main{max-width:1120px;margin:auto;padding:28px 20px 60px}.hero{background:linear-gradient(135deg,#eef4ff,#f7faff);padding:42px 28px;border-radius:22px}
h1{font-size:clamp(30px,5vw,48px);line-height:1.15;margin:0 0 16px}h2{line-height:1.25;margin-top:28px}
p{color:#475467}.muted{color:var(--muted)}.search{display:flex;gap:8px;max-width:650px;margin-top:24px}
input,textarea,select{font:inherit;border:1px solid #d0d5dd;border-radius:10px;padding:12px;width:100%;background:white}
button,.btn{display:inline-block;border:0;border-radius:10px;padding:12px 17px;background:var(--blue);color:white;font-weight:700;cursor:pointer}
.btn.secondary{background:white;color:var(--blue);border:1px solid #b2ccff}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin:20px 0}
.card{border:1px solid var(--line);border-radius:16px;padding:20px;background:white}
.card h3{margin:0 0 8px}.card p{margin:7px 0}.tag{display:inline-block;font-size:12px;background:#eef4ff;color:#1849a9;padding:4px 9px;border-radius:30px}
.notice{background:#fffaeb;border:1px solid #fedf89;padding:14px;border-radius:12px;font-size:14px}
.article{max-width:800px}.article li{margin:8px 0}.cta{background:#eff8ff;padding:22px;border-radius:15px;margin:25px 0}
footer{background:#101828;color:white;padding:30px 20px}footer a{color:#d1e0ff}footer p{color:#d0d5dd}
.footer-inner{max-width:1120px;margin:auto}.footer-links{display:flex;gap:16px;flex-wrap:wrap}
.tool-output{white-space:pre-wrap;background:#f2f4f7;padding:14px;border-radius:10px}
@media(max-width:760px){.grid{grid-template-columns:1fr}.hero{padding:30px 20px}.links{gap:11px}.search{flex-direction:column}.nav{align-items:flex-start}main{padding:22px 16px 45px}}
"""

def page(title, description, body, path="/"):
    canonical = "https://websitewire.co.in" + path
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="{LOGO}">
<meta name="robots" content="index,follow">
{ADSENSE}
<style>{css}</style></head><body>
<header><nav class="nav">
<a class="brand" href="/"><img src="{LOGO}" alt="Websitewire logo">Websitewire</a>
<div class="links">
<a href="/">Home</a><a href="/articles/">Articles</a>
<a href="/buying-guides/">Buying Guides</a><a href="/tools/">Free Tools</a>
<a href="/services/">Services</a><a href="/contact/">Contact</a>
</div></nav></header>
<main>{body}</main>
<footer><div class="footer-inner">
<a class="brand" href="/" style="color:white"><img src="{LOGO}" alt="">Websitewire</a>
<p>Practical guides, useful tools, product research and website services.</p>
<div class="footer-links"><a href="/about/">About</a><a href="/contact/">Contact</a>
<a href="/privacy-policy/">Privacy Policy</a><a href="/disclaimer/">Affiliate Disclosure</a>
<a href="/terms/">Terms</a></div>
<p>© 2026 Websitewire. All rights reserved.</p>
</div></footer></body></html>"""

def write(path, content):
    f = ROOT / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content, encoding="utf-8")
    print("Created", f)

articles = [
    {
        "slug":"fix-slow-wifi",
        "title":"How to Fix Slow Wi-Fi at Home",
        "desc":"Practical steps to troubleshoot slow Wi-Fi, improve router placement and check your internet connection.",
        "category":"Technology",
        "intro":"Slow Wi-Fi can be caused by router placement, interference, too many connected devices or an internet service issue. Try these checks before spending money on new equipment.",
        "steps":[
            ("Run a speed test","Test near the router and compare the result with your internet plan. Repeat on another device."),
            ("Restart your router","Power it off briefly, then restart it. Wait for the connection to return."),
            ("Improve router placement","Place the router in an open, central location, away from thick walls and metal objects."),
            ("Check connected devices","Pause large downloads and disconnect devices you do not use."),
            ("Check your plan and equipment","If speeds remain low on multiple devices, contact your internet provider before buying a new router.")
        ],
        "related":"See our buying guides for help comparing networking equipment."
    },
    {
        "slug":"create-a-business-website",
        "title":"How to Create a Website for Your Small Business",
        "desc":"A beginner-friendly checklist for planning, creating and launching a small business website.",
        "category":"Websites",
        "intro":"A useful business website explains what you offer, who you help and how customers can contact you. Plan these basics before choosing a design.",
        "steps":[
            ("Choose a clear goal","Decide whether the site should generate enquiries, sell products or showcase your work."),
            ("Plan essential pages","Most small businesses need Home, Services, About, Contact and a Privacy Policy."),
            ("Write useful content","Explain services in plain language and include accurate contact details."),
            ("Check mobile usability","Test the navigation, text, buttons and forms on a phone."),
            ("Publish and maintain","Connect your domain, check HTTPS and update content when your services change.")
        ],
        "related":"Need help? Explore our website development service."
    },
    {
        "slug":"choose-a-web-hosting-plan",
        "title":"How to Choose a Web Hosting Plan",
        "desc":"Understand hosting types, storage, support, backups and renewal prices before selecting a hosting plan.",
        "category":"Websites",
        "intro":"The right hosting depends on your website platform, traffic and technical needs. Compare the full renewal cost and features instead of choosing on introductory price alone.",
        "steps":[
            ("Identify your platform","Static HTML, WordPress and online stores can have different hosting needs."),
            ("Compare total costs","Check renewal pricing, taxes, domain charges and paid add-ons."),
            ("Check security and backups","Look for HTTPS support, reliable backups and clear recovery options."),
            ("Review support","Confirm how you can contact support and whether help is available when you need it."),
            ("Plan for growth","Choose a service that can handle expected traffic without paying for unnecessary features.")
        ],
        "related":"Compare features carefully before purchasing through any provider."
    }
]

def article_html(a):
    steps = "".join(f"<h2>{i}. {escape(h)}</h2><p>{escape(t)}</p>" for i,(h,t) in enumerate(a["steps"],1))
    return page(a["title"]+" | Websitewire", a["desc"],
        f"""<article class="article"><span class="tag">{escape(a['category'])}</span>
<h1>{escape(a['title'])}</h1><p class="muted">Practical guide from Websitewire</p>
<p>{escape(a['intro'])}</p>{steps}
<div class="cta"><h2>Need more help?</h2><p>{escape(a['related'])}</p>
<a class="btn" href="/services/">Explore Websitewire Services</a></div>
<h2>Related resources</h2><ul><li><a href="/articles/">Browse all articles</a></li>
<li><a href="/buying-guides/">Explore buying guides</a></li><li><a href="/contact/">Contact Websitewire</a></li></ul>
<p class="muted">This guide is general information. Check current specifications and provider terms before making a purchase.</p>
</article>""",
        "/articles/"+a["slug"]+".html")

for a in articles:
    write("articles/"+a["slug"]+".html", article_html(a))

article_cards = "".join(
    f'<div class="card"><span class="tag">{escape(a["category"])}</span><h3><a href="/articles/{a["slug"]}.html">{escape(a["title"])}</a></h3><p>{escape(a["desc"])}</p><a href="/articles/{a["slug"]}.html">Read guide →</a></div>'
    for a in articles)

home = f"""
<section class="hero"><span class="tag">Learn • Compare • Build</span>
<h1>Find practical solutions to everyday problems</h1>
<p>Helpful how-to articles, buying guides, free online tools and website services—all in one place.</p>
<form class="search" action="/search.html" method="get">
<input name="q" aria-label="Search Websitewire" placeholder="Search articles and guides..." required>
<button type="submit">Search</button></form>
<p class="muted">Explore trusted information and make more informed decisions.</p></section>
<h2>Explore Websitewire</h2><section class="grid">
<div class="card"><h3>📚 Articles & Guides</h3><p>Step-by-step help for technology, websites and everyday problems.</p><a href="/articles/">Browse articles →</a></div>
<div class="card"><h3>🛒 Buying Guides</h3><p>Compare features and understand what to check before buying.</p><a href="/buying-guides/">Explore guides →</a></div>
<div class="card"><h3>🧰 Free Online Tools</h3><p>Simple browser-based utilities for everyday tasks.</p><a href="/tools/">Use free tools →</a></div>
<div class="card"><h3>💻 Website Services</h3><p>Website development, landing pages and SEO assistance.</p><a href="/services/">View services →</a></div>
<div class="card"><h3>✉️ Contact Us</h3><p>Have a question or need help with a website project?</p><a href="/contact/">Get in touch →</a></div>
<div class="card"><h3>🔎 Search Resources</h3><p>Find a topic using our site search.</p><a href="/search.html">Search Websitewire →</a></div>
</section>
<h2>Featured articles</h2><section class="grid">{article_cards}</section>
<div class="notice"><strong>Affiliate disclosure:</strong> Some future buying-guide links may be affiliate links. If you buy through them, Websitewire may earn a commission at no additional cost to you. Recommendations should be based on useful, accurate information.</div>
"""
write("index.html", page("Websitewire | Helpful Guides, Buying Advice & Web Services",
    "Websitewire helps you solve problems with practical articles, buying guides, free online tools and website development services.", home, "/"))

articles_body = f"<h1>Articles & Problem Solutions</h1><p>Browse practical guides designed to explain problems and possible solutions clearly.</p><section class='grid'>{article_cards}</section>"
write("articles/index.html", page("Articles & How-to Guides | Websitewire","Browse Websitewire how-to articles and practical solutions.",articles_body,"/articles/"))

buying_body = """
<h1>Buying Guides</h1><p>Learn what features to compare before choosing a product. We aim to explain trade-offs, suitability and costs clearly.</p>
<div class="notice"><strong>Affiliate links:</strong> Product links on this page are examples until genuine approved affiliate URLs are added. No purchase link is active yet.</div>
<section class="grid">
<div class="card"><h3>Wi-Fi Routers</h3><p>Compare coverage, Wi-Fi standards, ports, home size and support.</p><a href="/articles/fix-slow-wifi.html">Read Wi-Fi troubleshooting guide →</a></div>
<div class="card"><h3>Web Hosting</h3><p>Compare renewal pricing, backups, support and the platform you need.</p><a href="/articles/choose-a-web-hosting-plan.html">Read hosting guide →</a></div>
<div class="card"><h3>Website Essentials</h3><p>Plan domains, security, backups and tools for your business website.</p><a href="/articles/create-a-business-website.html">Read website guide →</a></div>
</section>
<h2>Product recommendation format</h2><p>For each product, publish verified specifications, pros and cons, who it suits, alternatives, current pricing source and a clearly labelled affiliate link where available.</p>
"""
write("buying-guides/index.html", page("Buying Guides & Comparisons | Websitewire","Learn how to compare products and services with practical buying guides.",buying_body,"/buying-guides/"))

tools_body = """
<h1>Free Online Tools</h1><p>Simple utilities that run in your browser.</p>
<div class="card"><h2>Word Counter</h2><p>Paste or type text to count words, characters and sentences.</p>
<textarea id="wc-text" rows="7" placeholder="Type or paste your text here..."></textarea>
<p><strong>Words:</strong> <span id="wc-words">0</span> · <strong>Characters:</strong> <span id="wc-chars">0</span> · <strong>Sentences:</strong> <span id="wc-sentences">0</span></p>
<button type="button" id="wc-clear">Clear text</button></div>
<script>
const box=document.getElementById('wc-text');
function countText(){const t=box.value;document.getElementById('wc-words').textContent=(t.trim().match(/\\S+/g)||[]).length;document.getElementById('wc-chars').textContent=t.length;document.getElementById('wc-sentences').textContent=(t.match(/[.!?]+(?=\\s|$)/g)||[]).length;}
box.addEventListener('input',countText);document.getElementById('wc-clear').addEventListener('click',()=>{box.value='';countText();});
</script>
"""
write("tools/index.html", page("Free Online Tools | Websitewire","Use free Websitewire browser tools such as the word counter.",tools_body,"/tools/"))

services_body = """
<h1>Websitewire Services</h1><p>Practical support for individuals, creators and small businesses that need a useful web presence.</p>
<section class="grid">
<div class="card"><h3>Website Development</h3><p>Responsive business websites and landing pages planned around your goals.</p><a href="/contact/">Enquire about a website →</a></div>
<div class="card"><h3>SEO Setup</h3><p>On-page titles, descriptions, indexing basics, sitemap checks and internal links.</p><a href="/contact/">Ask about SEO →</a></div>
<div class="card"><h3>Website Improvements</h3><p>Help with mobile layout, content structure, speed and basic maintenance.</p><a href="/contact/">Discuss your project →</a></div>
</section>
<p>Project pricing depends on scope and requirements. Share what you need to receive a suitable response.</p>
"""
write("services/index.html", page("Website Development & SEO Services | Websitewire","Explore Websitewire website development, SEO setup and website improvement services.",services_body,"/services/"))

contact_body = """
<h1>Contact Websitewire</h1><p>Tell us what kind of website help or information you need.</p>
<div class="notice">This static website has no server-side form handler yet. Use the email address you configure below, or connect a trusted form service before publishing a working enquiry form.</div>
<div class="card"><h2>Project enquiry checklist</h2><ul><li>Your name and preferred reply method</li><li>Website or business URL, if available</li><li>What you want built or improved</li><li>Your timeline and approximate budget</li></ul>
<p><strong>Contact email:</strong> Replace <code>YOUR_EMAIL@example.com</code> in this page with your real business email before publishing.</p>
<a class="btn" href="mailto:YOUR_EMAIL@example.com?subject=Websitewire%20Project%20Enquiry">Email Websitewire</a></div>
"""
write("contact/index.html", page("Contact Websitewire","Contact Websitewire about website development, SEO and other project enquiries.",contact_body,"/contact/"))

about_body = """<h1>About Websitewire</h1><p>Websitewire is a growing online resource for practical how-to guides, product research, browser-based tools and website services.</p><p>Our goal is to make information easier to understand so visitors can compare options and decide what fits their needs. Product details and service information should be checked before making a purchase.</p>"""
write("about/index.html", page("About Websitewire","Learn about Websitewire and its practical guides, tools and web services.",about_body,"/about/"))

privacy_body = """<h1>Privacy Policy</h1><p>This starter policy must be reviewed and adapted to the services and analytics you actually use.</p><h2>Information you provide</h2><p>If you contact us by email or through a form added later, the information you send may be used to respond to your request.</p><h2>Cookies and advertising</h2><p>Third-party services such as advertising providers may use cookies or similar technologies according to their own policies and your applicable choices.</p><h2>External links</h2><p>Our pages may link to third-party websites. Their privacy practices are governed by their own policies.</p><h2>Contact</h2><p>Replace this section with your real business contact details and obtain appropriate legal review before relying on this policy.</p>"""
write("privacy-policy/index.html", page("Privacy Policy | Websitewire","Read Websitewire's privacy information and third-party link disclosures.",privacy_body,"/privacy-policy/"))

disclosure_body = """<h1>Affiliate Disclosure</h1><p>Some Websitewire articles may contain affiliate links. If you click a qualifying link and make a purchase, we may receive a commission at no additional cost to you.</p><p>Affiliate relationships should not replace honest explanations, accurate product details or consideration of alternatives. Prices, availability and product specifications may change, so verify them with the seller before buying.</p><p>We will identify affiliate links or relevant commercial relationships clearly near the recommendations.</p>"""
write("disclaimer/index.html", page("Affiliate Disclosure | Websitewire","Learn how Websitewire may earn commissions through qualifying affiliate links.",disclosure_body,"/disclaimer/"))

terms_body = """<h1>Terms of Use</h1><p>Websitewire content is provided for general informational purposes. We aim to be helpful, but cannot guarantee that every detail remains current or fits every situation.</p><p>Verify important product specifications, pricing, provider terms and technical instructions before acting. Third-party websites and services are outside our control.</p><p>Use this site lawfully and do not attempt to disrupt its operation. Add reviewed business-specific terms before offering paid services or collecting customer data.</p>"""
write("terms/index.html", page("Terms of Use | Websitewire","Read the basic terms for using Websitewire resources.",terms_body,"/terms/"))

search_body = """
<h1>Search Websitewire</h1><p>Search our current article titles and descriptions.</p>
<form id="search-form" class="search"><input id="search-query" placeholder="Enter a topic..." required><button>Search</button></form>
<div id="search-results"></div>
<script>
const pages=__DATA__;
const form=document.getElementById('search-form');
form.addEventListener('submit',e=>{e.preventDefault();const q=document.getElementById('search-query').value.toLowerCase().trim();const hits=pages.filter(p=>(p.title+' '+p.desc+' '+p.category).toLowerCase().includes(q));const el=document.getElementById('search-results');el.innerHTML=hits.length?hits.map(p=>'<div class="card"><h3><a href="'+p.url+'">'+p.title+'</a></h3><p>'+p.desc+'</p></div>').join(''):'<p>No matching pages found. Try another phrase.</p>';});
</script>
"""
search_data = [{"title":a["title"],"desc":a["desc"],"category":a["category"],"url":"/articles/"+a["slug"]+".html"} for a in articles]
search_body = search_body.replace("__DATA__", json.dumps(search_data).replace("</","<\\/"))
write("search.html", page("Search Websitewire","Search Websitewire articles and guides.",search_body,"/search.html"))

# Static sitemap includes every generated page.
urls = ["/", "/articles/", "/buying-guides/", "/tools/", "/services/", "/contact/",
        "/about/", "/privacy-policy/", "/disclaimer/", "/terms/", "/search.html"]
urls += ["/articles/"+a["slug"]+".html" for a in articles]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
for url in urls:
    sitemap += f'  <url><loc>https://websitewire.co.in{url}</loc></url>\\n'
sitemap += '</urlset>\\n'
write("sitemap.xml", sitemap)
write("robots.txt", "User-agent: *\\nAllow: /\\nSitemap: https://websitewire.co.in/sitemap.xml\\n")

print("\\nWebsite pages created. Review contact email and policies before publishing.")
