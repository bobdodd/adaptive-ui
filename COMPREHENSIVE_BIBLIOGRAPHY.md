# Comprehensive Bibliography & Paper Reviews

This document provides reviews and bibliographic entries for papers referenced in the PhD thesis on adaptive UI for mobile accessibility. Each entry includes:

1. **Bibliographic citation** (APA or ACM format)
2. **Summary** (beyond abstract, focused on thesis relevance)
3. **Thesis relevance** (why cited, what it tells us, questions raised)
4. **Cross-references** (thesis chapters, concepts, models)
5. **Category** (topic area)

## Categories

### Dexter Model & Hypertext
Papers on the Dexter Hypertext Reference Model, Amsterdam Model, and hypertext systems.

### Hypermedia & Multimedia
Papers on hypermedia, multimedia systems, synchronization, and adaptive hypermedia.

### Metaphor & Design Spaces
Papers on metaphor in UI, multi-sensory design spaces, and presentation metaphors.

### User Capability Modelling
Papers on user modelling, capability assessment, profiles, and accessibility.

### Sign Language & Communication
Papers on sign language, communication systems, and accessibility for deaf users.

### Methodologies & Modelling
Papers on Shlaer-Mellor, Executable UML, model-driven approaches.

### Accessibility & Assistive Technology
Papers on accessibility guidelines, assistive technology, and evaluation.

### Miscellaneous
Other relevant papers not fitting above categories.

---

## Dexter Model & Hypertext

### Halasz, F., & Schwartz, M. (1994). The Dexter hypertext reference model. *Communications of the ACM*, 37(2), 30-39.

**File:** `referenced papers/dexter_model/p30-halasz.pdf`
**Also:** `referenced papers/p30-halasz.pdf`

**Summary:**
The seminal paper introducing the Dexter Hypertext Reference Model, which provides a layered architectural model for hypertext systems. The model consists of three layers: Runtime Layer (user interaction), Storage Layer (component and link structure), and Within-Component Layer (content structure). It introduces key concepts including components (atoms, composites, links), anchors, presentations, and attributes.

**Thesis Relevance:**
- **Foundation for CISNA model:** The CISNA five-layer model extends Dexter, adding inventory and adaptation layers while reframing semantics and navigation.
- **Accessibility limitations:** Dexter's focus on navigation between components rather than semantic meaning creates challenges for assistive technology adaptation.
- **Basis for critique:** The thesis critiques Dexter's assumption of static components and lack of support for dynamic adaptation across design spaces.
- **Connections:** Chapter 4 (UI Modelling & AT) discusses Dexter limitations; w4a-blind paper extends Dexter to CISNA.

**Cross-references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology"
- Publication: `w4a-blind.doc` (CISNA model extension)
- Model: CISNA five-layer model vs. Dexter three-layer model

### Hardman, L., Bulterman, D.C.A., & Rossum, G.V. (1994). The Amsterdam hypermedia model: adding time and context to the Dexter model. *Communications of the ACM*, 37(2), 50-62.

**File:** `referenced papers/dexter_model/p50-hardman.pdf`
**Also:** `referenced papers/p50-hardman.pdf`

**Summary:**
Extension of the Dexter Hypertext Reference Model to support synchronized multimedia (hypermedia). Adds concepts of time, synchronization arcs, channels, and media component references to handle continuous media like audio and video. Introduces explicit support for competition for resources (e.g., audio channels, screen real estate) and synchronization between components.

**Thesis Relevance:**
- **Basis for CISNA adaptation:** Amsterdam's synchronization and channel concepts inform CISNA's adaptation layer for multi-sensory design space mapping.
- **Mobile relevance:** Amsterdam underpins SMIL (Synchronized Multimedia Integration Language) used in MMS (Multimedia Messaging System) for mobile phones, linking hypermedia models directly to mobile accessibility.
- **Accessibility challenges:** Highlights issues with semantic meaning of synchronized content (e.g., distinguishing background music from spoken text) crucial for adaptation between design spaces.
- **Connections:** Chapter 4 discusses Amsterdam limitations; w4a-blind paper references Amsterdam extensions.

**Cross-references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology"
- Publication: `w4a-blind.doc` (references Amsterdam model)
- Mobile context: SMIL, MMS, mobile multimedia accessibility

### Ceri, S., Daniel, F., Matera, M., & Facca, F. M. (2007). Model-driven development of context-aware Web applications. *ACM Transactions on Internet Technology*, 7(2), Article 1.

**File:** `referenced papers/dexter_model/p1-ceri.pdf`

**Summary:**
Proposes a model‑driven framework for developing context‑aware, multi‑channel Web applications using WebML (Web Modeling Language). The framework provides modeling facilities for context‑aware applications and shows how high‑level modeling constructs can drive application development through automatic code generation. Emphasizes user‑independent, context‑triggered adaptation actions where context operates as a "first‑class" actor independently of users on the same hypertext being navigated. The approach extends WebML, an established conceptual model for data‑intensive Web applications, to handle context‑aware adaptation.

**Thesis Relevance:**
- **Model‑driven development:** Demonstrates a model‑based approach to adaptive systems, relevant to thesis's use of Shlaer‑Mellor object‑oriented analysis for modeling adaptation.
- **Context‑aware adaptation:** Addresses adaptation based on context (environment, device, user), connecting to thesis's adaptation framework across user capability, device capacity, and context domains.
- **Hypertext extension:** Extends hypertext modeling (WebML) for adaptation, related to thesis's extension of Dexter/Amsterdam models to CISNA.
- **Automatic code generation:** Shows practical implementation of model‑driven approach, relevant to thesis's proposed Java prototype and action language execution.
- **Limitations:** Focuses on Web applications rather than mobile devices; adaptation is context‑triggered but may not address multi‑sensory design space mapping.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses model‑based approaches
- Model connection: WebML extension vs. CISNA extension of Dexter
- Mobile context: Paper's Web‑focus vs. thesis's mobile‑device focus

**Questions raised:**
- How could this model‑driven approach be adapted for mobile devices with constrained resources?
- What additional modeling constructs are needed for multi‑sensory adaptation across design spaces?
- How does context‑aware adaptation relate to user capability‑based adaptation?
- Could WebML be extended to support the CISNA five‑layer model?

---

## Hypermedia & Multimedia

### Bailey, C., Hall, W., Millard, D. E., & Weal, M. J. (2007). Adaptive hypermedia through contextualized open hypermedia structures. *ACM Transactions on Information Systems*, 25(4), Article 16.

**File:** `referenced papers/assets/Bailey et al2007Adaptive hypermedia through contextualized open hy.pdf`

**Summary:**
Re‑examines Brusilovsky's taxonomy of adaptive hypermedia (AH) techniques from a structural open hypermedia (OH) perspective. Argues that a wide range of AH techniques can be supported with a small number of OH structures, which can be combined to create complex adaptive effects. Identifies common structural patterns across the taxonomy of adaptive techniques. Presents HA3L, an agent‑based adaptive hypermedia system that uses OH structures to provide straightforward implementation of various AH techniques. Demonstrates structural equivalence of many adaptive techniques and shows advantages of the OH approach for designing future adaptive hypermedia systems.

**Thesis Relevance:**
- **AH‑OH integration:** Bridges adaptive hypermedia (AH) and open hypermedia (OH) research, directly relevant to the thesis's CISNA model which extends the Dexter OH model with adaptation capabilities.
- **Structural approach:** Emphasizes structural representations of adaptation, aligning with thesis's use of Shlaer‑Mellor object‑oriented analysis for modelling adaptation processes.
- **Taxonomy analysis:** Provides systematic analysis of adaptive techniques that could inform the design of the CISNA adaptation layer and action language.
- **Implementation example:** HA3L system demonstrates practical implementation of adaptive hypermedia using structural components, offering comparison point for thesis's Java prototype.
- **Limitations:** Focuses on general hypermedia rather than mobile‑specific constraints; does not address multi‑sensory adaptation across design spaces.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses adaptive hypermedia models
- Publication: `w4a‑blind.doc` – presents CISNA as adaptive hypermedia model extending Dexter
- Model connection: CISNA's adaptation layer vs. OH structures for adaptation
- Mobile context: Paper's general hypermedia focus vs. thesis's mobile‑device focus

**Questions raised:**
- How can OH structures be mapped onto the CISNA five‑layer model?
- How might mobile device constraints (processing, memory, bandwidth) affect the feasibility of structural adaptation approaches?
- What additional structures are needed to support adaptation across sensory modalities (visual → sonic/haptic)?
- How does the structural approach handle dynamic content (AJAX) common in mobile web applications?

### Sawhney, N., Balcom, D., & Smith, I. (1996). HyperCafe: Narrative and Aesthetic Properties of Hypervideo. In *Proceedings of the Seventh ACM Conference on Hypertext* (pp. 1-?). ACM.

**File:** `referenced papers/dexter_model/p1-sawhney.pdf`

**Summary:**
Presents HyperCafe, an experimental hypermedia prototype illustrating a general hypervideo system. Places users in a virtual café composed of digital video clips of actors engaged in fictional conversations. Allows users to follow different conversations through dynamic interaction opportunities via temporal, spatio‑temporal, and textual links presenting alternative narratives. Discusses components and a framework for hypervideo structures along with underlying aesthetic considerations. Explores multi‑threaded narratives, navigation, temporal links, and digital video as a hypermedia medium. The system redefines links for a video‑centric medium where they become spatial and temporal opportunities in video and text.

**Thesis Relevance:**
- **Hypervideo as hypermedia:** Extends hypertext concepts to video, relevant to thesis's extension of hypermedia models (Dexter/Amsterdam) to mobile accessibility.
- **Temporal/spatial linking:** Introduces temporal and spatio‑temporal links beyond traditional hypertext links, potentially informing adaptation across sensory modalities with temporal constraints (e.g., audio/haptic sequencing).
- **Narrative structures:** Explores multi‑threaded narratives and user choice, connecting to adaptation as navigation through alternative content representations.
- **Aesthetic considerations:** Addresses design aesthetics in adaptive systems, relevant to usability and user experience in accessible mobile interfaces.
- **Limitations:** Focuses on desktop hypervideo rather than mobile devices; does not address accessibility or adaptation for users with impairments.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses hypermedia models
- Model connection: Temporal links in hypervideo vs. synchronization in Amsterdam model
- Mobile context: Paper's desktop hypervideo focus vs. thesis's mobile‑device focus

**Questions raised:**
- How could hypervideo concepts be adapted for mobile devices with limited processing power and bandwidth?
- What additional structures are needed to make hypervideo accessible to users with sensory impairments?
- How might temporal linking inform the sequencing of multi‑sensory adaptations (e.g., coordinating audio descriptions with visual content)?
- Could narrative structures support adaptive storytelling for users with different cognitive capabilities?

