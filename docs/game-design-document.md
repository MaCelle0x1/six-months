# Six Months — Game Design Document v0.1

## 1. Game Overview

**Genre:** Text-based survival RPG  
**Setting:** Contemporary Midwestern United States  
**Timeline:** Approximately six months  
**Platform:** Command line initially  
**Primary focus:** Relationships, survival, consequential choices, exploration, and character development.

*Six Months* is a grounded survival RPG beginning shortly before the collapse of society caused by a fictional, rapidly spreading neurological disease.

The player creates an ordinary person with their own background, skills, and life history. They begin alone in a Midwestern suburban environment and experience the outbreak from its earliest stages through the gradual breakdown of normal society.

The player is not assigned a predetermined heroic purpose. They decide what matters. They may become a protector, survivor, leader, criminal, caretaker, wanderer, opportunist, or something else entirely.

The game's defining feature is its deep relationship and social simulation system. Major characters remember what the player does, develop opinions about them, form relationships with other characters, and react to the player's behavior over time.

## 2. Design Pillars

### People Over Numbers
Relationships are more important than traditional RPG morality meters. The player should infer how characters feel through behavior, dialogue, decisions, and willingness to help.

### Grounded Survival
The setting remains recognizably realistic. There are no supernatural elements, fantasy races, magical abilities, or monsters. Violence is dangerous and consequential.

### The World Moves Without You
People make decisions, communities change, resources disappear, infrastructure fails, quests expire, and characters may act independently.

### Player Identity Emerges Through Play
The player begins as an ordinary person. Their identity develops through background, skills, abilities, choices, relationships, and survival strategy rather than a fixed class.

### Consequences Without Constant Punishment
Choices should matter without constantly announcing consequences. A decision made early can quietly matter much later.

## 3. Setting

The game takes place in the Midwestern United States, primarily around suburban communities. The exact geographical region will be determined during narrative development.

The regional map can contain suburbs, small cities, rural areas, farms, highways, hospitals, industrial areas, shopping centers, schools, residential neighborhoods, lakes, and government facilities.

The game uses a regional network of locations rather than attempting to simulate the entire United States.

## 4. The Disease

The outbreak is caused by a fictional, rapidly spreading prion-like neurological disease. It is not intended to represent an actual real-world prion disease.

Within the game's fiction, transmission can occur through aerosol exposure, saliva, blood, contaminated bodily fluids, and close contact.

The disease progresses through neurological and behavioral symptoms and ultimately can be fatal. Not everyone progresses at the same rate.

There are no supernatural zombies. Severely affected individuals remain human, although they may become extremely dangerous.

## 5. Timeline

The primary game covers approximately six months.

### Days 1–2: Normal Life
The player establishes their character and experiences ordinary life. The disease exists but remains background information.

### Days 3–5: Awareness
News coverage increases. Hospitals report unusual cases. People begin discussing the disease and supply shortages begin.

### Days 6–9: Concern
Schools and businesses begin closing. Hospitals become overwhelmed. Government warnings increase. Public behavior changes.

### Days 10–14: Breakdown
Police response becomes unreliable. Stores are increasingly empty. Power and communications begin experiencing problems. Communities begin organizing independently.

### Months 2–6: Collapse and Adaptation
Infrastructure deteriorates. Communities become isolated. People establish informal settlements and survival groups. The world becomes increasingly defined by local relationships and resources rather than traditional institutions.

## 6. Character Creation

The player creates a completely customizable protagonist. The protagonist initially begins alone to allow maximum narrative flexibility.

Character creation includes name, age, occupation/background, education, starting location, and relevant life history.

Background affects both mechanics and narrative. It can provide skills and knowledge and can occasionally unlock contextual dialogue or opportunities, but should not dominate every conversation.

## 7. Attributes

Six primary attributes are planned:

- **Might:** physical strength and force.
- **Agility:** coordination, speed, and reflexes.
- **Vitality:** health, stamina, and resilience.
- **Intellect:** reasoning, education, technical knowledge, and problem solving.
- **Awareness:** perception, instincts, and situational awareness.
- **Presence:** social confidence, communication, leadership, and interpersonal ability.

## 8. Skills

Skills are separate from attributes. Checks can combine an attribute, skill, and contextual modifiers.

Potential skills include:

