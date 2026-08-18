# Six Months — Relationship System

## Purpose

Relationships are the game's central differentiating system. Major NPCs should feel like persistent people rather than dialogue dispensers.

## Relationship Model

A relationship is multidimensional. Planned dimensions include:

- Trust
- Respect
- Affection
- Fear
- Dependence
- Resentment

These values are primarily hidden from the player.

## Memory

Relationship state alone is insufficient. Major NPCs maintain memories of significant events.

A memory should be able to record:

- Event
- Date
- Participants
- Context
- Importance
- NPC interpretation
- Emotional impact
- Whether the NPC currently remembers it accurately

The system should distinguish between what happened and what an NPC believes happened.

## Emotional State

An NPC's current emotional state can temporarily modify how they behave. Examples include:

- Calm
- Afraid
- Angry
- Grieving
- Suspicious
- Relieved
- Exhausted
- Desperate

Emotional state is distinct from long-term relationship state.

## Relationships Between NPCs

Major NPCs can have relationships with one another. These can evolve without direct player involvement.

Examples:

- Trust
- Distrust
- Respect
- Rivalry
- Friendship
- Affection
- Fear
- Resentment
- Dependence

This creates a social network rather than a set of isolated NPC relationships.

## Relationship Effects

Actions and dialogue choices should produce contextual effects.

Examples:

- Keeping a promise may increase trust.
- Publicly defending someone may increase respect.
- Saving someone's life may dramatically increase trust or dependence.
- Lying may decrease trust if discovered.
- Repeated threats may increase fear while decreasing affection.
- Abandonment may cause severe resentment.

The same action can have different effects depending on the NPC's personality, beliefs, history, and interpretation.

## Dialogue Integration

Dialogue choices should express intent rather than morality labels.

A choice may specify:

- Intent
- Tone
- Truthfulness
- Target
- Subject
- Required skill
- Potential relationship effects
- Potential memory

The dialogue engine evaluates these properties against the current context.

## Long-Term Behavior

Relationship values and memories should influence future behavior such as:

- Willingness to cooperate
- Sharing information
- Sharing resources
- Following orders
- Offering help
- Defending the player
- Confronting the player
- Leaving the group
- Betraying the player

## Design Goal

The player should rarely see a message saying that a relationship changed. Instead, they should notice that a character behaves differently.

The desired player reaction is:

> "I think Sarah doesn't trust me anymore."

rather than:

> "Sarah lost 10 friendship points."