### Gaura, E. I., & Newman, R. M. (2000). Using AI techniques to aid hypermedia design. In *Proceedings of the ...*.

**File:** `referenced papers/hypermedia/p100-gaura.pdf`

**Summary:**
Explores application of artificial intelligence techniques to aid hypermedia design, particularly helping designers understand and control presentation structure. While AI techniques have found applications in adaptive user interfaces and information search/retrieval, there have been fewer cases applying these techniques to the authoring process. Studies applicability of AI techniques (particularly Artificial Neural Networks - ANNs) to support authoring and design of structure in hypermedia. Proposes that structure (connectivity/graph of a hypermedia document) affects usability, and AI methods can help designers manage complexity. Discusses strategies including divide‑and‑conquer (breaking large systems into smaller structured presentations) and visual feedback about system structure.

**Thesis Relevance:**
- **AI for hypermedia design:** Demonstrates application of AI (neural networks) to hypermedia structure design, relevant to thesis's need for intelligent adaptation mechanisms.
- **Structural complexity management:** Addresses challenge of managing complex hypermedia structures, connecting to thesis's modeling of adaptation across multiple domains (user, device, content, context).
- **Authoring support:** Focuses on authoring/design process rather than runtime adaptation, but insights could inform design of adaptation rule authoring tools.
- **Usability of structure:** Proposes that hypermedia structure itself affects usability, relevant to adaptation as structural transformation for accessibility.
- **Limitations:** Focuses on design‑time authoring rather than runtime adaptation; does not address multi‑sensory or mobile constraints.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses hypermedia models and AI applications
- Model connection: AI techniques for structure design vs. object‑oriented analysis for modeling
- Adaptation relevance: Could inform intelligent adaptation rule generation

**Questions raised:**
- How could AI techniques (neural networks) be applied to runtime adaptation decisions in mobile accessibility?
- What is the trade‑off between AI‑generated adaptations and explicit rule‑based adaptations (as in CISNA action language)?
- How might structural complexity metrics inform adaptation decisions (e.g., simplifying navigation for users with cognitive impairments)?
- Could ANN‑based approaches learn adaptation mappings from examples of successful multi‑sensory transformations?

### Sawhney, N., & Murphy, A. (1999?). ESPACE a: An experimental hyperaudio environment. In *Proceedings of the ...*.

**File:** `referenced papers/p105-sawhney.pdf`

**Summary:**
Presents ESPACE a, a prototype system for navigation of hyper‑linked audio information in an immersive audio‑only environment. Proposes essential design concepts for audio‑only computing environments, describing a hyperaudio system based on prior design principles and discussing evaluation of a preliminary prototype. Introduces hyper‑linked audio navigation where audio content is conceived as nodes within a hypertextual framework, with audio nodes grouped within abstract containers and links established between audio content. Discusses contextual awareness through continuous audio indicating background activity or sense of location within an audio environment. Addresses challenges of representing temporal data and persistent objects in audio‑only interfaces.

**Thesis Relevance:**
- **Audio‑only hypermedia:** Extends hypertext/hypermedia concepts to audio‑only environments, relevant to multi‑sensory design space mapping and adaptation across modalities (visual → auditory).
- **Hyperaudio navigation:** Proposes audio‑node‑based hypertext structure, connecting to thesis's hypermedia models (Dexter/Amsterdam) and their extension to non‑visual modalities.
- **Contextual audio awareness:** Uses continuous audio for spatial awareness and context, informing adaptation techniques for users with visual impairments.
- **Design principles for non‑visual interfaces:** Provides design concepts for audio‑only computing, relevant to accessibility adaptation for blind/low‑vision users.
- **Limitations:** Focuses on desktop audio‑only environments rather than mobile devices; does not address multi‑modal (visual+auditory) adaptation.

**Cross‑references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – discusses multi‑sensory design spaces including auditory
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses hypermedia models and non‑visual interfaces
- Model connection: Hyperaudio nodes vs. Dexter/Amsterdam components
- Mobile context: Paper's desktop audio‑focus vs. thesis's mobile‑device focus

**Questions raised:**
- How could hyperaudio concepts be adapted for mobile devices with limited audio capabilities and noisy environments?
- What additional design principles are needed for combined visual‑auditory interfaces (rather than audio‑only)?
- How might hyperaudio navigation inform adaptation of visual hypermedia for users with visual impairments?
- Could audio‑node‑based hypertext structures be integrated with the CISNA model's adaptation layer?

### Petersen, M. G., & Grønbæk, K. (2004?). Domestic hypermedia: Mixed media in the home. In *Proceedings of the ...*.

**File:** `referenced papers/p108-petersen.pdf`

**Summary:**
Analyses potentials for use of hypermedia in homes based on empirical studies. Characterizes use of physical materials by collaborative spatial organization and persistent visual awareness—qualities not well supported for digital materials. Notes that domestic materials (photos, music, messages) become digitized but personal computers provide centralized, individualized access lacking spatial distribution, persistence, and visibility of physical material. Proposes a Domestic Hypermedia infrastructure combining spatial, context‑aware, and physical hypermedia to support collaborative structuring and ambient presentation of materials in homes. The research is grounded in studies of how homes use physical materials to coordinate and structure domestic information.

**Thesis Relevance:**
- **Context‑aware hypermedia:** Extends hypermedia to domestic environments with spatial and context‑aware properties, relevant to thesis's context domain in adaptation framework.
- **Physical‑digital integration:** Addresses integration of physical and digital materials, informing adaptation between different presentation modalities (physical vs. digital).
- **Spatial organization:** Highlights spatial distribution of materials in homes, connecting to multi‑sensory design space and spatial adaptation for mobile devices.
- **Ambient presentation:** Proposes ambient presentation of materials, relevant to non‑intrusive adaptation for users with cognitive impairments.
- **Limitations:** Focuses on home environments rather than mobile devices; does not address accessibility or impairment‑specific adaptation.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses context‑aware hypermedia
- Thesis context domain: Domestic environment as a specific context type
- Model connection: Spatial hypermedia vs. Amsterdam model's synchronization concepts
- Mobile context: Paper's home‑focus vs. thesis's mobile‑device focus

**Questions raised:**
- How could domestic hypermedia concepts be adapted for mobile devices used across different contexts (home, work, travel)?
- What additional adaptation mechanisms are needed for users with impairments in domestic environments?
- How might spatial organization of physical materials inform spatial adaptation of digital content on small mobile screens?
- Could ambient presentation techniques reduce cognitive load for users with cognitive impairments?

### Nanard, M., Nanard, J., & Kahn, P. (1999?). Pushing reuse in hypermedia design: Golden rules, design patterns and constructive templates. In *Proceedings of the ...*.

**File:** `referenced papers/hypermedia/p11-nanard.pdf`

**Summary:**
Addresses reuse in hypermedia design as a strategic approach for reducing cost and improving quality. Classifies and explores different types of reuse in hypermedia design, focusing on reuse of design experience. Introduces constructive templates as a practical technique for capturing specification of reusable structures and components during design process and populating target hypermedia. Templates act as a bridge for reuse from design to implementation. Discusses connections between constructive templates and design patterns, showing how templates help push reuse into action by capturing implementation of design patterns and automating their use. Based on design and development of a real hypermedia application, the paper explores reuse types through examples and discusses relationship of reuse types to design patterns.

**Thesis Relevance:**
- **Design methodology for hypermedia:** Provides structured approach to hypermedia design with reusable patterns and templates, relevant to thesis's need for systematic adaptation design methodologies.
- **Constructive templates:** Introduces template‑based approach for capturing and reusing design structures, potentially applicable to adaptation rule templates in CISNA model.
- **Design patterns in hypermedia:** Extends software engineering design pattern concepts to hypermedia, connecting to thesis's use of object‑oriented analysis (Shlaer‑Mellor) for modeling adaptation.
- **Reuse classification:** Categorizes reuse types (data, software components, design experience), informing systematic approach to adaptation rule reuse across different user‑device‑context mappings.
- **Limitations:** Focuses on hypermedia design rather than runtime adaptation; does not address accessibility or mobile‑specific constraints.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses hypermedia design methodologies
- Model connection: Constructive templates vs. CISNA action language templates for adaptation
- Design pattern relevance: Paper's hypermedia design patterns vs. thesis's adaptation patterns

**Questions raised:**
- How could constructive templates be adapted for designing adaptation rules in mobile accessibility systems?
- What additional template types are needed for multi‑sensory adaptation across design spaces?
- How might hypermedia design patterns inform the design of adaptation patterns for users with specific impairments?
- Could template‑based approaches reduce complexity of authoring adaptation rules in CISNA model?

### Pyssysalo, T., Repo, T., Turunen, T., Lankila, T., & Röning, J. (2000). CyPhone – Bringing Augmented Reality to Next Generation Mobile Phones. In *Proceedings of DARE 2000*.

**File:** `referenced papers/p11-pyssysalo.pdf`

**Summary:**
Presents CyPhone, a prototype implementation of a future mobile phone designed to support context‑specific and multi‑user multimedia services in an augmented reality manner. Implements context‑awareness with GPS‑based navigation techniques and a registration algorithm capable of detecting predefined 3D models or landmarks in the environment. Develops a new adaptive transport protocol to support real‑time packet‑switched data transfer between concurrent users of mobile augmented reality applications. The prototype is based on PC/104 architecture and uses off‑the‑shelf hardware components. As a case example, describes an augmented reality‑based personal navigation service for cyclists using head‑mounted displays (HMDs). Addresses challenges of mobile networked augmented reality including efficient transmission, consistency, and multi‑user collaboration.

**Thesis Relevance:**
- **Mobile augmented reality:** Demonstrates context‑aware mobile services using augmented reality, directly relevant to thesis's focus on mobile device accessibility and adaptation.
- **Context‑awareness implementation:** Uses GPS and computer vision for context detection, informing adaptation based on environmental context (location, objects).
- **Adaptive transport protocol:** Develops protocol adapting to wireless link quality, relevant to adaptation across network conditions as part of device capacity constraints.
- **Multi‑user mobile services:** Addresses collaborative applications (CSCW) on mobile devices, connecting to social context dimension in adaptation framework.
- **Limitations:** Focuses on augmented reality rather than accessibility adaptation; does not address impairment‑specific adaptations or multi‑sensory design spaces.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses mobile context‑aware systems
- Thesis context domain: Environmental context detection and location‑based services
- Mobile device constraints: Bandwidth, processing power, battery considerations
- Adaptation relevance: Context‑aware adaptation for mobile augmented reality vs. accessibility adaptation

**Questions raised:**
- How could augmented reality techniques be adapted for users with visual impairments (e.g., audio‑based augmented reality)?
- What additional context detection methods are needed for indoor environments where GPS is unavailable?
- How might adaptive transport protocols inform adaptation across varying network conditions for users with different bandwidth requirements?
- Could augmented reality interfaces be adapted across sensory modalities (visual → auditory/haptic) for users with sensory impairments?

