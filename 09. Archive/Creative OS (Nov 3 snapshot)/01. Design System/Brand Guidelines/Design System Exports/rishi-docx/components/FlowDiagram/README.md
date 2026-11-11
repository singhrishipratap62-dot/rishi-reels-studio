# FlowDiagram

Numbered steps in square boxes connected by drawn lines, showing how something works.

**Use for:** processes and "how it works" explanations — how a model is trained, how a scam works, how an agent completes a task, what happens to your data.

**Anatomy:** nodes are `bg` boxes with a 4px `ink` border, `label` number (`01`) and `title` text → connectors in `line-strong`, `stroke-rule` → optional pen circle or arrow on the key node.

**Motion:** grid fades in → nodes build left to right (or top to bottom), staggered 90ms → connectors draw between them (300ms) → pen marks the step that matters. For long diagrams, show it whole, then pan/zoom to each step as it's discussed.

**Rules:** 2–5 nodes per frame. One or two words per node title. Align nodes to the grid. Vertical layout works better for long chains in 9:16.

**You provide:** the steps in order and which one is the point.