- Athletics
- Melee
- Firearms
- Stealth
- Survival
- Scavenging
- First Aid
- Navigation
- Mechanics
- Electronics
- Persuasion
- Intimidation
- Deception
- Leadership
- Medicine
- Investigation
- Science

The final skill list will be established during implementation.

## 9. Character Development

There are no traditional character classes. Players develop through attributes, skills, abilities, equipment, experience, and decisions.

Emergent roles may include protector, medic, scout, leader, fighter, negotiator, survivor, scavenger, and opportunist.

Abilities and perks will be designed later around actual gameplay behavior rather than generic numerical bonuses.

## 10. Time System

Time advances day by day. Important days may be divided into morning, afternoon, and night. The game does not simulate every hour.

Time advances when meaningful activities occur. Important days generate more substantial encounters.

## 11. Core Gameplay Loop

**Time advances → world changes → encounter/conversation occurs → player makes decisions → relationships/world state/character state change → player chooses next action → repeat.**

Important encounters can include private conversations, injuries, confrontations, discoveries, rumors, supply opportunities, relationship events, new threats, and major decisions.

## 12. Quest System

Quests emerge naturally through conversations, rumors, observations, character requests, discoveries, and world events rather than traditional fetch-quest prompts.

Quests have an origin, objective, time constraints, conditions, possible outcomes, and consequences. Quests can expire without always displaying an explicit failure message.

## 13. World State

The world evolves naturally over time. Important variables may include disease prevalence, food availability, power reliability, communications, public order, police presence, infrastructure condition, and community stability.

World variables should not simply decrease linearly. Events influence them.

Locations have changing states. For example, a hospital might be operational but overwhelmed early in the outbreak, partially abandoned later, looted afterward, and eventually occupied by a survivor community.

## 14. Survival and Logistics

Survival should be meaningful without becoming tedious. General food, water, fuel, and supply availability can be represented by an abstract Logistics resource.

Specific important resources remain individually tracked, including ammunition and significant medical supplies.

## 15. Inventory

Inventory remains relatively simple. Weapons, ammunition, important medical supplies, and special items are explicitly tracked. General survival supplies are represented through Logistics.

## 16. Injuries

Injuries are persistent conditions rather than simple HP depletion. Examples include lacerations, broken limbs, and leg injuries. Injuries affect actions and can require treatment, rest, nutrition, and time to recover.

## 17. Combat

Combat is turn-based, short, dangerous, realistic, and consequential.

Potential actions include fire, aim, move, take cover, talk, threaten, flee, surrender, protect another character, use an item, attempt to disarm, and attempt to incapacitate.

Combat should simulate dangerous encounters rather than traditional RPG damage races. Position, weapon, accuracy, cover, injury, stress, awareness, distance, and decisions all matter.

A single successful shot can end a fight. A single mistake can end the player's life.

## 18. Stress

Stress represents the character's immediate psychological state during traumatic events. It is not a morality or sanity meter.

High stress may affect accuracy, decision-making, perception, dialogue, and certain actions. Characters respond differently based on personality and experience.

## 19. Dialogue System

Dialogue is a primary gameplay system. Important conversations provide meaningful choices based on intent rather than simple good/bad responses.

Possible intents include reassurance, questioning, lying, threatening, persuading, challenging, deflecting, remaining silent, and changing the subject.

The dialogue system should account for player attributes, skills, background, previous actions, NPC personality, relationship state, emotional state, circumstances, and NPC knowledge.

## 20. Relationship System

The relationship engine is the game's central differentiating feature.

Relationships are multidimensional and can include trust, respect, affection, fear, dependence, and resentment. These values are primarily hidden from the player and expressed through character behavior.

## 21. Relationship Changes

Relationships change through actions and conversations. Significant events have stronger effects than minor disagreements.

Potential relationship-changing actions include saving someone, abandoning someone, sharing supplies, stealing, killing, lying, protecting someone, keeping promises, and breaking promises.

## 22. NPC Memory

Major NPCs maintain memories of significant events. Memories contain what happened, when it happened, who was involved, and potentially how the NPC interpreted the event.

NPCs should remember why they feel a certain way rather than merely storing a numerical relationship score.

## 23. NPC Personalities

Major characters have personalities, goals, beliefs, fears, values, preferences, relationships, memories, and emotional states.

Two characters can witness the same player action and react differently. There is no universal morality meter dictating which reaction is correct.