### Mogensen, P., & Grønbæk, K. (2000?). Hypermedia in the Virtual Project Room - Toward Open 3D Spatial Hypermedia. In *Proceedings of Hypertext 2000*.

**File:** `referenced papers/hypermedia/p113-mogensen.pdf`

**Summary:**
Discusses hypermedia aspects of designing a Virtual Project Room based on ethnographic and participatory design studies of landscape architects' and architects' work. Develops prototypes for virtual project rooms supporting remote collaboration. Since architects work with 3D objects and environments, the virtual project room is designed as a 3D virtual environment. The prototype, Manufaktur, utilizes open hypermedia technology to integrate documents with design models in the virtual project room. Provides hot‑linking of arbitrary MS Windows documents into the virtual project room, supports spatial arrangement and categorization of workspaces by proximity, and provides "classical" open hypermedia linking between document segments. Also supports two modes of tightly coupled collaboration through session management services. Combines experiences from Collaborative Virtual Environments (CVE), Open Hypermedia, Spatial Hypermedia, and CSCW.

**Thesis Relevance:**
- **Spatial hypermedia:** Extends hypermedia concepts to 3D spatial environments, relevant to multi‑sensory design space and spatial adaptation for mobile devices.
- **Virtual workspace augmentation:** Proposes augmenting physical workspaces with virtual counterparts, connecting to adaptation between physical and digital presentation modalities.
- **Collaborative virtual environments:** Addresses multi‑user collaboration in virtual spaces, relevant to social context dimension in adaptation framework.
- **Open hypermedia integration:** Uses open hypermedia technology for document linking, connecting to thesis's use of hypermedia models (Dexter/Amsterdam/CISNA).
- **Limitations:** Focuses on architectural design rather than accessibility; does not address impairment‑specific adaptations or mobile device constraints.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses hypermedia and collaborative systems
- Model connection: Spatial hypermedia vs. Amsterdam model's synchronization concepts
- Context domain: Virtual project rooms as specific context type
- Adaptation relevance: Spatial arrangement for cognitive organization vs. adaptation for cognitive impairments

**Questions raised:**
- How could spatial hypermedia concepts be adapted for mobile devices with small screens and limited 3D rendering capabilities?
- What additional spatial organization techniques could support users with cognitive impairments in virtual workspaces?
- How might virtual project rooms be made accessible to users with visual or motor impairments?
- Could spatial hypermedia inform the spatial adaptation of content across sensory modalities (e.g., arranging auditory cues in 3D audio space)?

---

## Metaphor & Design Spaces

### Nesbitt, K.V. (2001). Modeling the multi-sensory design space. In *Proceedings of the 2001 Asia-Pacific Symposium on Information Visualisation* (Vol. 9, pp. 27-36). Darlinghurst, Australia: Australian Computer Society.

**File:** `referenced papers/p27-nesbitt.pdf`

**Summary:**
Extends visualization concepts to multi-sensory displays (visual, auditory, haptic) creating a unified "multi-sensory design space." Proposes a structured classification of information types (nominal, quantitative, ordered) and their representation across sensory modalities. Uses UML notation to model design spaces and correlates them with metaphor-based classifications.

**Thesis Relevance:**
- **Core theoretical foundation:** Directly cited as key paper supporting the research; thesis extends Nesbitt's design spaces to visual, sonic, haptic, and cognitive interaction.
- **Design space structuring:** Provides taxonomy for analyzing user-device interaction across modalities, informing user capability modelling and device capacity assessment.
- **UML modelling approach:** Aligns with thesis's use of Shlaer-Mellor/Object-Oriented Analysis for modelling.
- **Metaphor correlation:** Links design spaces to metaphor selection, relevant to adaptive UI metaphor mapping.

**Cross-references:**
- Thesis Abstract: explicitly extends Nesbitt's concept of design spaces
- Thesis Glossary: multiple entries defining Nesbitt's terms (design space, perceptualization, temporal encoding)
- Chapter 2: "Design Spaces & Metaphor"
- Methodology: cited as example of accepted research approach using UML notation

**Questions raised:**
- How to extend design space model to include cognitive and contextual dimensions?
- How to operationalize design space mapping for real-time adaptation?
- How to handle competing demands across sensory channels in resource  constrained mobile devices?

### Noble, J., Biddle, R., & Tempero, E. (2002). Metaphor and metonymy in object-oriented design patterns. In *Proceedings of the ...*.

**File:** `referenced papers/assets/Noble et al2002Metaphor and metonymy in object-oriented design pa.pdf`

**Summary:**
Analyzes object‑oriented design patterns through the lens of literary theory, distinguishing metaphor (objects representing real‑world entities) from metonymy (objects representing attributes, causes, or effects). Uses Jakobson and Lodge's typology to show that while basic object‑oriented design is metaphorical (e.g., `Cow` object represents a cow), advanced patterns like State, Strategy, and Visitor are metonymic—they represent abstract concepts rather than concrete world objects. Argues that understanding both metaphor and metonymy helps designers create more accurate, flexible, and comprehensible software architectures. The paper bridges software engineering and literary criticism, offering a novel perspective on design pattern semantics.

**Thesis Relevance:**
- **Metaphor theory:** Provides a theoretical foundation for analyzing UI metaphors, distinguishing direct representation (metaphor) from abstract representation (metonymy). Relevant to thesis's discussion of metaphor in adaptive UI design.
- **Design pattern analysis:** Connects software design patterns to literary concepts, demonstrating interdisciplinary approach that parallels thesis's integration of hypertext models (Dexter) with accessibility.
- **Abstraction levels:** Highlights different levels of abstraction in design, which may inform adaptation between sensory modalities—metonymic mappings could support transformation across design spaces.
- **Limitations:** Focuses on software design patterns rather than UI metaphors; applicability to multi‑sensory UI adaptation requires extension.

**Cross‑references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – theoretical foundation for metaphor analysis
- Thesis Glossary: entries on metaphor, design patterns
- Model connection: Metaphor/metonymy distinction could inform mapping between user capability and device capacity representations

**Questions raised:**
- How does the metaphor/metonymy distinction apply to multi‑sensory UI design and adaptation?
- Can metonymic patterns inform the transformation of content across sensory modalities (visual → sonic/haptic)?
- How might literary theory concepts be operationalized in automated adaptation systems?
- What role do cultural differences in metaphor interpretation play in internationalized accessible design?

### Weiner, E. J. (1984). A knowledge representation approach to understanding metaphors. In *Proceedings of the ...*.

**File:** `referenced papers/metaphor/p1-weiner.pdf`

**Summary:**
Explores non‑literal language ("metaphors") through a knowledge representation approach amenable to computational modeling. Examines and expands Ortony's theories of salience and asymmetry in human metaphor processing. Identifies multiple interacting factors in metaphor comprehension: salience, asymmetry, incongruity, hyperbolicity, inexpressibility, prototypicality, and probable value range. Proposes a knowledge representation system incorporating these factors and their interactions, using a revised version of KL‑ONE. The approach focuses on computational modeling of metaphor understanding rather than literary analysis.

**Thesis Relevance:**
- **Computational metaphor modeling:** Provides a formal, computational approach to metaphor representation, relevant to thesis's need for operationalizing metaphor in adaptive UI design.
- **Knowledge representation:** Uses KL‑ONE (description logic) for modeling, connecting to thesis's use of formal models (Shlaer‑Mellor, UML) for representing adaptation mappings.
- **Factor analysis:** Identifies specific factors in metaphor comprehension (salience, asymmetry, etc.) that could inform metaphor selection in multi‑sensory design space mapping.
- **Formalization:** Demonstrates how literary/linguistic concepts can be formalized for computational systems, relevant to automating adaptation decisions.
- **Limitations:** Focuses on linguistic metaphor comprehension rather than UI metaphors; does not address multi‑sensory or accessibility concerns.

**Cross‑references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – theoretical foundation for metaphor analysis
- Model connection: Knowledge representation (KL‑ONE) vs. object‑oriented analysis (Shlaer‑Mellor) for modeling
- Adaptation relevance: Metaphor comprehension factors could inform adaptation rule selection

**Questions raised:**
- How could this knowledge representation approach be extended to UI metaphors (e.g., desktop, folder, trash can)?
- What additional factors are needed for modeling metaphor in multi‑sensory interfaces (visual, sonic, haptic)?
- How might metaphor comprehension models inform adaptive metaphor selection for users with different cognitive capabilities?
- Could KL‑ONE or similar description logics represent mappings between design spaces?

### Howell, M., Love, S., & Turner, M. (2005). Spatial metaphors for a speech-based mobile city guide service. *Personal and Ubiquitous Computing*, 9(1), 20–29.

**File:** `referenced papers/metaphor/779_2004_Article_271.pdf`

**Summary:**
Investigates use of spatial interface metaphors for speech‑based automated mobile city guide services. Implements four services: non‑metaphor numbered menu, travel system metaphor, office filing system metaphor, and shopping metaphor. Measures participant performance and subjective evaluations across trials. Results show for first‑time users the non‑metaphor service was most usable, but after three trials the office filing system metaphor service was most usable. Demonstrates that navigational cues from spatial metaphors can improve user attitudes and interactions with automated phone services.

**Thesis Relevance:**
- **Spatial metaphors for mobile interfaces:** Directly addresses metaphor use in mobile speech interfaces, relevant to thesis's focus on mobile device accessibility and adaptation.
- **Metaphor evaluation methodology:** Provides empirical evaluation of different metaphor types, informing methodology for testing adaptive metaphor selection.
- **Speech‑based mobile services:** Focuses on speech interaction for mobile users, relevant to adaptation for users with visual impairments or situational disabilities.
- **Metaphor learning curve:** Shows metaphor effectiveness improves with experience, suggesting adaptive systems may need to adjust metaphor selection based on user familiarity.

**Cross‑references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – discusses metaphor selection and evaluation
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses mobile speech interfaces
- Mobile context: Directly addresses mobile device constraints and speech interaction
- Adaptation relevance: Metaphor selection as adaptation technique for user capabilities

**Questions raised:**
- How could spatial metaphors be adapted for users with cognitive impairments?
- What metaphors are most effective for different user capabilities (e.g., users with visual vs. motor impairments)?
- How might metaphor selection be automated based on user context and task?
- Could spatial metaphor effectiveness inform the design of multi‑sensory adaptations?

---

## Accessibility & Assistive Technology

### Tan, C. C., Yu, W., & McAllister, G. (2007). An adaptive & adaptable approach to enhance web graphics accessibility for visually impaired people. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 1539-1542). ACM.

**File:** `referenced papers/assets/p1539-tan.pdf`

