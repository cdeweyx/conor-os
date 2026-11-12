---
name: design-sources
description: >
  The shared list of design resources (galleries, fonts, icons, component
  libraries, backgrounds, color tools, craft writing) with what each is good
  for and a taste verdict. Use when a reference pass, research lane, or
  build step needs a source, or when the user asks "where can I find", "best
  sites for inspiration", "font sites", "component libraries",
  "backgrounds", "what did I miss", or shares design resources to fold in.
  Do NOT use to turn a reference into technique (visual-assets,
  motion-design), for one shared example (explain-interface), a build
  library (tech-planning), or image models and icon licenses
  (visual-assets).
---

# Design sources

One list, so hifi-design, visual-assets, motion-design, landing-page, and design-shaping all pull from the same place instead of each keeping a copy that drifts. Organized by the job a source does. The method (lane plans, capture, annotating by technique) stays with the skill that runs it: visual-assets' and motion-design's `references/inspiration.md`.

Facts rot: check a link before relying on its price, plan, or access, and when a source dies or renames, fix it here the same day. When the user shares new resources, check each one live, add it under its job with a one-line verdict, and say which ones you left out and why. A specific site, screen, or effect shared as an example rather than a source goes to explain-interface.

How to use it:
- Mobbin over its MCP is the first stop when it's connected (`search_sections` for marketing and front-door pieces, `search_screens` by job, `search_flows` by competitor); install line in hifi-design's `references/brief-and-review.md`. The galleries below fill gaps and run through Playwright.
- The build gets technique text, never the images. A source is for stealing the thinking.
- Templates and component marketplaces are never a direction; their look is the template look. Borrow a piece only from the libraries not on the blocklist under Components.
- Several galleries refuse plain fetchers (403); the Access column says when Playwright needs a real user agent.

## Inspiration, by job

### Whole pages and heroes

| Source | For | Access |
|---|---|---|
| recent.design (was Godly) | High-end heroes and backdrops; tags for Motion, 3D, Illustration, Typography. The best single source for treatments. | Public |
| Land-book, Lapa Ninja, Landdding, One Page Love | Landing pages in volume; Landdding is community-upvoted daily picks. | Land-book and Lapa 403 to curl; browser |
| Saaspo | SaaS pages by type, sections tagged Dashboard, Graph, Dark Mode. | 403 to plain fetchers; Playwright with a real UA |
| SEESAW | Full sites tagged by industry (fintech, developer tools, productivity), for register. | Public |
| Siteinspire | Restrained, typographic, editorial sites. | Rate-limits bots; Playwright with delays |
| Inspora | A curated archive of recent visual and creative work; treatment ideas, not product context. | Public |
| Awwwards | Agency-grade sites and WebGL; read for technique, discount for register. | Public |
| Browse.cool, Hoverstat.es | Agency craft; anti-references for a working screen. | Public |

### Brand and identity

| Source | For | Access |
|---|---|---|
| Inspora | Recent identity and visual work; the first stop for brand-design's reference pass (marks, type in use, color systems, brand boards). The user's pick. | Public |
| Land-book, Landdding | Brand applied to a page: how an identity carries into type, color, and layout. Both listed above too. | Land-book 403s to curl; browser |
| Fonts In Use | Type in real identities, searchable by face. | Public |
| posts.design | Real launch and social posts, X headers, and OG images from a thousand-plus brands: an identity carried into launch assets. | Free browse; Pro tier |

### Sections by job

| Source | For | Access |
|---|---|---|
| Sections.wtf | Shipped sections filtered by job (Statistics, Comparison, Tabs, Pricing, Menu, Footer). The one to open per surface. | Public; Framer-hosted, Playwright fine |
| Unsection | Real-site sections by job (Hero, Feature, Pricing, CTA, Navbar, Footer); second source when Sections.wtf runs thin. | Free browse; account for more |
| Navbar Gallery | Website navs by type (Static, Dropdown, Mega Menu, Side Bar, Announcement, Full Screen). Use it for pattern names, not state details. | Public |
| Footer (footer.design) | Footers sorted by type and style (Typographic, Large Type, Grid, Animated, Illustrative). Mostly studios and portfolios, so read for the idea and discount for register. | Public |
| 404s | Error pages; how an empty or error state earns its space. | Public |
| Details.so | Production hero sections, footers, preloaders, transitions; the free tier shows under 1%. | Pro $9/mo |

