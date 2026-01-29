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

---

## Notes on Review Process

This bibliography will be built incrementally by reviewing each paper in the `referenced papers/` directory. Reviews focus on:
1. **What the paper says** (key contributions, methods, findings)
2. **Why it matters for the PhD** (theoretical foundation, critique source, validation)
3. **How it connects** (thesis chapters, models, publications)
4. **Questions it raises** (limitations, open issues, research gaps)

Total papers reviewed: 18 / ~255 (across 9 categories)