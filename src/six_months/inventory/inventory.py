from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True)
class Item:
    id: str
    name: str
    description: str
    quantity: int = 1
    tags: frozenset[str] = frozenset()
    throwable: bool = False
    consumable: bool = False


@dataclass
class Inventory:
    items: dict[str, Item] = field(default_factory=dict)

    def add(self, item: Item, quantity: int = 1) -> None:
        if quantity < 1:
            raise ValueError("quantity must be positive")
        existing = self.items.get(item.id)
        if existing:
            self.items[item.id] = Item(
                id=existing.id,
                name=existing.name,
                description=existing.description,
                quantity=existing.quantity + quantity,
                tags=existing.tags,
                throwable=existing.throwable,
                consumable=existing.consumable,
            )
        else:
            self.items[item.id] = Item(
                id=item.id,
                name=item.name,
                description=item.description,
                quantity=quantity,
                tags=item.tags,
                throwable=item.throwable,
                consumable=item.consumable,
            )

    def remove(self, item_id: str, quantity: int = 1) -> Item:
        if quantity < 1:
            raise ValueError("quantity must be positive")
        item = self.items.get(item_id)
        if item is None or item.quantity < quantity:
            raise ValueError(f"Not enough of item: {item_id}")
        remaining = item.quantity - quantity
        if remaining:
            self.items[item_id] = Item(item.id, item.name, item.description, remaining, item.tags, item.throwable, item.consumable)
        else:
            del self.items[item_id]
        return item

    def has(self, item_id: str, quantity: int = 1) -> bool:
        return item_id in self.items and self.items[item_id].quantity >= quantity

    def __iter__(self) -> Iterable[Item]:
        return iter(self.items.values())