### Product UI and flows

| Source | For | Access |
|---|---|---|
| Mobbin and its MCP | Shipped mobile and web screens, flows, and sections. | Login; Pro for MCP, OAuth, 60 calls a minute |
| Refero and its MCP | Web SaaS screens by pattern; the MCP's style search is the closest thing to "search by taste". | Free browse limited; MCP paid |
| Refero Styles (styles.refero.design) | 2,000-plus real sites written up as DESIGN.md: palette with each color's role, type, spacing, components. The fastest read of what makes a named product look like itself. Trait candidates only; the file never reaches the build. | Free, server-rendered, curl reads it |
| SaaSFrame | Dashboards, settings, marketing pages by category. | Public browse |
| Page Flows | Recorded real-product flows, motion in context. | Paid |
| Dark Mode Design | Dark sites only: how layers separate without shadows, how an accent holds on near-black. | Public |
| Appllama | Top-grossing iOS apps screen by screen, in journey order, each with revenue, downloads, and ratings. Covers indie apps Mobbin misses (Opal, Airbnb weren't in a Mobbin search). Free pages only; its MCP needs a paid plan. | Free browse; public boards and app pages read without login |

### Well-designed phone apps

Jaimin's [High Taste Apps](https://appllama.io/u/jaimin/high-taste-apps) board, which the user vouched for. Inspiration, not a checklist: when a phone-first product needs a feel to aim at, browse the ones nearest its category on Appllama's free pages or Mobbin, and read any that spark something through explain-interface. A brand-design reference pass can pull from it too.

- **Focus and screen time:** Opal, Blank Spaces Launcher, Unrot, Focus Friend, Cat On Chair.
- **Wellbeing and habits:** Endel, Lungy, Finch, Catzy, stoic., How We Feel, MyDooors, grug, Her 75, Amble, GO Club.
- **Astrology and journaling:** CHANI, Co–Star, daplit.
- **Learning and reference:** Duolingo, Bunpo, LookUp.
- **Social, photos, and camera:** Retro, Dispo, corner, Timeleft, Hinge, Pool, Picnic, Dudel Draw.
- **AI and audio:** Wabi, Character AI, Capy, Suno, ElevenLabs.
- **Money and crypto:** Wise, MoonPay, Jupiter, Phantom.
- **Travel and food:** Airbnb, Crouton.

### Motion and interaction

| Source | For | Access |
|---|---|---|
| 60fps.design | Product-motion clips with filters (Chart, Counter, Ticker, Progress, Stagger, Reveal). Mobile-heavy; read for choreography. | Free browse; Pro $15/mo; MCP separate |
| movin.design | Motion clips from X, daily; the fastest read on what practitioners ship now. | Public |
| uilabs.dev (Mariana Castilho) | Product-register micro-interactions as live React, so Playwright records them. | Public |
| detail.design | Small product decisions; clips are plain mp4, so curl fetches them. | Public |
| interior.dev | Micro-feedback recipes (segmented control, slider detents, loading button, hold to confirm), React and Motion. | Public, MIT |
| transitions.dev (Jakub Antalik) | The core product transitions (modal, toast, tooltip, accordion, tab slide) as copy-paste code at the Linear tier, plus a scanner that scores a codebase's motion. | Core free, MIT; Pro adds a skill and an MCP |
| Kinetics (Colorion) | 160-plus micro-interaction recipes in CSS and React (hold to confirm, tab pill glide); skip the liquid-glass and particle ones. | Free; license unstated, so technique only |
| save.design | Sites filtered by animation library and framework, so a reference already runs on our stack. | Public browse |
| Codrops roundups | Monthly interaction and animation demos with source. | Public |
| motionin.design | Physics-based, cursor-responsive sections sold as prompts. A vocabulary of ambitious moments, not a default. | Public browse |
| Devouring Details (Rauno) | The Line Graph and Radial Timeline prototypes with source; the choreography chapter. | Paid, $249 |
| Apple WWDC23 "Animate with springs"; Stripe gradient breakdowns (bram.us, Kevin Hufnagl) | The spring model; how an ambient shader hero actually works. | Public |
| Rive showcase, LottieFiles customers | State-machine and icon-scale motion; choreography, usually the wrong register. | Public |

Consumer-register motion, read only as anti-references: landing.love, Design Spells, Motionimo.

### Type, data viz, tokens

| Source | For | Access |
|---|---|---|
| Typewolf, Fonts In Use | Type in the wild, indexed by typeface; pairings that shipped. | Public |
| Information is Beautiful Awards, Datawrapper blog, Observable, The Pudding | Data-viz craft, color, and the technique in code. | Public |
| DESIGN.md galleries and Fudge | Tokens pre-extracted from real sites; Fudge turns a live site into tokens. A shortcut, not inspiration. | Public; Fudge is an MCP |

### Personal curation

Are.na (public channels, API without auth), Cosmos, Savee, Pinterest (login walls; texture and material at most), Dribbble and Behance (treatment ideas only; they reward what photographs well over what works).

Gone or renamed: Godly is recent.design, Screenlane is Page Flows (paid), scrnshts.club is App Store shots only, arc.net is a farewell page. Sombra is a gradient composer, not a gallery.

## Materials, by job

### Fonts

| Source | For | Notes |
|---|---|---|
| Fontshare | Free fonts from Indian Type Foundry (Satoshi, General Sans, Cabinet Grotesk, Clash). | Free for commercial use; renders by JS, so browse in a browser |
| Pangram Pangram | Contemporary grotesks and displays. | Free to try, paid license for commercial use |
| uncut.wtf, Velvetyne, Collletttivo | Experimental and open display faces for a statement moment, never the UI family. | Mostly OFL; credit the designer |
| Google Fonts | Inter, Inter Tight, Geist, Instrument Serif, and the open staples. | OFL; self-host as woff2 |

Inter and Geist are fine tuned (tracking per step, variable weights, stylistic sets) and generic at defaults; see landing-page's `references/craft.md`.

### Icons

Lucide, Tabler, Hugeicons, Phosphor, Iconoir, all searchable together through Icônes (icones.js.org) or the Iconify API. Stroke sets re-weight; baked-outline sets don't. visual-assets' `references/sourcing.md` has the license tiers and the re-weighting formula.

### Components

The build's picks (Base UI, cmdk, Sonner, Motion, NumberFlow) live in tech-planning's `references/libraries.md`, and a picked library sits behind the product's own `ui/` layer. These are for borrowing an idea or one piece of code. Before borrowing code, check its agent access: the license, a shadcn registry (`npx shadcn add @<lib>/<item>`), an MCP. An MIT library on a registry can be installed piece by piece; anything else is borrowed as an idea.

| Source | Verdict |
|---|---|
| motion-primitives | Reads at the Linear tier: In View, Text Effect per line, Sliding Number, Progressive Blur. The first place to look. |
| animate-ui | Animated drop-in primitives for Radix, Base UI, and React Aria. Useful when a primitive needs motion. |
| beui.dev | MIT, Motion-based, expressive (springs, morphs, glass). Fine for product UI, loud for a landing page. |
| 21st.dev, Skiper UI, Cult UI, Kokonut UI | Community and shadcn-CLI component drops (21st.dev has 12,000-plus and an MCP; Kokonut is MIT, on a registry as `@kokonutui`, MCP through `shadcn mcp init`). Wide and uneven; judge each piece. |
| Magic UI, React Bits, Aceternity, Animata, Eldora UI, Spectrum UI, Evil Charts | The cliché catalog (meteors, border beams, spotlight cards, globes, word rotators, glowing gradient charts). Read their names as a blocklist; most are MIT and popular, which is why they keep showing up in lists. |
| v0 templates, Webflow template shops (Wedoflow), Scrolltide | The template look itself; anti-references. |

### Backgrounds, shaders, generative

| Source | For | Notes |
|---|---|---|
| Paper Shaders (shaders.paper.design) | Mesh and grain gradients, dot grids, god rays as React components or GLSL. The default ambient layer. | Apache 2.0, about 1 KB core |
| Scroll Shaders (scrollshaders.com) | 117 seamless-loop WebGL shaders in 11 shelves (liquid metal, fluted glass, dither, halftone, ASCII), each one fragment shader in one file. Browse it for treatment ideas when Paper Shaders' set runs out. | Browsing free; code $29/mo or $239 lifetime, commercial use |
| fffuel, nnnoise | SVG generators for gradients, grain, patterns, textures. | Free, commercial use |
| Haikei | SVG blobs, waves, layered shapes. | Free tier |
| Unicorn Studio | Shader and 3D scenes in a visual editor, embedded. | 37 KB embed; free tier non-commercial |
| backgrounds.supply | 1,100-plus gradient images. | $49 one-time, commercial use, no redistribution; only if a shader can't do it |

### Color

Realtime Colors (a palette and fonts on a live sample site), oklch.com (pick and convert in OKLCH), UI Colors (shade ramps from one hex), Huemint (generated palettes). Ramps for a product come from hifi-design's `references/color-ramps.md`.

### Logos, mockups, image tools

| Source | For | Notes |
|---|---|---|
| svgl | About 680 brand logos, light and dark, free API (`https://api.svgl.app?search=<name>`). | No usage terms; check each brand's |
| remove.bg | Background removal by API. | 50 free calls a month, up to 10 MP |
| Lummi | AI stock photos, illustrations, 3D. | Read the license before use |
| shots.so | Device and browser mockups. | No API, 1x export; human use only |
| Stageshow (github.com/benjitaylor/skills) | Faux product UI for marketing (app windows, feature cards, bento grids, cursor demos) in React, with scripts that film the result. | MIT skill; read it before installing |
| Openverse, Wikimedia Commons, Art Institute of Chicago, the Met | Real pictures with the license attached: places, old maps, materials, museum objects. | Commercial-use licenses only, credit in the footer; rules in visual-assets' sourcing |

Image models, illustration sets, and their licenses: visual-assets' `references/sourcing.md`.

### Launch and video

HyperFrames (HTML and GSAP, deterministic frames, `lint`, `check`, and `snapshot`; Apache 2.0, eight agent skills) is the default for a launch video, since our HTML and tokens carry straight in. Remotion (React; source-available, free for individuals and companies up to three people) when the product is React or captions and 3D dominate. One engine per project.

### Builders

iter0 (checks competitors, shows three designs, builds one) and Lovable or Bolt are tools that produce a page, not sources. Read one as a competitor test for the landing-page skill, never as a reference.

## Craft writing and people

| Source | For |
|---|---|
| emilkowal.ski, animations.dev, ui.land | The motion rules ("Great animations", "You don't need animations", "Agents with taste") and interviews. |
| raunofreiberg/interfaces, "Invisible details" | The canonical checklist of interface details. |
| interfaces.dev | The polish principles better-ui is vendored from. |
| Vercel design guidelines | Motion and visual rules as bullets; the audit list. |
| Linear Craft posts | Calm motion and the redesign process; "don't compete for attention you haven't earned". |
| Interface Lineage (interfacelineage.com) | Principles and pattern references: 123 principles and 500-plus dated interface teardowns, each citable by slug. Free to read, `.md` on any URL; the MCP is paid. |
| ui-skills.com | A curated directory of design skills and design-system indexes; look here before writing a skill from scratch. |

People whose work is worth studying: Emil Kowalski, Rauno Freiberg, Paco Coursey, Jhey Tompkins, Jakub Krehel, Mariana Castilho, Maxime Heckel, Gavin Nelson, Josh Puckett, Raphael Salaja, Benji Taylor. Verify handles before citing.