**Summary:**
Presents a component-based adaptive and adaptable system for making web graphics accessible to visually impaired users. The system considers three key variables: (1) assistive technologies (audio, haptic, tactile devices), (2) graphic types/formats (graphs, maps, images, 3D objects), and (3) user behaviors/preferences. Uses a three-level adaptation approach (content, system, user) implemented through five components: Sub‑Application Database (handles graphic‑specific applications), Graphical Content System (identifies graphic type), Control Centre (user profile management), Context Manager (stores adaptation context), and Core Processor Module (executes adaptation). The system is interoperable with common browsers (IE, Firefox) and screen readers (JAWS), and uses XML to describe user profiles and system configuration.

**Thesis Relevance:**
- **Adaptive/adaptable architecture:** Demonstrates a practical implementation combining both adaptive (system‑driven) and adaptable (user‑controlled) approaches, relevant to the thesis's adaptation framework.
- **Multi‑variable adaptation:** Shows adaptation across user, content, and technology dimensions, aligning with the thesis's focus on mapping between user capability and device capacity.
- **Component‑based design:** Illustrates modular architecture for accessibility systems, which could inform the thesis's proposed CISNA model implementation.
- **Limitations for critique:** Focuses on web graphics rather than mobile devices; lacks explicit hypertext model (Dexter/CISNA) for semantic adaptation; adaptation is based on format matching rather than semantic transformation across design spaces.
- **State‑of‑the‑art context:** Represents contemporary (2007) research in graphics accessibility, providing comparison point for the thesis's mobile‑focused approach.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – could reference as example of adaptive system design
- Thesis Chapter 5: "Usability & Simulation Experiences" – could compare evaluation methods
- Model comparison: CISNA five‑layer model vs. three‑level adaptation approach
- Mobile context: Paper's web‑focus vs. thesis's mobile‑device focus

**Questions raised:**
- How could this architecture be extended to mobile devices with constrained resources?
- How might hypertext models (Dexter, CISNA) improve semantic adaptation of graphics?
- How to handle adaptation between sensory modalities (visual → sonic/haptic) beyond format conversion?
- What metrics could quantify the accessibility gain provided by such adaptive systems?

### Encelle, B., & Baptiste-Jessel, N. (2007). Personalization of user interfaces for browsing XML content using transformations built on end-user requirements. In *Proceedings of the 2007 International Cross-Disciplinary Conference on Web Accessibility (W4A)* (pp. 58-?). ACM.

**File:** `referenced papers/assets/p58-encelle.pdf`

**Summary:**
Proposes a model‑based approach for generating personalized multimodal user interfaces for browsing XML content, targeting users with impairments. Identifies four core requirements for content browsing: (R1) selection of sub‑information to present, (R2) choice of output modalities, (R3) specification of navigation/scanning possibilities, (R4) choice of input modalities. Introduces profiles of policies with stereotype‑based profiles (expert‑defined for user groups) and personalized profiles (user‑defined). Transformation rules are generated from these profiles to adapt XML content into accessible interfaces supporting multiple modalities (text‑to‑speech, Braille). The approach separates user‑friendly specification languages from system‑friendly transformation rules.

**Thesis Relevance:**
- **Model‑based UI generation:** Aligns with thesis's use of Shlaer‑Mellor/Object‑Oriented Analysis for modelling user‑device interaction; demonstrates practical application of modelling for accessibility.
- **Profile architecture:** Distinguishes stereotype (group) and personalized (individual) profiles, relevant to thesis's user capability modelling and adaptation framework.
- **XML transformation:** Shows how structured content (XML) can be transformed for accessibility, connecting to thesis's CISNA model which uses XML for action language representation.
- **Multimodal output:** Addresses adaptation across sensory modalities (visual → auditory/tactile), relevant to multi‑sensory design space mapping.
- **Limitations:** Focuses on XML content browsing rather than general mobile UI; transformation approach may not handle dynamic content (AJAX) or complex interaction patterns.

**Cross‑references:**
- Thesis Chapter 3: "Capability Modelling & User Constraints" – profile concepts
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – model‑based UI generation
- Model comparison: CISNA adaptation layer vs. transformation rule generation
- Mobile context: Paper's XML‑focus vs. thesis's mobile‑device focus

**Questions raised:**
- How could this model be extended to handle dynamic web content (AJAX) common in mobile applications?
- How might stereotype profiles be derived from measurable user capability assessments?
- What is the performance overhead of run‑time transformation on resource‑constrained mobile devices?
- How does this approach scale to complex interactive applications beyond content browsing?

### Brewster, S. A., Rantyo, V.-P., & Kortekangas, A. (1998). Enhancing scanning input with non-speech sounds. In *Proceedings of the ...*.

**File:** `referenced papers/p10-brewster.pdf`

**Summary:**
Proposes adding non‑speech sounds to aid people using scanning as their method of input. Scanning input is a temporal task where users press a switch when a cursor is over the required target, but is typically presented as a spatial task with items laid out in a grid. Research shows auditory modality is often better than visual for temporal tasks. The paper investigates this by adding non‑speech sound to a visual scanning system and shows how natural rhythm perception abilities can support the scanning process. Uses structured audio messages called Earcons for sound output. Preliminary results indicate feasibility. The work is part of the TIDE ACCESS Project aiming to create a mobile communication device for speech‑motor and/or language‑cognitive impaired users.

**Thesis Relevance:**
- **Multi‑modal accessibility:** Demonstrates auditory enhancement for visual scanning interfaces, directly relevant to multi‑sensory design space mapping and adaptation across modalities.
- **Mobile assistive technology:** Part of a project creating mobile communication devices for impaired users, aligning with thesis's focus on mobile device accessibility.
- **Earcons & non‑speech sounds:** Uses structured audio (Earcons) for conveying information, relevant to sonic design space and adaptation from visual to auditory representations.
- **Temporal vs. spatial tasks:** Highlights differences between temporal and spatial task representations, informing adaptation between different sensory modalities.
- **Limitations:** Focuses on scanning input rather than general UI adaptation; does not address hypertext models or semantic adaptation.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses multi‑modal interfaces
- Thesis Chapter 5: "Usability & Simulation Experiences" – could compare evaluation methods
- Mobile context: Directly addresses mobile communication devices for impaired users
- Design space connection: Visual → auditory adaptation example

**Questions raised:**
- How could Earcons be adapted for users with hearing impairments (e.g., through haptic equivalents)?
- What is the cognitive load of simultaneous visual scanning and auditory feedback?
- How might this approach scale to complex mobile applications beyond simple scanning grids?
- Could rhythm‑based auditory cues inform temporal sequencing in multi‑sensory adaptations?

### Lopes, J. B. (2001). Designing user interfaces for severely handicapped persons. In *Proceedings of the ...*.

**File:** `referenced papers/user_capability_model/p100-lopes.pdf`

**Summary:**
Addresses factors involved in designing user interfaces for elderly persons and persons with severe disabilities. Stresses the great diversity of user needs and questions how such needs can be met. Proposes an approach based on the Designing for Dynamic Diversity (D3) concept, where interfaces must adapt to each particular user disability profile, not only at a given time but also to changes in the user profile over time. Distinguishes between elderly persons (gradual disability progression) and severely handicapped persons (multiple severe disabilities emerging rapidly, then stable). Presents an example from the INTERCOMUNICANDO project: a simple game interface developed and tested to acquire parameters for an advanced user model of severely disabled persons. Results show need for highly parameterised applications and further research to design frameworks and tools supporting many different user levels.

**Thesis Relevance:**
- **User capability modeling:** Directly addresses user capability profiling for accessibility, central to thesis's user capability domain modeling.
- **Dynamic Diversity (D3) concept:** Introduces adaptation to changing user profiles over time, relevant to thesis's adaptation framework across temporal dimensions.
- **Severe disability focus:** Addresses users with multiple severe disabilities, expanding beyond typical accessibility research focused on single impairments.
- **Parameter acquisition:** Demonstrates empirical approach to acquiring user model parameters through testing, relevant to thesis's methodology for user capability assessment.
- **Limitations:** Focuses on desktop interfaces rather than mobile devices; does not address hypertext models or multi‑sensory adaptation.

**Cross‑references:**
- Thesis Chapter 3: "Capability Modelling & User Constraints" – core relevance
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses adaptive UI design
- Model connection: D3 concept vs. thesis's adaptation across user, device, content, context domains
- Mobile context: Paper's desktop focus vs. thesis's mobile‑device focus

**Questions raised:**
- How could the D3 concept be extended to mobile devices with their additional constraints (small screens, limited input)?
- What additional parameters are needed for modeling users with multiple severe disabilities in mobile contexts?
- How might hypertext models (Dexter/CISNA) support structural adaptation for diverse user capability profiles?
- Could parameter acquisition methods be automated for runtime adaptation in mobile applications?

### Petrie, H., Fisher, W., Weimann, K., & Weber, G. (2004?). Augmenting icons for deaf computer users. In *Proceedings of CHI 2004 Late Breaking Results* (pp. ?-?). ACM.

**File:** `referenced papers/sign language/p1131-petrie.pdf`

**Summary:**
Investigates augmenting icons with tooltips (TTs) to make icons more understandable to deaf and hearing impaired users. Implements four types of TTs: Sign Language (video of sign), Picture (enlarged icon with text explanation), Human Mouth (video of mouth movements for lip reading), and Digital Lips (synthesized lip movements). Evaluation with 12 deaf users found Sign Language and Picture TTs were very positively rated on satisfaction and understanding and would be used again, while Human Mouth and Digital Lips were of no assistance in their current implementation for lip reading icon names. Discusses semiotic relationships between icons and their referents (iconic, indexical, symbolic signs) and how different augmentations strengthen these relationships. The research addresses the challenge of making graphical user interfaces accessible to users with print disabilities who cannot rely on text‑based tooltips.

**Thesis Relevance:**
- **Multi‑modal icon augmentation:** Demonstrates adaptation of visual icons through multiple modalities (sign language, pictures, lip reading), relevant to multi‑sensory design space mapping and adaptation across sensory channels.
- **Deaf accessibility:** Addresses accessibility for deaf and hearing impaired users, expanding beyond visual impairment focus common in accessibility research.
- **Semiotic analysis:** Applies semiotic theory (iconic, indexical, symbolic signs) to icon design, informing theoretical foundation for metaphor and representation in adaptive UI design.
- **Evaluation methodology:** Provides example of user‑centered evaluation with deaf participants, relevant to thesis's methodology for validating adaptation approaches.
- **Limitations:** Focuses on desktop icons rather than mobile interfaces; does not address dynamic adaptation or hypertext models.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses multi‑modal interfaces and accessibility
- Thesis Sign16 project: Related to sign language representation research
- Design space connection: Visual → sign language/picture adaptation example
- User capability domain: Deafness as specific user capability profile