## 24. NPC-to-NPC Relationships

Major characters maintain relationships with one another. These relationships can evolve independently of the player and can involve arguments, alliances, jealousy, distrust, loyalty, coalitions, and betrayals.

The player can influence these relationships intentionally or accidentally.

## 25. Communities

During the first six months, communities are small and organic rather than highly developed ideological factions. Examples include families, neighborhoods, apartment communities, farms, church groups, former coworkers, and small survivor settlements.

Their philosophies and structures can develop naturally as the world evolves.

## 26. Story Structure

The overarching narrative has not yet been finalized. The game should have a narrative spine while allowing the player's personal motivation to remain flexible.

Potential player goals include surviving, protecting others, finding someone, establishing a home, traveling elsewhere, helping a community, becoming a leader, remaining independent, pursuing knowledge about the disease, or simply staying alive.

## 27. Endings

The game should support multiple broad outcomes without requiring dozens of completely independent ending scripts.

Ending evaluation can consider community, relationships, reputation, personal goals, independence, moral behavior, survival, and who remains alive.

The ending should describe the player's specific six-month journey.

## 28. Save System

SQLite will provide persistent game storage. Saves should preserve the complete game state, including player data, inventory, equipment, injuries, quests, NPCs, relationships, memories, locations, world state, time, and major events.

## 29. Command-Line Interface

The initial game is entirely command-line based. The interface prioritizes readability and atmosphere.

Example:

```text
DAY 17 — EVENING
────────────────────────────────────────

You return to the house as the sun sets.

Sarah is sitting on the porch.

She looks like she's been waiting for you.

"We need to talk about Marcus."

────────────────────────────────────────

1. "What's wrong?"
2. "I don't want to talk about Marcus."
3. "Did he do something?"
4. Sit beside her silently.
5. Leave.

>
```

## 30. Technical Architecture

The game should separate its engine from its content. The engine handles mechanics; content defines characters, locations, dialogue, quests, encounters, and events.

The planned engine areas are:

- Game state
- Time
- World state
- Events
- Characters
- Attributes and skills
- Relationships
- Dialogue
- Combat
- Quests
- Inventory
- Injuries
- Persistence
- Terminal UI

### Architectural principle

**The engine should not know the story.**

The engine knows that a conversation can modify a relationship. Content defines that Sarah becomes angry if the player lies about medicine.

## 31. Development Roadmap

### Phase 1 — Foundation

- Repository
- Python project
- Basic game loop
- Command-line interface
- Game state
- SQLite database

### Phase 2 — Character

- Character creation
- Attributes
- Skills
- Backgrounds
- Inventory
- Equipment

### Phase 3 — World

- Time
- Locations
- Travel
- World state
- Logistics

### Phase 4 — Encounters

- Event system
- Basic dialogue
- Choices
- Quest tracking

### Phase 5 — Relationships

- NPC profiles
- Relationship variables
- NPC memory
- NPC emotional state
- NPC-to-NPC relationships

### Phase 6 — Combat

- Turn-based encounters
- Weapons
- Ammunition
- Injuries
- Stress
- Non-lethal options

### Phase 7 — Content

- Opening sequence
- Initial locations
- Major characters
- First quests
- Outbreak progression

### Phase 8 — Persistence

- Full save/load
- World-state persistence
- Quest persistence
- Relationship persistence

### Phase 9 — Playtesting

- Balance
- Narrative testing
- Relationship testing
- Edge cases
- Dead-end scenarios
- Exploit detection

### Phase 10 — Alpha/Beta

A complete beginning-to-end playable version comes before expanding the amount of content.

## 32. Definition of Complete

The first complete release should provide:

- Complete character creation
- A functional six-month timeline
- A coherent beginning-to-end story
- Multiple starting situations
- Functional combat
- Functional injuries
- Functional inventory/logistics
- Meaningful quests
- A sophisticated relationship system
- Persistent NPC memories
- Evolving world state
- Multiple meaningful outcomes
- Reliable save/load
- A polished command-line interface

A smaller complete game is preferable to an enormous unfinished one.

## 33. Design North Star

> **Who do you become when the world stops functioning normally?**

The player is not told to be a hero, ruthless, or who to save. They are given six months, a deteriorating world, a handful of people, and increasingly difficult choices.

**The game remembers what they do.**
