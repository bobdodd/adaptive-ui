# PhD Thesis: Accessibility of Hand-held Mobile Devices

**Author:** Robert Dodd
**Period:** Circa 2006-2010
**Location:** University of Teesside, Accessibility Research Centre
**Status:** Unpublished and undefended thesis work

> **Note:** This repository contains draft materials from an unpublished and undefended PhD thesis. The work represents research conducted at the University of Teesside but was not formally submitted for examination or publication.

## Thesis Summary

This PhD presents a novel systems‑modelling approach to **accessibility of hand‑held mobile devices**. The core problem is that mobile devices have constrained communication channels (visual, sonic, haptic) yet must present complex information, and existing web technologies (AJAX, scripting) are opaque to assistive technology like screen readers.

### Key Contributions

1. **Systems‑analysis methodology** – Adopts Shlaer‑Mellor Object‑Oriented Analysis to model the "encounter" between user capability and device capacity as five independent problem domains:
   - **Users** (capability profiles)
   - **Devices** (presentation capacity)
   - **Context** (operating environment)
   - **Content** (information to be presented)
   - **Adaptation** (mapping between the domains)

2. **CISNA five‑layer document model** – An extension of the Dexter/Amsterdam hypertext models that separates a document into:
   - **Content** (raw media)
   - **Inventory** (references and formatting)
   - **Semantics** (rules, nouns, verbs, ontologies)
   - **Navigation** (directed graph of nodes/edges)
   - **Adaptation** (transactions that modify layers for specific user profiles)

3. **Adaptation framework** – Uses Shlaer‑Mellor concepts (bridges, counterparts, assigner state models, role migration, recursive design/archetypes) to describe how content and interaction modalities can be dynamically reconfigured to match user needs.

4. **Measurable accessibility** – Proposes that accessibility can be quantified by measuring the "distance" (e.g., Levenshtein distance) between default and adapted interface representations.

5. **Prototype validation** – A working Java prototype adapts a Google Maps fragment between a default user and a low‑vision user (adding text‑to‑speech).

### Thesis Structure (from synopsis)

- Literature review & lead‑in (1 chapter)
- Core (5 chapters: accessibility definitions, design spaces, capability modelling, UI modelling, simulation)
- Analysis & lead‑out (1 chapter)
- Discussion of wider context (1 chapter)
- Appendices (detailed methodology, population tables)

## Directory Organization

```
organized_phd/
├── 01-thesis-meta/              # Thesis metadata and overview
│   ├── abstract.txt
│   ├── phd thesis synopsis v2.txt
│   ├── content.txt
│   ├── overview.txt
│   ├── bibliography.txt
│   └── glossary.txt
├── 02-problem-hypothesis/       # Problem statement and hypotheses
│   ├── Statement of problem.txt
│   ├── hypothesis.txt
│   ├── Defining Accessibility.txt
│   └── Possible Accessibility Definitions.txt
├── 03-methodology/              # Research methodology and approaches
│   ├── methodology.txt
│   ├── Design Language.txt
│   ├── Requirement Modelling.txt
│   ├── Templates.txt
│   ├── optimal matching.txt
│   ├── metaphor.txt
│   ├── Subject Areas.txt
│   ├── First Person.txt
│   └── Preference Modelling.txt
├── 04-core-models/              # Core modelling frameworks
│   ├── cisna-model/             # CISNA five-layer document model
│   │   ├── CISNA.txt
│   │   ├── theCISNAModelOfAccessibleAdaptiveHypermedia.txt
│   │   ├── adaptation.txt
│   │   └── fibonacci.xml
│   ├── dexter-amsterdam/        # Dexter/Amsterdam hypertext models
│   │   └── The Dexter Model of Hypertext in Context.txt
│   ├── design-spaces/           # Multi-sensory design spaces
│   │   ├── Design Spaces.txt
│   │   ├── Sonic Design Space.txt
│   │   ├── Notes on the Sonic Design Space.txt
│   │   ├── Haptic Design Space.txt
│   │   ├── Notes on the Haptic Design Space.txt
│   │   └── Notes on the Visual Design Space.txt
│   ├── user-models/             # User capability modelling
│   │   ├── User Capability Set.txt
│   │   ├── User Personas as Capability Populations.txt
│   │   ├── User Cap in the Adaptive World.txt
│   │   ├── users.txt
│   │   ├── Notes on The User Model.txt
│   │   ├── Notes on The User Model(1).txt
│   │   └── Personas.txt
│   ├── action-language/         # Action language and execution
│   │   ├── Action Language XML example.txt
│   │   └── Action Model Execution Engine.txt
│   └── other-models/            # Additional model components
│       ├── Notes on the Adaptation Model.txt
│       ├── Notes on the Adaptation Model(1).txt
│       ├── Notes on the Application Model.txt
│       ├── Notes on the Navigation Model.txt
│       ├── Notes on The Render Model.txt
│       ├── On Rendering.txt
│       ├── Notes on the Semantics Model.txt
│       ├── devices.txt
│       └── context.txt
├── 05-case-studies-examples/    # Case studies and examples
│   ├── Tetris Case Study.txt
│   ├── full circle.txt
│   └── gaming.txt
├── 06-images/                   # Supporting images
│   ├── rendering.png
│   └── modality ontologies.png
└── converted_files.txt          # List of all converted files
```

## File Organization

**Each directory contains both:**
- **Text versions** (.txt) – Converted from original formats for easy reading and searching
- **Original files** (.doc, .docx, .odt, .xml, .png) – Preserved in native formats for reference

All files have been organized into the same hierarchical structure, with paired files coexisting in each directory (e.g., `abstract.odt` and `abstract.txt` side-by-side).

## Conversion Notes

Original Microsoft Word (.doc, .docx) and OpenDocument (.odt) files were converted to plain text using `textutil` for readability. Original binary files have also been organized into the same directory structure for completeness.

## Key Files to Start With

1. **`01-thesis-meta/phd thesis synopsis v2.txt`** – Thesis structure and outline
2. **`01-thesis-meta/abstract.txt`** – Complete thesis abstract
3. **`02-problem-hypothesis/Statement of problem.txt`** – Problem statement
4. **`03-methodology/methodology.txt`** – Detailed research methodology
5. **`04-core-models/cisna-model/theCISNAModelOfAccessibleAdaptiveHypermedia.txt`** – Core CISNA model paper

## Research Context

This work was conducted at the University of Teesside's Accessibility Research Centre under supervision of Dr. Steve Green and Dr. Elaine Pearson. The research addresses the intersection of:
- Mobile device constraints (screen size, battery, processing power)
- Multi-sensory design spaces (visual, sonic, haptic, cognitive)
- Adaptive user interfaces for accessibility
- Hypertext models (Dexter, Amsterdam) and their limitations
- Object-oriented analysis (Shlaer-Mellor method)
- Measurable accessibility metrics