**Questions raised:**
- How could icon augmentation techniques be adapted for mobile devices with smaller screens and touch‑based interaction?
- What additional augmentation types are needed for users with combined impairments (e.g., deaf‑blind users)?
- How might semiotic analysis inform the design of adaptive metaphors across sensory modalities?
- Could sign language tooltips be integrated with the CISNA model's adaptation layer for dynamic content?

### ISO/IEC JTC 1 SC 36. (2005?). ISO/IEC 24751-1: Information technology for learning, education and training — Individualized adaptability and accessibility in e-learning, education and training — Part 1: Framework and reference model.

**File:** `referenced papers/metamodel/36N1024.pdf`

**Summary:**
ISO/IEC 24751‑1 standard providing a common framework and reference model for matching learner accessibility needs and preferences with appropriate learning resources and user interfaces in e‑learning, education, and training. Defines key terms including accessibility, adaptability, access modality, alternative access system, and digital resource. The multi‑part standard consists of: Part 1 (Framework and Reference Model), Part 2 ("AccessForAll" Personal Needs and Preferences for digital delivery), and Part 3 ("AccessForAll" Digital Resource Description). The framework encompasses two complementary sets of information: description of learner's accessibility needs/preferences and description of digital resource accessibility characteristics. Aims to facilitate discovery and use of the most appropriate content components for each user without being judgmental about resource flaws. Based on IMS specifications and designed for interoperability across standards communities (Dublin Core, IEEE LOM, etc.).

**Thesis Relevance:**
- **Standards‑based accessibility framework:** Provides an international standard for accessibility and adaptability frameworks, relevant to thesis's need for formal, interoperable approaches to adaptation.
- **Reference model structure:** Offers a structured reference model for matching user needs with resources, analogous to thesis's adaptation framework mapping user capability to device capacity.
- **Terminology standardization:** Defines standardized terminology (accessibility, adaptability, access modality) that could inform thesis's glossary and conceptual definitions.
- **Interoperability focus:** Emphasizes interoperability and consistent implementation, relevant to thesis's goal of creating widely applicable adaptation frameworks.
- **Limitations:** Focuses on e‑learning/education context rather than general mobile device accessibility; framework is descriptive rather than prescriptive for implementation.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses accessibility frameworks and standards
- Thesis Glossary: potential alignment with standardized terminology
- Model connection: ISO reference model vs. thesis's adaptation framework across user, device, content, context domains
- Standards relevance: Demonstrates international standards approach to accessibility adaptation

**Questions raised:**
- How could the ISO 24751 framework be extended or adapted for mobile device accessibility beyond e‑learning contexts?
- What additional concepts are needed in the reference model to handle real‑time adaptation (vs. resource discovery)?
- How might the "AccessForAll" approach inform the CISNA model's adaptation layer and action language?
- Could the standardized terminology improve interoperability between different adaptation systems?

---

### Nylander, S., Bylund, M., & Waern, A. (2004?). Ubiquitous service access through adapted user interfaces on multiple devices. *Personal and Ubiquitous Computing, 9*(5-6), 20–29.

**File:** `referenced papers/root/779_2004_Article_317.pdf`

**Summary:**
Presents the Ubiquitous Interactor (UBI) framework for device‑independent service access through adapted user interfaces. The system separates user‑service interaction from presentation, allowing services to adapt their user interfaces to diverse devices. Uses "interaction acts" (input, output, select, modify, create, destroy, start, stop) as abstract interaction units that can be rendered differently per device. Includes device profiles and customisation forms enabling UI adaptation to device capabilities and user preferences. Case studies: calendar and stock‑ticker services.

**Thesis Relevance:**
- **Device‑agnostic UI adaptation:** Demonstrates a framework for generating device‑tailored UIs from abstract interaction descriptions, relevant to CISNA's goal of device‑independent adaptation.
- **Interaction‑act paradigm:** Shows how abstract interaction units can be implemented as concrete UI widgets, informing CISNA’s adaptation‑layer operations.
- **Multi‑device context:** Addresses a core thesis challenge: delivering the same content/functionality across devices with different constraints.
- **Limitations:** Focuses on cross‑device consistency, not accessibility or impairment‑specific adaptations.

**Cross‑references:**
- Thesis Chapter 4 (UI Modelling): model‑based UI generation
- CISNA adaptation layer: mapping abstract interactions to concrete UIs
- Mobile‑device context: adapting to screen, input, processing constraints

**Questions raised:**
- How could “interaction acts” be extended to support accessibility‑driven adaptations (e.g., replace graphical output with speech for visually impaired users)?
- Could interaction‑act mappings be defined in CISNA’s adaptation‑rule language?
- How to ensure UIs generated from a common interaction model are equally usable on all target devices?
- Could the UBI framework be extended to incorporate user‑capability profiles (sensory, motor, cognitive)?

### SIGACCESS Newsletter (January 2006). SIGACCESS Newsletter, (84), January 2006.

**File:** `Jan06_all.pdf`

**Summary:**
The January 2006 issue of the ACM SIGACCESS Newsletter (Issue 84) features short contributions from the 2004 ASSETS Doctoral Consortium. The newsletter contains several accessibility‑research summaries including personal‑information‑management approaches for users with low vision (Brown & Robinson), CSS‑based web‑accessibility techniques, vision‑enhancement algorithms for refractive‑error correction, mobile‑health monitoring guidelines for older adults, haptic interfaces for blind users, conversational‑audio interfaces, heuristic evaluation of screen‑reader learnability, and robust text‑entry methods. The issue represents the state‑of‑the‑art in accessible‑computing research ca. 2005‑2006.

**Thesis Relevance:**
- **Historical perspective:** Provides a snapshot of the accessible‑computing field just before mobile/ubiquitous access became mainstream, offering a historical baseline for thesis context.
- **Multimodal design examples:** Demonstrates how accessibility can be realized across sensory modalities (visual, auditory, haptic).
- **Early‑stage research format:** Shows how doctoral‑level research in accessibility is framed, designed, and communicated.
- **User‑centered validation:** Most contributions include some form of user‑centered evaluation, providing examples of how adaptation techniques can be validated.

**Cross‑references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – many of the described systems could be mapped to CISNA's five‑layer model.
- Chapter 2: "Design Spaces" – the articles collectively illustrate multi‑sensory design‑space concepts in practice.
- Chapter 5: "Usability & Evaluation" – provides examples of empirical validation methods.

**Questions raised:**
- How have these 2006‑era solutions evolved with today's mobile/wearable platforms?
- Could a unified adaptation model like CISNA accelerate progress across diverse accessibility domains?
- What enduring lessons can be drawn from the research questions asked in 2005‑2006?

### Trewin, S., Keates, S., & Moffatt, K. (2006). Developing Steady Clicks: A Method of Cursor Assistance for People with Motor Impairments. In *Proceedings of the 8th International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS '06)* (pp. 26-33). ACM.

**File:** `referenced papers/p26-trewin.pdf`

**Summary:**
Presents "Steady Clicks," an assistance feature designed to help mouse users with motor impairments who experience slipping while clicking and accidental clicks. The system suppresses these errors by freezing the cursor during mouse clicks, preventing overlapping button presses, and suppressing clicks made while the mouse is moving at high velocity. The paper describes an empirical study with older adults and people with Parkinson's Disease that identified specific clicking problems, then evaluates Steady Clicks with eleven target users who have various motor impairments. Results show that Steady Clicks enabled participants to select targets using significantly fewer attempts, with overall task performance times significantly improved for the five participants with the highest slip rates. Nine of eleven participants preferred Steady Clicks to the unassisted condition.

**Thesis Relevance:**
- **Motor impairment adaptation:** Directly addresses adaptation for users with motor impairments, a key user capability domain in the thesis's adaptation framework.
- **Error suppression techniques:** Demonstrates practical techniques for suppressing specific error types (slips, accidental clicks, overlapping presses), informing adaptation rule design for motor-impaired users.
- **Empirical validation:** Provides example of empirical evaluation with target user population (people with motor impairments), relevant to thesis's methodology for validating adaptation approaches.
- **Real-time adaptation:** Implements real-time adaptation based on cursor velocity and button state, demonstrating feasibility of runtime adaptation decisions.
- **Limitations for critique:** Focuses specifically on mouse clicking rather than broader mobile device interaction; adaptation is limited to cursor/clicking behavior rather than comprehensive UI adaptation; does not address hypertext models or multi-sensory adaptation.

**Cross-references:**
- Thesis Chapter 3: "Capability Modelling & User Constraints" – motor impairment as specific user capability profile
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses adaptive input techniques
- Thesis Chapter 5: "Usability & Simulation Experiences" – could reference evaluation methodology
- User capability domain: Motor impairments and clicking strategies
- Adaptation technique: Error suppression vs. transformation across design spaces

**Questions raised:**
- How could Steady Clicks techniques be adapted for touchscreen mobile devices where traditional mouse clicking doesn't apply?
- What additional adaptation mechanisms are needed for users with combined motor and sensory impairments?
- How might error suppression techniques be integrated with the CISNA model's adaptation layer for comprehensive UI adaptation?
- Could velocity-based adaptation thresholds be personalized based on individual user capability profiles?

### Ramakrishnan, I. V., Stent, A., & Yang, G. (2004). HearSay: Enabling Audio Browsing on Hypertext Content. In *Proceedings of the 13th International Conference on World Wide Web (WWW '04)* (pp. 80-89). ACM.

**File:** `referenced papers/p80-ramakrishnan.pdf`

**Summary:**
Presents HearSay, a system for browsing hypertext web documents via audio, designed primarily for visually impaired users. The system automatically transforms HTML documents into audio-browsable content through novel partitioning techniques that combine structural and semantic analysis. HearSay analyzes HTML DOM trees to identify semantically related units, organizes them into concept hierarchies (partition trees), and automatically generates VoiceXML dialogs for interactive audio navigation. The system addresses the challenge of information overload in traditional screen readers by allowing users to selectively listen to relevant document parts based on semantic structure. Evaluation shows effective partitioning of news websites and promising usability for audio browsing tasks.

**Thesis Relevance:**
- **Hypertext to audio transformation:** Demonstrates automatic transformation of visual hypertext (HTML) to auditory interfaces, directly relevant to multi-sensory design space mapping (visual → auditory).
- **Structural-semantic analysis:** Combines structural analysis (DOM tree patterns) with semantic analysis (ontologies, WordNet) to understand document organization, informing adaptation techniques for content understanding.
- **Automatic dialog generation:** Uses templates to generate VoiceXML dialogs from partition trees, showing automated interface generation from content analysis.
- **Accessibility for visual impairments:** Focuses on making web content accessible to blind/low-vision users, a core user capability domain.
- **Limitations for critique:** Focuses on HTML documents rather than general hypertext models; transformation is document-specific rather than model-based; does not address mobile device constraints or multi-modal adaptation.

