# OOP in python

Python でオブジェクト指向を学ぶ

## Keywords

Abstraction: 抽象的な、ぼんやりした

Inheritance: 継承、受け継ぐ、引き継ぐ

Composition: 合成、（複数のものからひとつに）形を成す

Polymorphism: 多態性、複数の異なるオブジェクトが同一の行動を成せること

Encapsulation: カプセル化、データと処理を一つのクラスの中に閉じ込めておくこと

## 継承と合成

どちらを使うべきか

`inheritance/composition` は `is/has` の関係性であると言われる

たとえば、人間と戦士のクラスがあったとする

```python
class Person:
    name: str
    hp: int

# Person を継承
class Warrior(Person):
    name: str
    hp: int
```

この場合、"Warrior is a Person" と言える。しかし、"Warrior has a Person" では、違和感を覚える

次に、武器のクラスがあったとする

```python
class Weapon:
    name: str
    strength: int

# Person を継承して、Weapon を合成
class Warrior(Person):
    name: str
    hp: int
    weapon: Weapon
```

これだと、"Warrior has a weapon" でしっくりくる。"Warrior is a weapon" ではない。

## 抽象クラスと具象クラス

Abstract class and Concrete class
