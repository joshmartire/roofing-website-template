# -*- coding: utf-8 -*-
# Roofing services. Each entry becomes a service page (500-600 words of main content together with its
# COSTS entry and FAQs) plus one page per city in content_cities.py.
#
# Tokens: {biz} = business name, {phone} = phone number, [[slug|anchor text]] = link to another service
# (or [[contact|...]], [[estimate|...]], [[area:windsor|...]]). Links to services the client does not
# offer become plain text and are listed in _build/removed-service-mentions.txt for rewording.
#
# "cities" holds one short paragraph per city slug. It must be genuinely about that town, not a
# find-and-replace of the city name.

SERVICES = [
# ------------------------------------------------------------------ ROOF SYSTEMS
{
"slug": "roof-replacement",
"name": "Roof Replacement",
"cat": "systems",
"icon": "roof",
"short": "Full tear-off and a complete new asphalt shingle roof system, from the deck up to the ridge cap.",
"title": "Roof Replacement & Asphalt Shingle Reroofing",
"desc": "Full asphalt shingle roof replacement: tear-off, deck repairs, ice and water protection, underlayment, ventilation and new shingles. Written quotes.",
"h1": "Roof Replacement",
"lead": "A new roof is more than new shingles. We strip it to the deck and rebuild the whole system, so every layer underneath is done right.",
"body": """
<p>Curling or cracked shingles, bald patches where the granules have washed off, daylight in the attic or a stain spreading across a ceiling: these are the signs most homeowners notice first. When a roof reaches that point, patching usually just buys time. {biz} replaces asphalt shingle roofs on homes across the region, and we walk you through what we found before we price anything.</p>
<h2>What a full replacement includes</h2>
<ul>
<li><strong>Complete tear-off</strong> — every existing layer comes off, down to the roof deck, with the debris loaded straight into a bin.</li>
<li><strong>Deck inspection and repair</strong> — soft, rotted or delaminated sheathing is cut out and replaced so the new roof is fastened to something solid.</li>
<li><strong>Eave and valley protection</strong> — self-adhering ice and water membrane along the eaves and in the valleys, where ice dams and heavy runoff do the most damage.</li>
<li><strong>Underlayment and drip edge</strong> — synthetic underlayment across the rest of the deck and metal drip edge on the eaves and rakes.</li>
<li><strong>Shingles and flashing</strong> — architectural shingles installed to the manufacturer's nailing pattern, with new step, chimney and pipe flashing.</li>
<li><strong>Ventilation</strong> — balanced intake and exhaust, usually soffit intake with a ridge vent, checked on every job (see [[roof-ventilation|roof ventilation]]).</li>
</ul>
<h2>How the job runs</h2>
<ol>
<li><strong>Inspection.</strong> We check the shingles, flashing, ventilation and, where we can get in, the attic for moisture or frost.</li>
<li><strong>Written quote.</strong> Materials, ventilation plan and a per-sheet price for any decking that needs replacing are listed up front.</li>
<li><strong>Install day.</strong> Landscaping and siding are protected, the old roof comes off and the new system goes on in sections so the house is never left open.</li>
<li><strong>Cleanup.</strong> Magnetic sweeps for nails across the lawn, driveway and beds, then a final walk-around with you.</li>
</ol>
<p>Not sure your roof is finished? Start with a [[roof-inspections|roof inspection]], or get a ballpark number in a minute with our [[estimate|instant roof estimate]].</p>
""",
"faqs": [
("How long does a roof replacement take?", "Most homes are done in one to three days. Size, steepness, the number of layers coming off and the weather all affect the schedule."),
("Can you shingle over my old roof?", "Sometimes it's allowed, but we recommend a full tear-off. It's the only way to inspect and repair the deck and install the new roof the way the shingle manufacturer specifies."),
("Do I need to be home?", "Not for the whole job. We'll confirm access, parking for the bin and anything near the house you'd like moved before we start."),
],
"related": ["roof-inspections", "roof-ventilation", "eavestroughs"],
"cities": {
"windsor": "In older Windsor neighbourhoods, a tear-off often turns up two or even three layers of shingles and original plank decking with gaps between the boards. We budget for that possibility in the quote, re-sheet where the boards can't hold a nail properly, and replace the tired chimney flashing that's common on houses of that age.",
"lasalle": "A lot of LaSalle homes from the 1990s and 2000s are still on their first set of shingles, and many of those roofs are wearing out within a few years of each other. Replacement is usually straightforward on these houses, but we look closely at bathroom fans vented into the attic and at builder-grade ventilation before we reroof.",
"tecumseh": "Tecumseh homes closer to Lake St. Clair can take stronger gusts off the water than inland streets. On those roofs we pay extra attention to starter strips at the edges, the nailing pattern and the ridge cap, because those are the spots where wind lifts shingles first."
},
},
{
"slug": "metal-roofing",
"name": "Metal Roofing",
"cat": "systems",
"icon": "metal",
"short": "Standing seam and steel roofing systems for homeowners who want a long-lasting, low-maintenance roof.",
"title": "Metal Roofing: Standing Seam & Steel Roofs",
"desc": "Standing seam and steel metal roofing for homes: panel options, colours, underlayment, flashing and snow guards. Get a written metal roofing quote.",
"h1": "Metal Roofing",
"lead": "Metal costs more on day one and asks very little after that. We install standing seam and steel roofing systems detailed for real Ontario winters.",
"body": """
<p>Metal roofing has moved well beyond barns and cottages. Homeowners choose it because a well-installed metal roof can outlast several asphalt roofs, sheds snow and rain quickly and comes in finishes that suit modern and traditional houses alike. {biz} installs metal roofing on homes and garages, and we'll give you an honest comparison with shingles before you decide.</p>
<h2>Metal roofing options</h2>
<ul>
<li><strong>Standing seam</strong> — vertical panels joined with raised seams and concealed fasteners, so there are no exposed screws to maintain.</li>
<li><strong>Exposed-fastener steel panels</strong> — a more economical ribbed panel, well suited to garages, outbuildings and some homes.</li>
<li><strong>Metal shingles and shakes</strong> — pressed steel that resembles slate, shake or tile while keeping the benefits of metal.</li>
<li><strong>Accent roofs</strong> — porches, bay windows and dormers in metal, paired with a shingled main roof.</li>
<li><strong>Snow guards and trim</strong> — snow retention above doors and walkways, plus matching ridge, rake and eave trim.</li>
</ul>
<h2>What we pay attention to</h2>
<ol>
<li><strong>The deck and underlayment.</strong> We tear off to the deck in most cases and install a high-temperature underlayment rated for metal.</li>
<li><strong>Expansion and movement.</strong> Panels move with temperature, so clips and fasteners are installed to let them expand without buckling.</li>
<li><strong>Flashing details.</strong> Chimneys, skylights, walls and pipes get flashing made for metal roofing, not leftovers adapted from a shingle job.</li>
<li><strong>Snow and ice.</strong> We plan where sliding snow will land and add guards where it would hit a door, deck or walkway.</li>
</ol>
<p>Metal is quieter than most people expect when it's installed over a solid deck with underlayment. If you're weighing it against shingles, our [[roof-replacement|roof replacement]] page explains the asphalt option, and our [[estimate|instant estimate]] gives a shingle baseline to compare.</p>
<h2>Good to know</h2>
<p>Metal roofs are heavier on the budget at the start, so it helps to think about how long you plan to stay in the house. If you expect to move within a few years, a quality shingle roof may make more sense. If this is your long-term home, metal's lifespan and low upkeep can make the difference worthwhile. Colour also matters more than people expect: lighter finishes reflect more summer heat, while darker ones show less dirt. We'll bring physical samples so you can see them against your brick or siding in daylight.</p>
""",
"faqs": [
("Is metal roofing noisy in the rain?", "Over a solid deck with underlayment and an insulated attic, most people find it no louder than shingles. The noisy metal roofs people remember are usually on open-framed barns."),
("Does a metal roof attract lightning?", "No. Metal doesn't make a strike more likely. If lightning does hit, a metal roof won't burn, which is one reason insurers generally view it well."),
("Can metal go over my existing shingles?", "Some systems allow it, but we usually recommend a tear-off so the deck can be inspected and the roof sits flat."),
],
"related": ["roof-replacement", "snow-ice", "skylights"],
"cities": {
"windsor": "Windsor's mix of hot summers and freeze-thaw winters is where metal's expansion details matter most. On older Windsor houses with dormers and porch roofs, we also plan the transitions between metal and any shingled sections carefully, since that's where leaks usually start.",
"lasalle": "In LaSalle, we often install metal on newer homes where the owners plan to stay for decades and don't want to reroof again. Some subdivisions have design guidelines or covenants on roof colour and material, so check yours before you choose a panel colour.",
"tecumseh": "For homes near the Lake St. Clair shore in Tecumseh, standing seam's concealed fasteners and interlocking seams handle wind well. We still match the clip spacing and edge details to the exposure of your lot rather than using one standard for every house."
},
},
{
"slug": "flat-roofing",
"name": "Flat Roofing",
"cat": "systems",
"icon": "flat",
"short": "Low-slope roof replacement and repair with EPDM, TPO and modified bitumen membranes.",
"title": "Flat Roofing: EPDM, TPO & Modified Bitumen",
"desc": "Flat and low-slope roofing for homes, additions, garages and porches: EPDM, TPO and modified bitumen, drainage and repairs. Written flat roof quotes.",
"h1": "Flat Roofing",
"lead": "Flat roofs fail when water has nowhere to go. We replace and repair low-slope roofs with proper membranes, seams and drainage.",
"body": """
<p>Flat and low-slope roofs are common on additions, garages, porches, row houses and the back sections of older homes. Shingles can't be used on them because water drains too slowly, so they need a continuous membrane instead. {biz} installs and repairs low-slope roofing systems and pays as much attention to drainage as to the membrane itself.</p>
<h2>Low-slope roofing systems</h2>
<ul>
<li><strong>EPDM rubber</strong> — a single-ply rubber membrane with very few seams, widely used on residential flat roofs.</li>
<li><strong>TPO</strong> — a heat-welded single-ply membrane with a light-coloured surface that reflects summer heat.</li>
<li><strong>Modified bitumen</strong> — multi-layer torch-free or self-adhered rolls with a tough granulated cap sheet.</li>
<li><strong>Tapered insulation</strong> — sloped insulation boards that move water toward drains and scuppers instead of letting it pond.</li>
<li><strong>Flat roof repairs</strong> — seam repairs, blister and puncture patches, and new flashing at walls, curbs and drains.</li>
</ul>
<h2>How we approach a flat roof</h2>
<ol>
<li><strong>Find where the water goes.</strong> We look for ponding, staining and soft spots and check every drain, scupper and eavestrough outlet.</li>
<li><strong>Choose the membrane.</strong> The right system depends on the structure, foot traffic, what's on the roof and your budget.</li>
<li><strong>Fix the deck and slope.</strong> Wet insulation and damaged decking are replaced, and tapered boards are added where ponding is a problem.</li>
<li><strong>Detail the edges.</strong> Walls, curbs and edges get proper flashing and termination bars, since that's where flat roofs usually leak.</li>
</ol>
<p>Where a flat section meets a sloped roof, we tie the two together so the transition stays watertight. For larger buildings, see [[commercial-roofing|commercial roofing]].</p>
<h2>Good to know</h2>
<p>Low-slope roofs reward regular attention. Clearing leaves from drains and scuppers each fall, checking seams after big storms and keeping foot traffic to a minimum all help a membrane last. If a flat roof sits under a deck, planters or air-conditioning equipment, those need to be lifted or protected during replacement, so let us know what's up there before we quote. And if water has been getting in for a while, expect some wet insulation or decking to be replaced; we'll show you what we find before we replace it.</p>
""",
"faqs": [
("Is a little ponding on a flat roof normal?", "Water that's gone within about two days after rain is usually acceptable. Water that sits longer speeds up wear and should be corrected with better drainage or tapered insulation."),
("Which is better, EPDM or TPO?", "Both perform well when installed properly. EPDM has a long track record and few seams, while TPO reflects more heat. We'll recommend one based on your roof."),
("Can I walk on a flat roof?", "Occasional careful foot traffic is fine on most membranes. If you plan to use the roof as a deck, it needs a system and walkway built for that."),
],
"related": ["commercial-roofing", "roof-repair", "eavestroughs"],
"cities": {
"windsor": "Windsor has plenty of flat and low-slope roofs on the back additions of older homes, on corner storefronts with apartments above, and over porches. Many were built with minimal slope and patched many times, so we often find several old layers to remove before the new membrane goes down.",
"lasalle": "In LaSalle, low-slope roofing is most common over attached garages with rooms above, sunrooms and porch roofs on newer homes. The tricky part is usually where the flat section meets siding or a sloped roof, and that's where we focus our flashing work.",
"tecumseh": "Tecumseh has a good number of low-slope roofs on garages, commercial plazas and mid-century homes. Heavy summer storms test their drains and scuppers, so we clear and check every outlet as part of the job."
},
},
{
"slug": "new-construction-roofing",
"name": "New Construction Roofing",
"cat": "systems",
"icon": "build",
"short": "Roofing for new homes, additions and garages, coordinated with builders and framers from sheathing to ridge.",
"title": "New Construction Roofing for Homes & Additions",
"desc": "Roofing for new homes, additions and garages: sheathing coordination, underlayment, ice and water protection, shingles or metal and inspections.",
"h1": "New Construction Roofing",
"lead": "On a new build, the roof is what closes the house in. We work to the builder's schedule and get it weathertight fast and done right.",
"body": """
<p>Whether you're a homeowner building custom, a builder with several houses on the go or adding a garage or addition, the roof is a critical stage. Once it's on, interior trades can get to work without worrying about rain. {biz} roofs new construction to the drawings and the manufacturer's specifications and coordinates closely with the framing crew and general contractor.</p>
<h2>What we handle on new builds</h2>
<ul>
<li><strong>Dry-in</strong> — underlayment, drip edge and ice and water protection installed quickly after the sheathing is on, so the house is protected early.</li>
<li><strong>Shingles or metal</strong> — architectural asphalt shingles or a metal roofing system, installed to specification for warranty coverage.</li>
<li><strong>Flashing and penetrations</strong> — step and counter flashing at walls, plus vents and plumbing stacks sealed as the trades install them.</li>
<li><strong>Ventilation</strong> — intake and exhaust sized to the attic, coordinated with the soffit installer and insulation contractor.</li>
<li><strong>Additions and tie-ins</strong> — new roofs joined into existing ones so the old and new sections shed water as one.</li>
</ul>
<h2>Working with builders</h2>
<ol>
<li><strong>Review the drawings.</strong> We confirm roof pitches, materials, valleys and ventilation before ordering.</li>
<li><strong>Schedule to the frame.</strong> We line up with the framer so sheathing doesn't sit exposed to the weather any longer than it has to.</li>
<li><strong>Install and inspect.</strong> We keep the site tidy, protect other trades' work and are ready for any building inspection that covers the roof.</li>
<li><strong>Hand off.</strong> You get the material and warranty details for your records.</li>
</ol>
<p>For an addition on an existing home, we'll often recommend replacing the old roof at the same time so both sections match and age together. See [[roof-replacement|roof replacement]] and [[soffit-fascia|soffit and fascia]].</p>
<h2>Good to know</h2>
<p>Small decisions on the drawings make a big difference to how a new roof performs. Simple roof lines with fewer valleys shed water and snow more easily and cost less to build. Placing plumbing vents and exhaust fans away from valleys avoids awkward flashing. Planning attic ventilation with the insulation contractor prevents the moisture problems that new, tightly built homes can develop. If you're still at the design stage, we're happy to review the roof plan with your designer before it's finalized.</p>
""",
"faqs": [
("Do you work directly for homeowners on new builds?", "Yes. We work for builders, general contractors and homeowners acting as their own general contractor, as long as the schedule and drawings are clear."),
("How soon after framing can you start?", "As soon as the roof sheathing is on and inspected, if an inspection is required. Getting the underlayment on quickly protects the framing and sheathing from rain."),
("Can the new roof match my existing house?", "We can usually match shingle style and colour closely, although new shingles will look cleaner than weathered ones for a while."),
],
"related": ["roof-replacement", "metal-roofing", "soffit-fascia"],
"cities": {
"windsor": "Windsor's new construction is a mix of infill homes on older lots and builds in newer subdivisions on the edges of the city. On infill lots, tight side yards and neighbouring houses make material deliveries and bin placement part of the planning, so we sort that out with the builder before roofing day.",
"lasalle": "LaSalle continues to see new subdivision homes and custom builds, often with complex roof lines, multiple valleys and large garages. Those details take more flashing and careful layout, and we plan them from the drawings before materials are ordered.",
"tecumseh": "New homes and additions in Tecumseh often sit on larger lots with more open exposure to wind. We follow the shingle manufacturer's high-wind nailing requirements where they apply and keep the site secure between stages."
},
},
{
"slug": "commercial-roofing",
"name": "Commercial Roofing",
"cat": "systems",
"icon": "commercial",
"short": "Roofing for small commercial buildings, plazas, offices and multi-unit properties, planned around your operations.",
"title": "Commercial Roofing for Small Buildings & Plazas",
"desc": "Commercial roofing for plazas, offices, shops and multi-unit buildings: membrane roofs, repairs, maintenance and replacements scheduled around tenants.",
"h1": "Commercial Roofing",
"lead": "A roof leak in a business costs more than the repair. We plan commercial roofing around your tenants, customers and hours.",
"body": """
<p>Small commercial buildings, retail plazas, offices, churches and multi-unit residential properties need roofers who understand both low-slope membranes and the reality of working on an occupied building. {biz} handles roofing for property owners and managers and keeps you informed at each stage.</p>
<h2>Commercial roofing services</h2>
<ul>
<li><strong>Membrane roof replacement</strong> — EPDM, TPO and modified bitumen systems with tapered insulation where drainage needs improving.</li>
<li><strong>Leak investigation and repair</strong> — tracing leaks back to failed seams, flashings, drains or rooftop equipment curbs.</li>
<li><strong>Sloped commercial roofs</strong> — shingle and metal roofing on mansards, storefront canopies and smaller pitched buildings.</li>
<li><strong>Roof maintenance</strong> — scheduled inspections, drain cleaning and minor repairs to extend the life of an existing roof.</li>
<li><strong>Condition reports</strong> — written reports with photos to help owners plan capital budgets, reserve funds or a sale.</li>
</ul>
<h2>How we run commercial projects</h2>
<ol>
<li><strong>Site review.</strong> We check the roof, access, rooftop equipment and any tenant or safety restrictions.</li>
<li><strong>Scope and schedule.</strong> You get a written scope, a schedule that works around your business and a plan for keeping the building watertight.</li>
<li><strong>Safety and protection.</strong> We set up fall protection, protect entrances and keep materials and debris contained.</li>
<li><strong>Closeout.</strong> Final photos, material details and any warranty information for your files.</li>
</ol>
<p>For low-slope systems on homes and garages, see [[flat-roofing|flat roofing]]. For storm-related leaks on a commercial property, see [[storm-damage-repair|storm damage repair]].</p>
<h2>Good to know</h2>
<p>For many commercial owners, the most cost-effective approach is a maintenance plan rather than waiting for a leak. Twice-yearly inspections, cleared drains and small seam repairs can extend a roof's life and help you plan a replacement years ahead instead of reacting to an emergency. When replacement is due, timing matters: planning around tenants' busy seasons, lease renewals and budgets keeps disruption low. We document each visit with photos, so you have a clear record for insurers, lenders, buyers or a condominium board, and a history of the roof that makes future decisions easier.</p>
""",
"faqs": [
("Can you work while my business stays open?", "Usually, yes. We plan noisy work and material lifts around your hours and keep entrances and walkways safe and clear."),
("Do you provide reports for property managers or insurers?", "Yes. We can provide a written condition report with photos describing what we found and what we recommend."),
("Do you install roofs on large industrial buildings?", "We focus on small and mid-sized commercial buildings. For very large industrial roofs, we'll tell you honestly if the project is outside what we take on."),
],
"related": ["flat-roofing", "roof-repair", "roof-inspections"],
"cities": {
"windsor": "Windsor has a large stock of older commercial buildings, from main-street storefronts with apartments above to plazas and light industrial units. Many have been re-covered more than once, so we confirm what's underneath before recommending a repair or full replacement.",
"lasalle": "In LaSalle, commercial roofing work is mostly on plazas, offices and service businesses along the main corridors, many of them built within the last few decades. Regular maintenance on these roofs is often the most economical way to delay a full replacement.",
"tecumseh": "Tecumseh's commercial properties range from Main Street storefronts to plazas and light industrial buildings. We schedule around business hours and keep customer entrances safe while work is going on overhead."
},
},
# ------------------------------------------------------------------ REPAIRS & INSPECTIONS
{
"slug": "roof-repair",
"name": "Roof Repair",
"cat": "repair",
"icon": "repair",
"short": "Leak investigation and lasting repairs to shingles, flashing, valleys, vents and chimneys.",
"title": "Roof Repair & Leak Repair",
"desc": "Roof leak repair: missing shingles, flashing, chimneys, valleys, vents and skylights. We find the source, show you photos and give a written price.",
"h1": "Roof Repair",
"lead": "Water travels before it drips. We trace a leak back to where it actually starts, fix it properly and show you photos of what we did.",
"body": """
<p>A ceiling stain rarely sits directly under the problem. Water can run along rafters and the top of the drywall for several feet before it shows up inside. That's why so many roof repairs don't hold: someone patched the wrong spot. {biz} starts every repair by finding the real source, and we'll tell you straight if a repair makes sense or if the roof is past it.</p>
<h2>Common roof repairs</h2>
<ul>
<li><strong>Missing or damaged shingles</strong> — replaced and sealed after wind, falling branches or age, matched as closely as possible.</li>
<li><strong>Flashing repairs</strong> — new step, counter and chimney flashing where old flashing has lifted, rusted or been sealed with caulking alone.</li>
<li><strong>Valley leaks</strong> — re-lining valleys with ice and water membrane where runoff concentrates and old materials have worn through.</li>
<li><strong>Vent and pipe boots</strong> — cracked rubber pipe boots and damaged roof vents replaced, one of the most common sources of small leaks.</li>
<li><strong>Ice dam damage</strong> — repairs at the eaves and a look at the attic insulation and ventilation that caused the dam (see [[roof-ventilation|roof ventilation]]).</li>
<li><strong>Skylight leaks</strong> — re-flashing the skylight, or replacing the unit when it has failed (see [[skylights|skylights]]).</li>
</ul>
<h2>How a repair visit works</h2>
<ol>
<li><strong>Tell us what you're seeing.</strong> Where the stain or drip is, when it happens and whether it's tied to heavy rain, wind or melting snow.</li>
<li><strong>Find the source.</strong> We inspect the roof and, where we can, the attic, then take photos of what we find.</li>
<li><strong>Repair or recommend.</strong> You get a written price for the repair, or an honest recommendation if the roof needs replacing.</li>
<li><strong>Confirm the fix.</strong> We show you before and after photos, and we'll come back if the same leak returns.</li>
</ol>
<p>If several areas are failing at once, a [[roof-replacement|roof replacement]] is often better value than a series of patches.</p>
""",
"faqs": [
("Can you repair just part of my roof?", "Yes, when the rest of the roof is in reasonable shape. If shingles are brittle or curling everywhere, a repair may cause more damage than it fixes, and we'll explain why."),
("Will repaired shingles match my roof?", "We match style and colour as closely as we can, but weathered shingles fade, so a patch may look slightly different for a while."),
("Is caulking a good way to fix a leak?", "Only as a short-term measure. Lasting repairs use properly lapped flashing and shingles, with sealant as a backup, not the main defence."),
],
"related": ["storm-damage-repair", "roof-inspections", "skylights"],
"cities": {
"windsor": "Many Windsor leaks we see come from chimneys on older homes, where flashing has been sealed over with tar or caulking several times instead of being replaced. Re-flashing properly, sometimes with a new cricket behind a wide chimney, is what finally stops them.",
"lasalle": "On LaSalle homes from the 1990s and 2000s, small leaks often trace back to cracked plumbing vent boots, lifted shingles on the ridge or valleys where two roof planes meet over a garage. These are usually quick, inexpensive fixes if they're caught early.",
"tecumseh": "In Tecumseh, wind is a frequent culprit: lifted tabs along the rakes and ridge, and shingles that have lost their seal. We check the surrounding area for loose shingles that haven't come off yet so you aren't calling us back after the next storm."
},
},
{
"slug": "storm-damage-repair",
"name": "Storm Damage Repair",
"cat": "repair",
"icon": "storm",
"short": "Wind, hail and fallen-tree damage inspected, documented with photos and made watertight.",
"title": "Storm Damage Roof Repair: Wind, Hail & Trees",
"desc": "Storm damage roof repair after wind, hail or fallen branches: inspection, photo documentation for your insurer, temporary protection and permanent repairs.",
"h1": "Storm Damage Repair",
"lead": "After a bad storm, the first job is keeping water out. The second is documenting the damage properly for you and your insurer.",
"body": """
<p>Thunderstorms, high winds and the occasional hailstorm can leave missing shingles, lifted ridge caps, dented vents or a branch through the roof. Some damage is obvious from the ground; some isn't visible until it leaks months later. {biz} inspects storm damage, protects the roof from further water and gives you the photos and written details you need if you decide to make an insurance claim.</p>
<!-- CLIENT REVIEW: confirm whether the client offers emergency or after-hours tarping and how quickly they can respond before adding any availability claims. -->
<h2>What we do after a storm</h2>
<ul>
<li><strong>Damage inspection</strong> — shingles, ridge caps, flashing, vents, skylights and eavestroughs checked for wind, hail and impact damage.</li>
<li><strong>Photo documentation</strong> — dated photos and a written description of the damage that you can share with your insurance adjuster.</li>
<li><strong>Temporary protection</strong> — tarping or temporary patches to keep water out until permanent repairs can be made.</li>
<li><strong>Permanent repairs</strong> — replacing damaged shingles, flashing and vents, or a full [[roof-replacement|roof replacement]] when the damage is widespread.</li>
<li><strong>Related exterior damage</strong> — bent or torn-off [[eavestroughs|eavestroughs]] and damaged [[soffit-fascia|soffit and fascia]].</li>
</ul>
<h2>What to do right after a storm</h2>
<ol>
<li><strong>Stay safe.</strong> Keep away from downed power lines and don't go on the roof yourself.</li>
<li><strong>Limit interior damage.</strong> Move belongings away from leaks and catch water where it's coming through.</li>
<li><strong>Take your own photos.</strong> Photograph damage you can see from the ground and inside the house.</li>
<li><strong>Call your insurer and a roofer.</strong> Your insurer decides on coverage; we document the damage and give you a written repair or replacement price.</li>
</ol>
<p>We don't decide insurance claims and we can't promise what a policy will cover, but clear documentation helps your adjuster understand what happened. For leaks that aren't storm-related, see [[roof-repair|roof repair]].</p>
<h2>Good to know</h2>
<p>Storm damage isn't always obvious right away. Shingles that lost their seal in high wind may stay in place for weeks before blowing off, and hail bruising can shorten a roof's life without causing an immediate leak. If several homes on your street have damage, it's worth an inspection even if your roof looks fine from the ground. Keep your own photos and dates, and avoid signing anything with door-to-door crews until you've seen the damage documented and priced in writing.</p>
""",
"faqs": [
("Will my insurance cover storm damage to my roof?", "That depends on your policy, the cause of the damage and the roof's condition before the storm. Your insurer makes that decision; we provide the inspection photos and repair details."),
("How can I tell if hail damaged my roof?", "Look for dents in vents, eavestroughs and downspouts, and granules washing out of the downspouts. Shingle bruising is hard to see from the ground, so an inspection is the reliable way to know."),
("Should I tarp the roof myself?", "We don't recommend it. Wet, damaged roofs are slippery and unstable. Call a roofer and limit damage from inside the house instead."),
],
"related": ["roof-repair", "roof-inspections", "eavestroughs"],
"cities": {
"windsor": "Windsor's mature tree canopy is beautiful until a summer storm brings branches down onto roofs. Impact damage can crack the deck under shingles that look fine, so after a tree or large limb hits a Windsor home, we check the decking and rafters as well as the surface.",
"lasalle": "Open subdivision streets and newer homes with fewer mature trees mean LaSalle storm damage is more often wind-related: missing shingles, lifted ridge caps and torn eavestroughs on the windward side of the house.",
"tecumseh": "Storms crossing Lake St. Clair can reach Tecumseh with strong wind, and homes nearer the shoreline take the brunt of it. Wind can break the seal on shingles without tearing them off, so we check for loose tabs across the whole roof, not just the obvious gaps."
},
},
{
"slug": "roof-inspections",
"name": "Roof Inspections",
"cat": "repair",
"icon": "inspect",
"short": "Detailed roof inspections with photos, an honest condition rating and a written list of what needs attention.",
"title": "Roof Inspections & Roof Condition Reports",
"desc": "Roof inspections with photos and a written condition report: shingles, flashing, ventilation, attic, eavestroughs. For homeowners, buyers and sellers.",
"h1": "Roof Inspections",
"lead": "Find out what your roof actually needs, with photos and plain answers, before a small problem turns into a ceiling repair.",
"body": """
<p>Most roof problems are cheap to fix early and expensive to fix late. A roof inspection tells you how much life your roof has left, what needs attention now and what can wait. {biz} inspects roofs for homeowners planning ahead, buyers and sellers, and anyone who has spotted something that doesn't look right.</p>
<h2>What we inspect</h2>
<ul>
<li><strong>Roof surface</strong> — shingle wear, granule loss, curling, cracking, lifted or missing shingles and previous repairs.</li>
<li><strong>Flashing</strong> — chimneys, walls, valleys, skylights and plumbing vents, the most common sources of leaks.</li>
<li><strong>Ventilation</strong> — intake and exhaust vents, plus signs of trapped heat or moisture.</li>
<li><strong>Attic</strong> — where accessible: staining, mould, frost, daylight and insulation that may be blocking airflow.</li>
<li><strong>Roofline</strong> — eavestroughs, downspouts, soffit and fascia, and how water leaves the roof.</li>
</ul>
<h2>What you get</h2>
<ol>
<li><strong>Photos.</strong> Clear photos of what we found, so you can see your roof without climbing a ladder.</li>
<li><strong>A condition summary.</strong> An honest assessment of the roof's overall condition and its expected remaining life.</li>
<li><strong>A priority list.</strong> What needs repair now, what to watch and what can wait.</li>
<li><strong>A written price.</strong> If work is needed, a separate written quote with no pressure to book it with us.</li>
</ol>
<p>An inspection is a good idea before buying or selling a home, after a major storm, if your roof is more than 15 years old, or when you notice granules in the eavestroughs. If repairs are needed, see [[roof-repair|roof repair]]; for storm-related concerns, see [[storm-damage-repair|storm damage repair]].</p>
<h2>Good to know</h2>
<p>If you're buying a home, schedule the roof inspection early in your conditional period so there's time to get quotes if work is needed. If you're selling, an inspection ahead of listing lets you fix small issues or price the house knowing the roof's condition. For homeowners, an inspection every few years, and after any major storm, catches problems while they're still small. Bring your questions: we'll explain what we see in plain language rather than handing you a list of jargon.</p>
""",
"faqs": [
("How long does a roof inspection take?", "Most residential inspections take under an hour on site, depending on the roof's size, access and whether we can get into the attic."),
("Do you walk on the roof?", "When it's safe to do so. On very steep or fragile roofs, we inspect from ladders, the edges and the attic instead."),
("Is a home inspection the same as a roof inspection?", "A general home inspection usually looks at the roof from the ground or a ladder. A roofer's inspection goes into more detail on flashing, ventilation and remaining life."),
],
"related": ["roof-repair", "roof-ventilation", "roof-replacement"],
"cities": {
"windsor": "For Windsor buyers looking at older homes, a roof inspection often answers the big questions a general inspection can't: how many layers are on the roof, what condition the plank decking is in and whether the chimney flashing is due. That's useful information before you firm up an offer.",
"lasalle": "Many LaSalle roofs are reaching the age where homeowners start asking how many years are left. An inspection gives you a realistic answer, so you can budget for a replacement on your timeline rather than after a leak.",
"tecumseh": "After a windy season, Tecumseh homeowners often call us because neighbours are replacing shingles. An inspection shows whether your roof came through intact or has loose and unsealed shingles that are likely to blow off next."
},
},
{
"slug": "roof-ventilation",
"name": "Roof Ventilation",
"cat": "repair",
"icon": "vent",
"short": "Balanced attic intake and exhaust to reduce ice dams, attic moisture and summer heat build-up.",
"title": "Roof & Attic Ventilation: Ridge, Soffit & Box Vents",
"desc": "Roof and attic ventilation: ridge vents, soffit intake, box vents and bath fan venting to help prevent ice dams, attic moisture and heat build-up.",
"h1": "Roof Ventilation",
"lead": "A roof that can't breathe wears out from the inside. Balanced attic ventilation protects the shingles, the deck and your ceilings.",
"body": """
<p>Your attic needs a steady flow of outside air: cool air in low at the soffits, warm moist air out high at the ridge. When that balance is off, heat bakes the shingles in summer, moisture condenses on the underside of the deck in winter and warm attic air melts snow that refreezes at the eaves as ice dams. {biz} assesses and corrects attic ventilation on its own or as part of a roof replacement.</p>
<h2>Ventilation work we do</h2>
<ul>
<li><strong>Ridge vents</strong> — a continuous vent along the peak that lets warm air escape evenly along the whole roof.</li>
<li><strong>Soffit intake</strong> — vented soffit panels and clear baffles so insulation doesn't block air coming in (see [[soffit-fascia|soffit and fascia]]).</li>
<li><strong>Box and roof vents</strong> — static vents where a ridge vent isn't practical, sized to the attic.</li>
<li><strong>Bath and kitchen fan venting</strong> — fans ducted all the way outside instead of into the attic, a common cause of attic moisture.</li>
<li><strong>Mixed-vent corrections</strong> — removing competing exhaust vents that short-circuit airflow.</li>
</ul>
<h2>Signs your ventilation needs work</h2>
<ol>
<li><strong>Ice dams</strong> along the eaves every winter, especially with icicles hanging from the eavestroughs.</li>
<li><strong>Frost or dampness</strong> on the underside of the roof deck or on nails in the attic during cold weather.</li>
<li><strong>Mould or dark staining</strong> on the attic sheathing.</li>
<li><strong>Very hot upper floors</strong> in summer, and shingles that are aging faster than they should.</li>
</ol>
<p>Ventilation works together with attic insulation and air sealing, so we look at all three. If an ice dam has already caused a leak, see [[roof-repair|roof repair]].</p>
<h2>Good to know</h2>
<p>Ventilation is easiest and least expensive to fix during a roof replacement, when the deck is open and a continuous ridge vent can be cut in. If your roof still has years left, many problems can still be improved now by clearing soffits, adding baffles and venting bathroom fans properly. Be cautious about adding powered attic fans without checking the house first: they can pull conditioned air and even exhaust gases from the living space. We look at the whole attic before recommending any change.</p>
""",
"faqs": [
("How much attic ventilation do I need?", "It depends on the attic floor area and whether there's a vapour barrier. As a general guide, building codes call for a minimum ratio of vent area to attic area, split between intake and exhaust. We calculate it for your attic."),
("Can I have too much ventilation?", "Too much exhaust without enough intake can pull conditioned air from the house. The goal is balance, not simply more vents."),
("Will better ventilation stop ice dams?", "It helps a lot, especially combined with good insulation and air sealing, but on some roof shapes eave protection is still essential."),
],
"related": ["roof-replacement", "soffit-fascia", "roof-inspections"],
"cities": {
"windsor": "Older Windsor homes were often built with little or no attic ventilation and have had insulation blown in over the years, covering the soffits. Adding baffles and opening up intake is often the most effective fix for the ice dams we see on these houses.",
"lasalle": "On many LaSalle homes, bathroom fans were vented into the attic or to a soffit instead of through the roof. That warm, damp air can cause frost and mould on the deck, so we check fan ducting on every ventilation visit.",
"tecumseh": "Some Tecumseh homes have a mix of ridge vents, box vents and gable vents added over the years. Too many exhaust types can actually reduce airflow, so we often remove some vents rather than adding more."
},
},
# ------------------------------------------------------------------ ROOFLINE & SKYLIGHTS
{
"slug": "eavestroughs",
"name": "Eavestroughs & Downspouts",
"cat": "roofline",
"icon": "gutter",
"short": "Seamless aluminum eavestroughs, downspouts and gutter guards that carry water away from your roof and foundation.",
"title": "Eavestroughs, Gutters & Downspouts",
"desc": "Seamless aluminum eavestrough installation, downspouts, gutter guards and repairs. Sized for your roof and directed away from the foundation.",
"h1": "Eavestroughs & Downspouts",
"lead": "Your roof sheds the water. Your eavestroughs decide where it ends up. We install seamless systems sized and sloped to actually carry it away.",
"body": """
<p>Overflowing, sagging or leaking eavestroughs do more damage than most people realize: rotted fascia, stained siding, washed-out gardens and water pooling against the foundation. {biz} installs and repairs eavestroughs and downspouts and sizes the system to the roof area it needs to drain.</p>
<h2>Eavestrough services</h2>
<ul>
<li><strong>Seamless aluminum eavestroughs</strong> — formed on site to the length of each run, so the only joints are at the corners and outlets.</li>
<li><strong>Downspouts and extensions</strong> — enough downspouts in the right places, with extensions that move water away from the foundation.</li>
<li><strong>Gutter guards</strong> — covers that reduce clogging from leaves and seeds, chosen for the trees around your house.</li>
<li><strong>Repairs and re-sloping</strong> — resealing leaking corners, re-hanging sagging sections and correcting slope so water doesn't sit.</li>
<li><strong>Cleaning and flushing</strong> — clearing troughs and downspouts and checking for underground connections that are blocked.</li>
</ul>
<h2>What we check</h2>
<ol>
<li><strong>Size.</strong> Large or steep roofs, and valleys that dump onto one section, may need larger troughs or extra downspouts.</li>
<li><strong>Slope and hangers.</strong> Troughs need a slight fall toward each outlet, with hidden hangers spaced close enough to carry snow and ice.</li>
<li><strong>Fascia and drip edge.</strong> We make sure water runs into the trough and not behind it, and replace rotted fascia first.</li>
<li><strong>Where water goes.</strong> Downspouts should discharge away from the foundation and, where applicable, follow municipal rules on downspout disconnection.</li>
</ol>
<p>New eavestroughs are often installed with a [[roof-replacement|new roof]] or new [[soffit-fascia|soffit and fascia]], so the whole roofline is finished at once.</p>
<h2>Good to know</h2>
<p>Most eavestrough problems come down to three things: debris, slope and capacity. Cleaning troughs at least once a year, usually in late fall, keeps them flowing and stops ice from building up inside them. If a run sags or holds water after rain, the hangers or slope need adjusting. If water pours over the front edge during heavy storms even when the troughs are clean, the system is undersized for that part of the roof, and a larger trough or an extra downspout is the fix.</p>
""",
"faqs": [
("Are seamless eavestroughs worth it?", "For most homes, yes. Fewer joints mean fewer places to leak, and they look cleaner. Sectional troughs still have a place for small repairs."),
("Do gutter guards really work?", "Good guards reduce how often troughs clog, especially under trees, but no guard is maintenance-free. We'll recommend a type based on what falls on your roof."),
("Should my downspouts go into the ground?", "It depends on your property and local rules. Many municipalities encourage disconnecting downspouts from the sewer and directing water onto the lawn instead."),
],
"related": ["soffit-fascia", "roof-replacement", "storm-damage-repair"],
"cities": {
"windsor": "Many older Windsor homes still have downspouts running into underground connections, and some neighbourhoods have been part of the City's basement flooding and downspout disconnection efforts. We'll talk through where your downspouts can discharge before changing them.",
"lasalle": "LaSalle homes with multiple roof levels and valleys often have troughs that overflow at one corner every heavy rain. Adding a downspout or upsizing that run usually solves it without replacing the whole system.",
"tecumseh": "Tecumseh's mature trees in established neighbourhoods mean leaves, seeds and maple keys in the eavestroughs every season. That's where gutter guards and properly placed downspouts make the biggest difference."
},
},
{
"slug": "soffit-fascia",
"name": "Soffit & Fascia",
"cat": "roofline",
"icon": "soffit",
"short": "Vented aluminum soffit, fascia wrap and rot repair for a clean roofline and proper attic intake.",
"title": "Soffit & Fascia Installation and Repair",
"desc": "Aluminum soffit and fascia installation, rot repair, vented soffit for attic airflow and capping. Often done with a new roof and eavestroughs.",
"h1": "Soffit & Fascia",
"lead": "The roofline is where the roof meets the house, and where rot, pests and poor ventilation start. We rebuild it clean and vented.",
"body": """
<p>Soffit is the underside of the roof overhang; fascia is the board along the edge that the eavestroughs hang from. Together they finish the roofline, keep animals out of the attic and, when the soffit is vented, supply the fresh air your attic needs. {biz} replaces and repairs soffit and fascia, usually alongside roofing or eavestrough work.</p>
<h2>Soffit and fascia services</h2>
<ul>
<li><strong>Vented aluminum soffit</strong> — perforated panels that let air into the attic while keeping insects and animals out.</li>
<li><strong>Fascia capping</strong> — aluminum wrapped over sound wood fascia for a low-maintenance finish that never needs painting.</li>
<li><strong>Rot repair</strong> — rotted fascia boards and rafter tails replaced before anything is capped over them.</li>
<li><strong>Pest damage</strong> — repairing openings where birds, squirrels or raccoons have got in, and closing them properly.</li>
<li><strong>Baffles and airflow</strong> — making sure insulation isn't blocking the new vented soffit (see [[roof-ventilation|roof ventilation]]).</li>
</ul>
<h2>Why we don't cap over rot</h2>
<ol>
<li><strong>Rot spreads.</strong> Covering soft wood with aluminum hides it while it keeps getting worse.</li>
<li><strong>Eavestroughs need a solid board.</strong> Hangers fastened into rotten fascia pull out under the weight of snow and ice.</li>
<li><strong>It points to the cause.</strong> Rotted fascia usually means water is getting behind the eavestrough or past the drip edge, which we correct.</li>
<li><strong>It's cheaper now.</strong> Replacing a few boards during the job costs far less than tearing the capping off later.</li>
</ol>
<p>Soffit and fascia are often replaced with new [[eavestroughs|eavestroughs]] or a [[roof-replacement|roof replacement]], so the roofline is finished in one visit and in matching colours.</p>
<h2>Good to know</h2>
<p>Soffit and fascia problems usually start small: a loose corner, a gap where an animal has pushed through or a soft spot behind an overflowing eavestrough. Catching these early keeps repairs to a few boards and panels instead of a full replacement. When you have work done, ask that the soffit be vented wherever the attic needs intake air and that any old wood be checked before it's covered. Matching colours to your eavestroughs and window trim also gives the whole roofline a finished, cohesive look.</p>
""",
"faqs": [
("What's the difference between soffit and fascia?", "Soffit is the horizontal panel under the overhang. Fascia is the vertical board along the roof edge, where the eavestroughs attach."),
("Do I need vented soffit?", "If your attic relies on soffit intake, yes. Without it, exhaust vents at the ridge can't work properly, which can lead to moisture and ice dams."),
("What colours are available?", "Aluminum soffit and fascia come in a wide range of colours. We'll help you match or complement your eavestroughs, windows and siding."),
],
"related": ["eavestroughs", "roof-ventilation", "roof-replacement"],
"cities": {
"windsor": "On older Windsor homes, original wood soffits are often solid boards with no ventilation at all, painted many times over. Replacing them with vented aluminum both cleans up the look and gives the attic the intake air it's been missing.",
"lasalle": "Many LaSalle homes already have aluminum soffit and fascia, but corners can be damaged by animals and fascia can rot where eavestroughs have overflowed. Targeted repairs are often all that's needed.",
"tecumseh": "Tecumseh's established neighbourhoods have plenty of squirrels and raccoons, and the roofline is where they get in. We repair the damage, close the openings and recommend a wildlife professional first if animals are still inside."
},
},
{
"slug": "skylights",
"name": "Skylights",
"cat": "roofline",
"icon": "skylight",
"short": "Skylight replacement, new installations and re-flashing to stop leaks around existing skylights.",
"title": "Skylight Installation, Replacement & Leak Repair",
"desc": "Skylight installation and replacement, sun tunnels and skylight leak repair with proper flashing kits. Often done during a roof replacement.",
"h1": "Skylights",
"lead": "A skylight should bring in light, not water. We install, replace and re-flash skylights with the kits made for the job.",
"body": """
<p>Skylights and sun tunnels can transform a dark hallway, bathroom or kitchen. They also put a hole in the roof, so the flashing has to be right. Most skylight leaks come from old or improvised flashing, failed seals in older units or condensation on single-pane glass. {biz} installs new skylights, replaces aging ones and fixes leaks around existing units.</p>
<h2>Skylight services</h2>
<ul>
<li><strong>Skylight replacement</strong> — old, fogged or leaking units replaced with new energy-efficient skylights and a complete flashing kit.</li>
<li><strong>New skylights</strong> — framing a new opening in the roof, with the interior light shaft finished by the appropriate trade.</li>
<li><strong>Sun tunnels</strong> — tubular skylights for small rooms and hallways where a full skylight isn't practical.</li>
<li><strong>Leak repair</strong> — re-flashing skylights and correcting the underlayment around them.</li>
<li><strong>Removal</strong> — closing up a skylight opening you no longer want and roofing over it to match.</li>
</ul>
<h2>Best time to replace a skylight</h2>
<ol>
<li><strong>During a roof replacement.</strong> The flashing is new, the shingles match and you avoid disturbing a new roof later.</li>
<li><strong>When the seal fails.</strong> Fogging between panes or condensation running down the shaft is a sign the unit is near the end.</li>
<li><strong>After repeated leaks.</strong> If the skylight has been patched more than once, replacing the unit and flashing is usually the lasting fix.</li>
<li><strong>When upgrading a room.</strong> Adding or enlarging a skylight is easiest before the room is finished.</li>
</ol>
<p>If your skylight is leaking right now, see [[roof-repair|roof repair]]. If your roof is due anyway, we'll include skylight replacement in your [[roof-replacement|roof replacement]] quote.</p>
<h2>Good to know</h2>
<p>Not every skylight problem means a new unit. Condensation in winter is often a humidity issue inside the house, and a fogged double-pane unit may still be watertight. On the other hand, a skylight that has been sealed with tar or caulking around the edges almost always needs proper flashing. If you're replacing your roof, it's worth asking about the age of your skylights: most homeowners find that replacing them during the reroof is far simpler than doing it a few years later.</p>
""",
"faqs": [
("Is it worth replacing skylights with a new roof?", "Usually, yes. Skylights tend to be replaced at about the same age as a roof, and doing them together avoids cutting into new shingles later."),
("Why does my skylight drip only in winter?", "Winter drips are often condensation rather than a leak, caused by warm, humid indoor air meeting cold glass. Newer units with better glass help, along with controlling indoor humidity."),
("Do new skylights need a permit?", "Cutting a new opening in the roof structure often requires a building permit. Replacing a unit in the same opening usually doesn't. We confirm with your municipality."),
],
"related": ["roof-repair", "roof-replacement", "roof-ventilation"],
"cities": {
"windsor": "Skylights on older Windsor homes were often added in the 1980s or 1990s with flashing that's now well past its life. When we replace those units, we also check the framing around the opening, since long-term leaks can soften the wood.",
"lasalle": "Many LaSalle homes built in the 1990s have skylights or sun tunnels over kitchens, bathrooms and stairwells. Those units are now reaching the same age as the original roofs, which makes a roof replacement the ideal time to swap them.",
"tecumseh": "On Tecumseh homes with skylights facing the prevailing wind, wind-driven rain can find its way under worn flashing. A proper manufacturer flashing kit with underlayment collars is what keeps those openings dry."
},
},
{
"slug": "snow-ice",
"name": "Ice Dam Prevention",
"cat": "roofline",
"icon": "ice",
"short": "Eave protection, roof heat cables, insulation fixes and safe ice dam removal to protect your roof edges.",
"title": "Ice Dam Prevention & Removal",
"desc": "Ice dam prevention and removal: eave protection membrane, heat cables, attic airflow and safe steam removal of ice. Protect your eaves and ceilings.",
"h1": "Ice Dam Prevention",
"lead": "Ice dams aren't a winter you just put up with. We fix why they form, protect the eaves and, when needed, remove the ice safely.",
"body": """
<p>Ice dams form when warm attic air melts snow on the upper roof and the meltwater refreezes at the colder eaves. The ridge of ice traps more water behind it, which backs up under the shingles and into soffits, walls and ceilings. Chipping at it with a hammer damages the roof. {biz} helps homeowners remove ice dams safely and, more importantly, stop them from coming back.</p>
<h2>How we prevent and treat ice dams</h2>
<ul>
<li><strong>Eave protection membrane</strong> — self-adhering ice and water membrane at the eaves and valleys so backed-up water can't get through to the deck.</li>
<li><strong>Ventilation and insulation</strong> — improving soffit intake and exhaust and finding warm-air leaks into the attic (see [[roof-ventilation|roof ventilation]]).</li>
<li><strong>Heat cable</strong> — roof and eavestrough heat cables for problem areas that can't be fixed any other way, installed on a dedicated circuit by a licensed electrician where required.</li>
<li><strong>Steam removal</strong> — low-pressure steam cuts channels through ice without damaging shingles the way picks and hammers do.</li>
<li><strong>Eavestrough fixes</strong> — re-hanging troughs pulled down by ice and adding downspouts where water freezes (see [[eavestroughs|eavestroughs]]).</li>
</ul>
<h2>The order we work in</h2>
<ol>
<li><strong>Stop the leak.</strong> If water is coming in, we open channels in the ice to let it drain.</li>
<li><strong>Find the heat source.</strong> We look for missing insulation, open attic hatches, bathroom fans and blocked soffits.</li>
<li><strong>Fix the roof edge.</strong> At the next reroof, or sooner if needed, we install eave protection to the depth your roof needs.</li>
<li><strong>Add cable only if needed.</strong> Heat cable is a last resort, not a first step.</li>
</ol>
<p>Ice dam leaks often damage the deck and fascia, so check [[roof-repair|roof repair]] once the snow is gone.</p>
<h2>Good to know</h2>
<p>A few simple habits help between visits. Keep eavestroughs and downspouts clear before winter so meltwater has somewhere to go. Use a roof rake from the ground to pull snow off the lower few feet of the roof after heavy snowfalls, without climbing a ladder. Make sure the attic hatch is weatherstripped and insulated, and that bathroom fans vent outdoors. If ice dams keep returning in the same spot, that location is telling you where heat is escaping.</p>
""",
"faqs": [
("Should I pull icicles or chip the ice off myself?", "We don't recommend it. Falling ice is dangerous, and chipping damages shingles and eavestroughs. Steam removal is safer for you and the roof."),
("Will a new roof stop ice dams?", "A new roof with proper eave protection stops the water from getting in, but the dams can still form. Fixing ventilation and attic insulation is what stops them forming."),
("Do heat cables use a lot of electricity?", "They do draw power when they're on, which is why we see them as a targeted fix for specific trouble spots rather than a whole-roof solution."),
],
"related": ["roof-ventilation", "eavestroughs", "roof-repair"],
"cities": {
"windsor": "Windsor winters swing above and below freezing often, which is exactly the pattern that builds ice dams. Story-and-a-half homes with finished upper rooms and sloped ceilings are especially prone, because there's little room for insulation and airflow behind those ceilings.",
"lasalle": "On LaSalle homes with complex roofs, ice dams tend to form above garages and in valleys where one roof drains onto another. Those spots are where we make sure eave protection is installed generously during a reroof.",
"tecumseh": "Tecumseh homes near the lake can see heavier snowfalls when winds blow across Lake St. Clair, which adds weight and meltwater at the eaves. Proper eave protection and clear eavestroughs matter more in those conditions."
},
},
]