**Cross-references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – auditory design space and semantic representation
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses hypertext accessibility and audio interfaces
- Model connection: HTML to VoiceXML transformation vs. CISNA model's adaptation between design spaces
- User capability domain: Visual impairment and auditory adaptation
- Adaptation technique: Structural-semantic analysis for content understanding

**Questions raised:**
- How could HearSay's partitioning techniques be adapted for dynamic web content (AJAX) common in modern web applications?
- What additional analysis is needed for mobile-optimized websites with different structural patterns?
- How might the structural-semantic analysis approach inform the CISNA model's understanding of content semantics for adaptation?
- Could VoiceXML dialog generation be generalized using the CISNA action language for broader adaptation scenarios?

### Hatala, M., Kalantari, L., Wakkary, R., & Newby, K. (2004). Ontology and Rule based Retrieval of Sound Objects. In *Proceedings of the 13th International Conference on World Wide Web (WWW '04)* (pp. 1045-1046). ACM.

**File:** `referenced papers/p1045-hatala.pdf`

**Summary:**
Proposes an ontology and rule-based approach for retrieving sound objects, focusing on creating "soundscapes" for various applications. The system uses semantic web technologies where sounds are annotated with metadata describing acoustic properties, semantic meaning, and contextual usage. An ontology defines concepts and relationships for sound classification, while rules enable intelligent retrieval based on user queries and context. The approach aims to support applications such as audio-enhanced learning environments, accessible interfaces, and multimedia presentations by providing structured access to sound resources. The paper discusses the conceptual framework and potential applications of semantic sound retrieval.

**Thesis Relevance:**
- **Semantic sound representation:** Uses ontologies to represent sound properties and meanings, relevant to formal representation of sensory properties in design spaces.
- **Rule-based retrieval:** Implements rule-based reasoning for sound selection, connecting to thesis's use of rule-based adaptation in the CISNA model.
- **Soundscape creation:** Addresses composition of auditory environments, relevant to multi-sensory design and adaptation across sensory modalities.
- **Semantic web approach:** Applies semantic web technologies (ontologies, rules) to accessibility and multi-sensory design, demonstrating formal approaches that could inform thesis methodology.
- **Limitations:** Focuses on sound retrieval rather than real-time adaptation; conceptual paper with limited implementation details; does not address integration with visual or haptic modalities.

**Cross-references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – auditory design space and semantic representation of sensory properties
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses ontology-based approaches and rule-based systems
- Model connection: Sound ontology vs. CISNA model's representation of design space properties
- Adaptation relevance: Rule-based sound selection vs. adaptation rule execution in CISNA action language

**Questions raised:**
- How could this ontology and rule-based approach be extended to support real-time adaptation decisions in mobile accessibility systems?
- What additional ontological concepts are needed to represent relationships between visual, auditory, and haptic properties for cross-modal adaptation?
- How might sound retrieval rules be integrated with the CISNA model's action language for comprehensive multi-sensory adaptation?
- Could this approach support personalized sound selection based on user capability profiles (e.g., hearing impairments, cognitive preferences)?

### Schmandt, C., & Vallejo, G. (2003). Audio Hallway: A Virtual Acoustic Environment for Browsing. In *Proceedings of the 16th Annual ACM Symposium on User Interface Software and Technology (UIST '03)* (pp. 163-164). ACM.

**File:** `referenced papers/p163-schmandt.pdf`

**Summary:**
Presents Audio Hallway, a virtual acoustic environment that allows users to browse audio content spatially using a hallway metaphor. The system creates a metaphorical "hallway" where different audio sources (radio stations, podcasts, music collections) are represented as rooms or doors along the hallway. Users navigate this space using spatial audio cues, moving forward/backward and selecting audio sources based on position. The interface provides intuitive browsing of large audio collections without visual display, using only auditory feedback. The paper discusses implementation details, user interaction techniques, and potential applications for visually impaired users or eyes-free interaction scenarios. Audio Hallway demonstrates how spatial audio and metaphor can create navigable auditory interfaces.

**Thesis Relevance:**
- **Spatial audio interfaces:** Demonstrates use of spatial audio for navigation and browsing, relevant to auditory design space and spatial adaptation techniques.
- **Metaphor-based design:** Uses hallway/room metaphor for organizing content, connecting to thesis's discussion of metaphor in adaptive UI design.
- **Eyes-free interaction:** Addresses interaction without visual display, important for mobile devices (glanceable interfaces) and users with visual impairments.
- **Audio-only browsing:** Provides example of comprehensive audio interface, informing adaptation techniques for visual → auditory transformation.
- **Limitations:** Focuses on audio content browsing rather than general UI adaptation; short paper with limited evaluation; does not address integration with visual or haptic modalities.

**Cross-references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – spatial audio, auditory metaphors, eyes-free interaction
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses non-visual interfaces and spatial navigation
- Design space connection: Auditory spatial substrate and navigation techniques
- User capability domain: Visual impairment and auditory adaptation
- Metaphor relevance: Hallway metaphor as spatial organization technique

**Questions raised:**
- How could Audio Hallway concepts be adapted for mobile devices with limited audio spatialization capabilities?
- What additional navigation techniques are needed for complex hierarchical content structures beyond linear hallways?
- How might spatial audio browsing be combined with tactile feedback for users with combined visual and hearing impairments?
- Could the hallway metaphor be extended to support multi-sensory browsing (visual + auditory + haptic representations)?

### Brewster, S. A., & Ramloll, R. (2002). Enhancing Scanning Input with Non-Speech Sounds. In *Proceedings of the 4th International ACM Conference on Assistive Technologies (ASSETS '00)* (pp. 10-17). ACM.

**File:** `referenced papers/p770-brewster.pdf`

**Summary:**
Investigates the use of non-speech sounds to enhance scanning input interfaces for people with severe motor impairments. Scanning input is a temporal task where users press a switch when a cursor is over the required target, typically presented as items laid out in a spatial grid. The research shows that the auditory modality is often better than visual for temporal tasks, and proposes adding structured non-speech sounds (Earcons) to visual scanning systems. The paper demonstrates how natural rhythm perception abilities can support the scanning process, with preliminary results indicating feasibility. The work is part of the TIDE ACCESS Project aiming to create mobile communication devices for speech-motor and/or language-cognitive impaired users.

**Thesis Relevance:**
- **Multi-modal scanning interfaces:** Combines visual scanning with auditory feedback, directly relevant to multi-sensory design space mapping and adaptation across modalities.
- **Motor impairment adaptation:** Addresses severe motor impairments requiring alternative input methods, a key user capability domain.
- **Earcons and temporal cues:** Uses structured audio (Earcons) and rhythm for conveying temporal information, relevant to sonic design space and temporal adaptation.
- **Mobile assistive technology:** Part of project creating mobile communication devices for impaired users, aligning with thesis's mobile focus.
- **Limitations:** Focuses on scanning input rather than general UI adaptation; preliminary results rather than comprehensive evaluation; does not address hypertext models or semantic adaptation.

**Cross-references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses scanning interfaces and multi-modal feedback
- Thesis Chapter 5: "Usability & Simulation Experiences" – could reference evaluation methodology
- Mobile context: Directly addresses mobile communication devices for impaired users
- Design space connection: Visual scanning + auditory feedback adaptation
- User capability domain: Severe motor and speech-motor impairments

**Questions raised:**
- How could Earcons and rhythm-based cues be adapted for users with hearing impairments (e.g., through haptic/vibratory equivalents)?
- What is the cognitive load of simultaneous visual scanning and auditory feedback for users with cognitive impairments?
- How might this approach scale to complex mobile applications beyond simple scanning grids?
- Could rhythm-based auditory cues inform temporal sequencing in multi-sensory adaptations for users with different cognitive capabilities?

### Kobayashi, M., & Schmandt, C. (1997). Dynamic Soundscape: mapping time to space for audio browsing. In *Proceedings of the ACM SIGCHI Conference on Human Factors in Computing Systems (CHI '97)* (pp. 194-201). ACM.

**File:** `referenced papers/p194-kobayashi.pdf`

**Summary:**
Presents Dynamic Soundscape, an audio browsing system that maps temporal audio data to spatial locations for more efficient navigation. The system addresses the challenge of browsing audio (which is inherently temporal) by creating a spatial interface where "Speakers" (moving sound sources) orbit the user's head, playing different portions of a single audio recording simultaneously. Users can navigate by switching attention between multiple Speakers, using spatial memory to recall where specific topics were heard. The paper describes an iterative design process that refined Speaker motion speed, developed head-leaning interfaces for selective listening, and created interaction techniques like "grab-and-move" and "audio cursor" for precise control. Evaluation shows that spatial mapping helps users remember audio content locations and browse more efficiently than traditional linear playback.

**Thesis Relevance:**
- **Temporal to spatial mapping:** Demonstrates mapping of temporal audio data to spatial locations, relevant to adaptation across temporal and spatial design spaces.
- **Spatial audio navigation:** Uses spatialized audio for navigation and memory, connecting to auditory design space and spatial cognition in adaptation.
- **Simultaneous listening:** Implements "cocktail party effect" for selective attention among multiple audio streams, informing multi-sensory attention management in adaptive interfaces.
- **Iterative design methodology:** Shows systematic refinement of audio interface based on user testing, relevant to thesis's methodology for developing adaptation techniques.
- **Audio-only interaction:** Provides example of comprehensive audio interface without visual display, relevant to adaptation for visually impaired users.
- **Limitations:** Focuses on desktop audio browsing rather than mobile devices; complex hardware setup (head tracking, spatial audio); does not address integration with other sensory modalities.

**Cross-references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – spatial audio, temporal-spatial mapping, auditory design space
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses audio interfaces and spatial navigation
- Design space connection: Temporal audio → spatial auditory representation adaptation
- User capability domain: Visual impairment and auditory adaptation
- Methodology connection: Iterative design approach for refining adaptation techniques

**Questions raised:**
- How could Dynamic Soundscape concepts be adapted for mobile devices without head tracking or sophisticated spatial audio hardware?
- What additional challenges arise when mapping complex hierarchical audio content (not just linear recordings) to spatial representations?
- How might spatial audio navigation techniques inform adaptation of visual content for users with visual impairments?
- Could the "cocktail party effect" and selective listening techniques be applied to multi-modal attention management in complex adaptive interfaces?

### Lumbreras, M., & Sánchez, J. (1999). Interactive 3D Sound Hyperstories for Blind Children. In *Proceedings of the ACM SIGCHI Conference on Human Factors in Computing Systems (CHI '99)* (pp. 318-325). ACM.

**File:** `referenced papers/p318-lumbreras.pdf`

