# Six Months — Technical Architecture

## Goal

Build a maintainable engine that can support a long-running, content-heavy text RPG without embedding story logic directly into gameplay code.

## Principles

1. Separate engine logic from narrative content.
2. Keep game state explicit and serializable.
3. Make major systems independently testable.
4. Prefer deterministic, inspectable rules over opaque behavior.
5. Avoid building systems that do not serve the game's core experience.

## Proposed Project Structure

```text
six-months/
├── src/
│   └── six_months/
│       ├── main.py
│       ├── engine/
│       │   ├── game.py
│       │   ├── time.py
│       │   ├── world.py
│       │   ├── events.py
│       │   └── state.py
│       ├── characters/
│       │   ├── character.py
│       │   ├── attributes.py
│       │   ├── skills.py
│       │   └── relationships.py
│       ├── dialogue/
│       │   ├── engine.py
│       │   ├── conditions.py
│       │   └── effects.py
│       ├── combat/
│       │   ├── engine.py
│       │   ├── weapons.py
│       │   └── injuries.py
│       ├── quests/
│       │   └── engine.py
│       ├── inventory/
│       │   └── inventory.py
│       ├── persistence/
│       │   ├── database.py
│       │   └── migrations.py
│       └── ui/
│           └── terminal.py
├── content/
│   ├── characters/
│   ├── locations/
│   ├── dialogue/
│   ├── quests/
│   ├── encounters/
│   └── events/
├── tests/
└── docs/
```

## Engine vs Content

Engine modules implement reusable rules. Content files describe specific game material.

For example, the relationship engine should expose an operation such as `apply_relationship_effect()`. It should not contain hard-coded knowledge of Sarah, Marcus, or any specific story event.

## Game State

The central game state should contain or reference:

- Current date and time segment
- Player state
- Character state
- Relationships
- Memories
- Locations
- World variables
- Active quests
- Inventory
- Equipment
- Injuries
- Major event history

The state must be serializable to SQLite.

## Event System

Events are the primary mechanism through which time and world changes produce gameplay.

An event should support:

- Conditions
- Priority
- Timing
- Presentation
- Player choices
- Effects
- Follow-up events

Events should be able to modify multiple systems at once while remaining testable.

## Content-Driven Dialogue

Dialogue should be represented as structured data rather than deeply nested Python conditionals.

A dialogue choice may contain:

- Text
- Intent
- Conditions
- Skill checks
- Effects
- Memory creation
- Relationship changes
- Follow-up dialogue
- Time cost

## Persistence

SQLite is the initial persistence layer. The database should be treated as an implementation detail behind a persistence interface so the storage implementation can change later if needed.

## Testing

Core simulation systems should have automated tests before significant narrative content is added.

Priority test areas:

- Time progression
- State serialization
- Relationship changes
- Memory creation/retrieval
- Dialogue conditions
- Quest expiration
- Combat resolution
- Injury effects
- World-state transitions

## Development Rule

Do not solve narrative problems with engine-specific hacks. If a story requirement cannot be expressed cleanly through the existing systems, improve the system rather than adding a one-off conditional wherever the problem occurs.
