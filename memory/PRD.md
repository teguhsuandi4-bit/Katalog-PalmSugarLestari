# PRD — Palm Sugar Lestari B2B Product Catalog

## Original Problem Statement
Build a premium, standalone B2B digital product catalog in ONE SINGLE HTML FILE (index.html) for PALM SUGAR LESTARI — premium palm sugar products for international buyers, importers, distributors, wholesalers, retailers, food manufacturers, restaurants, cafes, and trading companies. Not a website/store: no backend, database, cart, checkout, login, or CMS. Must be print-to-PDF friendly (A4), mobile responsive, with editable config block, image placeholders, WhatsApp CTA, gallery with lightbox/zoom, floating minimal navigation, and strict data accuracy (no invented MOQ, certifications, origin, contact info — use "Available upon request" / "To be confirmed").

## User Personas
- International buyer / importer evaluating palm sugar supply
- Distributor / wholesaler / retailer checking product range and prices
- Food manufacturer, restaurant, cafe sourcing palm sugar
- Brand owner editing config (images, WhatsApp number, contact info)

## Core Requirements (static)
- Single-file index.html (HTML5 + CSS3 + vanilla JS), zero dependencies beyond Google Fonts CDN
- Exact 4 products: Organic Powdered 1kg USD 3.50; Powdered 100 pcs USD 2.00; Organic Liquid 350ml USD 1.80; Organic Liquid 200ml USD 1.50
- Sections: Cover, About, Collection, 4 Product Details, Comparison, Applications, Why Choose, B2B Info, CTA, Contact, Back Cover
- Palette: #4A2C20 #A66A3F #C6A15B #FAF7F1 #F1E9DD #292522 #746B63; Playfair Display + Inter
- catalogConfig / productImages / products JS config at top of script
- WhatsApp button with editable number + prefilled message
- @media print A4 brochure mode
- Gallery: 4 slots per product, thumbnails, zoom, lightbox

## Architecture
- /app/index.html — canonical deliverable (standalone, opens directly in browser)
- /app/frontend/public/palm-sugar-catalog.html — preview copy served by the dev server
- No backend, no database (by requirement)

## Implemented (2026-07)
- Full single-file catalog with all 11 sections, all rendered from JS config
- v2 redesign "The Tropical Export Journal": kinetic hero with masked line-by-line reveal,
  parallax + mouse-tilt spotlight cover frame, editorial slow marquee, numbered manifesto
  chapter headers (outlined serif numerals), LESTARI watermark in dark Why chapter,
  Lenis momentum scrolling (CDN, graceful fallback), upgraded reveals/micro-interactions
- Product cards, detail sections with spec tables, comparison table, applications, why-choose, B2B cards
- Gallery with 4 slots per product, thumbnail switching, cursor-follow zoom, lightbox (keyboard: Esc/arrows)
- Floating pill navigation with scroll-spy; WhatsApp float + CTAs (wa.me link when number configured)
- Print CSS: A4 pages, hidden nav/floats, break control, color preservation
- Mobile responsive layouts (stacked, compact nav, icon-only WA button)
- Elegant labeled image placeholders (no fake stock/product photos); contact placeholders [ADD ...]

## Pending User Input
- User said they will upload actual packaging photos — first upload attempt did NOT arrive
  (get_assets returned none). Photo slots remain placeholders until photos are re-attached.

## Verified
- Desktop: cover, nav, all 4 products/prices, detail, lightbox open/close, comparison, contact, back cover
- Mobile 390px: cover, detail gallery, table, back cover
- Text checks: all product names, USD prices, "100 pcs", "Available upon request", "To be confirmed"

## Backlog
- P0: User to add real product photos (productImages), WhatsApp number, email, address in catalogConfig
- P1: Optional extra gallery images per product (product1_2, product1_3, product1_4 keys)
- P1: Print → Save as PDF final review by owner after real images added
- P2: Trade terms (MOQ, lead time, Incoterms) once provided by owner