**Summary:**
Presents AudioDoom, an interactive 3D sound hyperstory system designed for blind children aged 8-12. The system creates acoustic virtual worlds where children navigate through spatialized sound environments, interact with virtual objects and characters, and engage in narrative-driven adventures. AudioDoom uses a "hyperstory" model combining navigable virtual worlds, dynamic objects, characters, and narrative plots. Children interact using an ultrasonic joystick (The Owl) with 3 degrees of freedom, coordinating haptic input with spatial audio output. The research explores whether 3D sound navigable environments can create cognitive spatial structures in blind children's minds. Evaluation with seven blind children showed they could construct accurate mental models of the virtual environment using LEGO blocks, demonstrating spatial understanding through audio-only interaction.

**Thesis Relevance:**
- **Audio-only virtual environments:** Demonstrates comprehensive virtual environments using only spatial audio, relevant to adaptation for visual impairments.
- **Hyperstory model:** Presents a structured approach to interactive narratives in virtual environments, connecting to hypermedia/hypertext models and adaptation frameworks.
- **Haptic-audio correlation:** Combines ultrasonic joystick input with spatial audio output, showing multi-modal interaction design for blind users.
- **Spatial cognition development:** Investigates how audio interfaces can develop spatial understanding in blind children, relevant to cognitive adaptation techniques.
- **Educational entertainment (edutainment):** Addresses both learning and entertainment needs of blind children, showing adaptive systems can serve multiple purposes.
- **Limitations:** Focuses on specific age group (8-12 year old blind children); uses specialized hardware (ultrasonic joystick); does not address integration with visual interfaces or mobile devices.

**Cross-references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – auditory design space, spatial audio, virtual environments
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses audio interfaces and accessibility for blind users
- Thesis Chapter 3: "Capability Modelling & User Constraints" – visual impairment as user capability domain
- Model connection: Hyperstory model vs. hypertext/hypermedia models (Dexter/Amsterdam)
- User capability domain: Blind children and spatial cognition development

**Questions raised:**
- How could the hyperstory model be integrated with the CISNA adaptation framework for dynamic content adaptation?
- What additional adaptation mechanisms are needed for users with combined visual and hearing impairments?
- How might the haptic-audio correlation techniques be adapted for standard mobile device interfaces (touchscreens, vibration)?
- Could the spatial cognition development approach inform adaptation techniques for users with cognitive impairments?

### Suryanarayana, L., & Hjelm, J. (2002). Situation-aware applications on the World Wide Web. In *Proceedings of the 11th International Conference on World Wide Web (WWW '02)* (pp. 200-209). ACM.

**File:** `referenced papers/p200-suryanarayana.pdf`

**Summary:**
Presents a profiles-based architecture for situation-aware web applications that adapt content, interaction, and presentation based on user context. Distinguishes between customized (device capabilities), personalized (user preferences), and situated (immediate environment) applications. Introduces key concepts: user profiles (personal facts, device capabilities, situation data, permission preferences), application profiles (content metadata), and rules for processing profiles. Uses CC/PP (Composite Capabilities/Preferences Profile) framework with RDF/XML for profile representation. Discusses transport mechanisms (HTTP headers, SOAP), processing models (rules engines, XSLT transformations), and trust/privacy considerations. Argues that trusted frameworks with rich vocabularies describing users, applications, and processing rules are critical for situated web architectures.

**Thesis Relevance:**
- **Situation-aware adaptation framework:** Provides comprehensive framework for context-aware adaptation across content, interaction, and presentation dimensions, directly relevant to thesis's adaptation framework.
- **Profiles-based architecture:** Distinguishes user profiles (capabilities, preferences, situation) from application profiles (content metadata), informing user capability and device capacity modeling.
- **CC/PP framework:** Uses standardized profile framework (CC/PP) with RDF/XML representation, relevant to thesis's need for formal profile representations.
- **Mobile context awareness:** Specifically addresses mobile devices and location-based services, connecting to thesis's focus on mobile accessibility.
- **Trust and privacy considerations:** Discusses critical issues of profile security, integrity, and privacy in adaptive systems.
- **Limitations:** Focuses on web applications rather than general mobile UI; conceptual framework with limited implementation details; does not address impairment-specific adaptations.

**Cross-references:**
- Thesis Chapter 3: "Capability Modelling & User Constraints" – user profiles and context modeling
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses context-aware systems and adaptation frameworks
- Thesis Chapter 6: "Hypertext Models & Adaptation" – connects to web-based adaptation approaches
- Model connection: CC/PP profile framework vs. thesis's user capability and device capacity models
- Mobile context: Directly addresses mobile devices and location-based adaptation

**Questions raised:**
- How could the CC/PP framework be extended to include impairment-specific user capability profiles?
- What additional profile elements are needed for multi-sensory adaptation across design spaces?
- How might situation-aware adaptation rules be integrated with the CISNA model's action language?
- Could the trust/privacy framework be adapted for sensitive user capability data (e.g., medical impairment information)?

### Jacobs, T., & Musial, B. (2003). Interactive Visual Debugging with UML. In *Proceedings of the ACM Symposium on Software Visualization* (pp. 115-122). ACM.

**File:** `referenced papers/p115-jacobs.pdf`

**Summary:**
Presents an interactive visual debugging system that links dynamic program execution state to Unified Modeling Language (UML) object diagrams. The system addresses the cognitive challenges of software debugging by providing visual representations that facilitate comprehension of overall application behavior alongside detailed understanding of specific components. It enhances standard UML diagrams with focus+context techniques, graph layout algorithms, and color encoding to organize and present objects and events in ways that support system behavior analysis. The approach allows debugging using high-level design abstractions while maintaining access to low-level details through interactive displays. The system extracts execution state from Java programs using the Java Platform Debug Architecture and visualizes it through modified UML diagrams in ArgoUML, applying degree-of-interest transformations and selective aggregation to handle large-scale systems.

**Thesis Relevance:**
- **Visual representation of system state:** Demonstrates how visual techniques can represent complex system states and behaviors, relevant to visualizing adaptation processes in the CISNA model.
- **Focus+context techniques:** Uses degree-of-interest transformations to manage information complexity, informing adaptation techniques for managing cognitive load in adaptive interfaces.
- **UML as modeling language:** Shows practical application of UML for system representation, connecting to thesis's use of modeling languages (Shlaer-Mellor, UML) for adaptation specification.
- **Multi-level abstraction:** Provides simultaneous access to high-level overviews and low-level details, relevant to adaptation across different granularity levels.
- **Cognitive support for complex tasks:** Addresses cognitive challenges in complex system understanding, informing adaptation techniques for users with cognitive impairments.
- **Limitations:** Focuses on software debugging rather than UI adaptation; does not address accessibility or multi-sensory design spaces; specialized for Java programming environment.

**Cross-references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses modeling approaches and visual representations
- Thesis methodology: Use of modeling languages (UML, Shlaer-Mellor) for system specification
- Cognitive aspects: Managing complexity and cognitive load in adaptive systems
- Model connection: Visual representation techniques vs. CISNA model visualization needs

**Questions raised:**
- How could visual debugging techniques be adapted to visualize adaptation processes in the CISNA model?
- What additional visual representations are needed for multi-sensory adaptation across design spaces?
- How might focus+context techniques inform adaptation of content presentation for users with cognitive impairments?
- Could UML-based visualization approaches be extended to represent user capability profiles and adaptation rules?

### More, G., Yuille, J., Padgham, L., Sahani, A., & Burry, M. (2003). The Space and Sound of Intelligent Information Environments. In *Proceedings of the Australian Conference on Computer-Human Interaction (OZCHI '03)* (pp. 15-19). ACM.

**File:** `referenced papers/p15-more.pdf`

**Summary:**
Presents Eureka, a Multi-Dimensional Presentation Environment (MPE) prototype that combines digital information spaces with spatial sound and intelligent agent support. Eureka is described as a "spatially adaptive hypermedia" system that allows users to arrange image-based information in 3D space for presentation scenarios, moving beyond linear slide sequences. The system features: (1) spatial navigation through 3D information spaces with different modes (library, history, presentation), (2) integrated spatial sound design using Max/MSP for navigation feedback and content representation, and (3) intelligent BDI (Belief-Desire-Intention) agents that monitor presentation timing and dynamically suggest content adjustments. The sound design applies electroacoustic composition strategies, using concepts like "reduced listening" and spatial sound objects to represent information hierarchies. Intelligent agents analyze XML-based presentation plans, monitor timing deviations, and suggest content deletions/additions to fit within scheduled time, communicating via PDA.

**Thesis Relevance:**
- **Spatially adaptive hypermedia:** Combines adaptive hypermedia with spatial organization, connecting to thesis's hypertext/hypermedia models and spatial adaptation techniques.
- **Multi-sensory integration:** Integrates visual spatial presentation with spatial sound design, relevant to multi-sensory design space mapping and cross-modal adaptation.
- **Intelligent agent adaptation:** Uses BDI agents for real-time adaptation based on context (timing, user behavior), informing rule-based adaptation approaches in CISNA model.
- **3D information spaces:** Demonstrates spatial organization of content beyond linear structures, relevant to spatial cognition and navigation adaptation.
- **XML-based representation:** Uses XML for presentation plans and agent reasoning, connecting to thesis's use of XML for adaptation rule representation.
- **Limitations:** Focuses on presentation software rather than general UI adaptation; complex system requiring specialized hardware (multi-channel audio, PDA); limited evaluation of effectiveness.

**Cross-references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – spatial design, multi-sensory integration, auditory design space
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses adaptive hypermedia and intelligent systems
- Thesis Chapter 6: "Hypertext Models & Adaptation" – connects to adaptive hypermedia concepts
- Model connection: BDI agent reasoning vs. CISNA adaptation rule execution
- Design space connection: Visual spatial + auditory spatial integration

**Questions raised:**
- How could Eureka's spatial sound techniques be adapted for accessibility (e.g., auditory navigation for visually impaired users)?
- What additional agent reasoning capabilities are needed for impairment-specific adaptation (beyond timing adjustments)?
- How might 3D spatial organization concepts inform adaptation of content for users with different cognitive spatial abilities?
- Could the BDI agent architecture be integrated with the CISNA model's adaptation layer for comprehensive multi-domain adaptation?

### Tsingos, N., Gallo, E., & Drettakis, G. (2004). Perceptual Audio Rendering of Complex Virtual Environments. In *Proceedings of the ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games (I3D '04)* (pp. 249-258). ACM.

**File:** `referenced papers/p249-tsingos.pdf`

**Summary:**
Presents a real-time 3D audio rendering pipeline for complex virtual scenes containing hundreds of moving sound sources. The approach combines auditory culling (eliminating inaudible sources based on psychoacoustic masking) with spatial level-of-detail clustering to handle more than ten times the number of sources available on consumer 3D audio hardware. The method dynamically eliminates inaudible sources using binaural masking models and groups remaining audible sources into a budget number of clusters, each represented by an "impostor" sound source positioned using perceptual criteria. Spatial audio processing is then performed only on the impostor sources rather than every original source, greatly reducing computational cost. The system includes pre-processing of audio signals to extract spectral features (power spectrum distribution, tonality index) used for perceptual saliency estimation. Evaluation shows the approach works well for both indoor and outdoor environments with minimal decrease in audio quality and limited localization impairment.

**Thesis Relevance:**
- **Perceptual audio rendering:** Uses psychoacoustic principles (masking, saliency) to optimize audio processing, relevant to efficient multi-sensory adaptation.
- **Auditory culling and clustering:** Demonstrates techniques for managing complexity in multi-source audio environments, informing adaptation strategies for complex sensory scenes.
- **Real-time performance optimization:** Shows how perceptual models can enable real-time processing of complex sensory data, relevant to mobile device constraints.
- **Spatial audio level-of-detail:** Applies LOD concepts to audio rendering, similar to visual LOD techniques, connecting to multi-level adaptation approaches.
- **Cross-modal considerations:** Discusses interaction between audio and visual rendering, relevant to multi-sensory integration in adaptive interfaces.
- **Limitations:** Focuses on audio rendering for virtual environments rather than accessibility; technical paper with emphasis on performance optimization; does not address impairment-specific adaptations.

**Cross-references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – auditory design space, perceptual models, spatial audio
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses audio rendering and performance optimization
- Thesis mobile context: Performance optimization for resource-constrained devices
- Design space connection: Perceptual optimization across sensory modalities
- Methodology connection: Use of psychoacoustic models for efficient processing

**Questions raised:**
- How could auditory culling and clustering techniques be adapted for accessibility applications (e.g., prioritizing important audio cues for users with hearing impairments)?
- What additional perceptual models are needed for impairment-specific audio adaptation (e.g., frequency shifting for hearing loss)?
- How might spatial audio LOD concepts inform adaptation of visual content for users with visual impairments?
- Could the perceptual saliency estimation approach be extended to multi-sensory importance weighting in adaptive interfaces?

### Aoki, P. M., Romaine, M., Szymanski, M. H., Thornton, J. D., Wilson, D., & Woodruff, A. (2003). The Mad Hatter's Cocktail Party: A Social Mobile Audio Space Supporting Multiple Simultaneous Conversations. In *Proceedings of the ACM SIGCHI Conference on Human Factors in Computing Systems (CHI '03)* (pp. 425-432). ACM.

**File:** `referenced papers/p425-aoki.pdf`

**Summary:**
Presents "The Mad Hatter's Cocktail Party," a mobile audio space designed for social groups that supports multiple simultaneous conversations through automatic floor management. The system monitors participant turn-taking behavior using machine learning (Naïve Bayes classifier) to identify conversational floors as they emerge, then dynamically modifies audio delivery to enhance the salience of participants in the same conversational floor while reducing the salience of those in different floors. Unlike conventional audio spaces that require explicit floor specification or present all participants at equal volume, this system automatically detects conversational groupings based on temporal features (TRP positioning, simultaneous speech). Evaluation through conversation analysis shows that automatic audio enhancements effectively facilitate multiple simultaneous conversations, though incorrect inferences require repair strategies. The system runs on handheld computers with wireless networking, providing toll-quality audio with 150ms latency.

**Thesis Relevance:**
- **Social mobile audio spaces:** Addresses social communication needs in mobile contexts, relevant to thesis's focus on mobile accessibility and social interaction.
- **Automatic floor management:** Uses machine learning to detect conversational structures, informing adaptation techniques for social interaction patterns.
- **Conversation analysis methodology:** Applies conversation analytic methods to evaluate system effectiveness, demonstrating rigorous evaluation approaches for adaptive systems.
- **Audio salience adaptation:** Dynamically adjusts audio volume based on conversational context, showing real-time adaptation based on interaction patterns.
- **Mobile implementation:** Runs on handheld devices with wireless networking, demonstrating feasibility for mobile adaptive systems.
- **Social group dynamics:** Focuses on gelled social groups and their communication patterns, relevant to social aspects of accessibility.
- **Limitations:** Focuses on able-bodied social communication rather than accessibility; requires training data for machine learning; does not address impairment-specific adaptations.

**Cross-references:**
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses audio communication systems and social interaction support
- Thesis mobile context: Directly addresses mobile audio communication systems
- Methodology connection: Conversation analysis as evaluation method for adaptive systems
- Social aspects: Addresses social group communication patterns relevant to social inclusion
- Adaptation technique: Real-time audio adaptation based on conversational context

**Questions raised:**
- How could automatic floor management techniques be adapted for users with hearing impairments (e.g., prioritizing certain speakers or frequency ranges)?
- What additional features would be needed to support users with speech impairments in conversational floor detection?
- How might the conversation analysis methodology inform evaluation of adaptive systems for users with communication impairments?
- Could the social audio space concept be extended to support multi-sensory social interactions for users with different sensory capabilities?

### Cavarra, A., Riccobene, E., & Scandurra, P. (2003). A Framework to Simulate UML Models: Moving from a Semi-formal to a Formal Environment. In *Proceedings of the ACM Symposium on Applied Computing (SAC '03)* (pp. 1519-1526). ACM.

**File:** `referenced papers/p1519-cavarra.pdf`

**Summary:**
Presents a simulation framework for UML models based on mapping UML metamodel elements into Abstract State Machines (ASMs). The approach translates structural model elements (classes, relationships) into ASM vocabulary as domains and functions, while dynamic behavior (state machines) is captured by multi-agent ASMs. The toolkit takes UML models from CASE tools in XMI format, automatically initializes the ASM model, and executes it symbolically using the AseGofer ASM programming system. The framework supports class diagrams, object diagrams, state diagrams, and sequence diagrams, with the stack-printer case study demonstrating simulation of interactions among state machines through signal exchange and operation calls. The work addresses the lack of precise semantics in UML by providing a formal executable semantics through ASMs, enabling model validation, verification, and early error detection.

**Thesis Relevance:**
- **Formal modeling of UML:** Provides formal semantics for UML models using Abstract State Machines, relevant to thesis's use of modeling languages (UML, Shlaer-Mellor) for adaptation specification.
- **Model simulation and validation:** Enables simulation of behavioral models for validation and verification, informing approaches for validating adaptation rules and behaviors.
- **Multi-agent ASMs:** Uses multi-agent ASMs to model concurrent behavior, connecting to distributed adaptation approaches and multi-user scenarios.
- **XMI-based tool integration:** Uses standard XMI format for tool interoperability, relevant to thesis's need for standardized model representations.
- **Formal verification foundation:** Provides basis for formal verification of models, informing approaches for verifying adaptation rule correctness.
- **Model-driven development:** Supports model-driven approach from semi-formal UML to formal ASM specifications, relevant to thesis's model-driven adaptation framework.
- **Limitations:** Technical paper focused on UML simulation rather than accessibility; does not address adaptive systems or user interface concerns; specialized formal methods approach.

**Cross-references:**
- Thesis methodology: Use of modeling languages (UML, Shlaer-Mellor) for system specification
- Thesis Chapter 4: "User Interface Modelling & Assistive Technology" – discusses modeling approaches and formal methods
- Model connection: Formal semantics for behavioral models vs. CISNA adaptation rule semantics
- Tool integration: XMI-based approach for tool interoperability

**Questions raised:**
- How could the UML-to-ASM mapping approach be extended to model adaptation rules in the CISNA framework?
- What additional formal semantics are needed for modeling multi-sensory adaptation across design spaces?
- How might model simulation techniques inform validation of adaptation behaviors for users with different capabilities?
- Could the multi-agent ASM approach model distributed adaptation across multiple devices or users?

### Nesbitt, K. V. (2001). Modeling the Multi-Sensory Design Space. In *Proceedings of the Australian Symposium on Information Visualisation* (pp. 27-36). Australian Computer Society.

**File:** `referenced papers/p27-nesbitt.pdf`

**Summary:**
Presents a comprehensive framework for modeling the multi-sensory design space by extending Card and Mackinlay's visual design space taxonomy to include auditory and haptic displays. The paper introduces a unified model where visual, auditory, and haptic structures share common components: spatial substrate, marks, properties, and temporal encoding. It uses UML notation to model these components across sensory modalities. The framework distinguishes between "direct properties" (perceptually direct encodings requiring automatic processing) and "abstract properties" (requiring controlled cognitive processing). The paper also correlates this extended design space with a metaphor-based classification, identifying nine metaphor categories (visual spatial, visual temporal, sight, auditory spatial, auditory temporal, sound, haptic spatial, haptic temporal, touch). The work provides a foundation for systematic design of multi-sensory information displays (perceptualization) that can represent abstract, multivariate data.

**Thesis Relevance:**
- **Multi-sensory design space framework:** Directly addresses thesis's core concept of multi-sensory design spaces for adaptation, providing a formal model for visual, auditory, and haptic modalities.
- **Unified sensory structure model:** Shows how visual, auditory, and haptic displays share common structural components (spatial substrate, marks, properties, temporal encoding), informing cross-modal adaptation approaches.
- **Direct vs. abstract properties:** Distinguishes between perceptually direct encodings (automatic processing) and abstract encodings (controlled processing), relevant to adaptation for users with different cognitive capabilities.
- **Metaphor-based classification:** Provides metaphor-based organization of design space, connecting to thesis's use of metaphors in adaptation.
- **UML modeling approach:** Uses UML notation for formal modeling, connecting to thesis's use of modeling languages.
- **Perceptualization concept:** Introduces "perceptualization" as multi-sensory display of abstract information, directly relevant to multi-sensory adaptation.
- **Limitations:** Focuses on information visualization/auditory/haptic displays rather than accessibility; does not address impairment-specific adaptations; conceptual framework without implementation.

**Cross-references:**
- Thesis Chapter 2: "Design Spaces & Metaphor" – directly addresses multi-sensory design spaces and metaphor classification
- Thesis core concept: Multi-sensory adaptation across design spaces
- Methodology connection: UML modeling of design spaces
- Sensory modalities: Visual, auditory, haptic design spaces
- Metaphor connection: Metaphor-based classification of design space

**Questions raised:**
- How could the multi-sensory design space framework be extended to include impairment-specific adaptations (e.g., alternative encodings for sensory impairments)?
- What additional components are needed to model cross-modal adaptation (mapping between sensory modalities)?
- How might the direct vs. abstract properties distinction inform adaptation for users with cognitive impairments?
- Could the metaphor classification guide the selection of appropriate adaptation metaphors for different user capabilities?

---

## Notes on Review Process

This bibliography will be built incrementally by reviewing each paper in the `referenced papers/` directory. Reviews focus on:
1. **What the paper says** (key contributions, methods, findings)
2. **Why it matters for the PhD** (theoretical foundation, critique source, validation)
3. **How it connects** (thesis chapters, models, publications)
4. **Questions it raises** (limitations, open issues, research gaps)

Total papers reviewed: 37 / ~255 (across 9 categories)
